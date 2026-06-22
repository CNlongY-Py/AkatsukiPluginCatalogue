import os
import traceback

from prompt_toolkit.completion import Completer, Completion
from libs import command, completer, events, logger, session
from plugins.solian.api import SolianWSClient
from plugins.solian.define import BASE_URL
from plugins.solian.sdk.client import SolarNetworkClient

log = logger.get_logger("Solian")

_http_clients = {}
_clients = {}


class SolianEventPayload(events.EventPayload):
    __slots__ = ("data", "account", "client")

    def __init__(self, log, cfg, data, account, client):
        super().__init__(log, cfg)
        self.data = data
        self.account = account
        self.client = client


def _fire(event_type, data, account=None):
    log.debug(f"_fire '{event_type}' account={account}")
    client = _http_clients.get(account) if account and account in _http_clients else SolarNetworkClient(base_url=BASE_URL)
    events.call_event(f"solian.{event_type}", data=data, account=account or "default", client=client)
    if account:
        events.call_event(f"solian.{account}.{event_type}", data=data, account=account, client=client)


def _make_callbacks(account):
    def on_open():
        _fire("on_connect", {}, account=account)
    def on_message(msg):
        log.debug(f"{account} << {msg.get('type')}")
        _fire("on_recv", {"type": msg.get("type", ""), "data": msg.get("data", {})}, account=account)
        _fire(msg.get("type", ""), msg.get("data", {}), account=account)
    def on_close(code, reason):
        _fire("on_close", {"close_status_code": code, "close_msg": reason}, account=account)
    return on_open, on_message, on_close


def _connect(account, token):
    if account in _clients and _clients[account].connected:
        log.warning(f"{account} already connected")
        return
    log.debug(f"connecting '{account}' ...")
    if account not in _http_clients:
        _http_clients[account] = SolarNetworkClient(base_url=BASE_URL)
    _http_clients[account].set_default_headers({"Authorization": f"Bearer {token}"})
    client = SolianWSClient(log=logger.get_logger(f"Solian.{account}"))
    client.on_open, client.on_message, client.on_close = _make_callbacks(account)
    client.start(token)
    _clients[account] = client


def _disconnect(account):
    log.debug(f"disconnecting '{account}' ...")
    client = _clients.pop(account, None)
    if client and client.connected:
        client.stop()
    _http_clients.pop(account, None)


def _active_accounts():
    return list(_clients.keys())


class _NameCompleter(Completer):
    def __init__(self, provider):
        self.provider = provider

    def get_completions(self, document, complete_event):
        text = document.text_before_cursor
        idx = text.rfind(" ")
        word = text[idx + 1:] if idx >= 0 else text
        for name in self.provider():
            if name.lower().startswith(word.lower()):
                yield Completion(name, start_position=-len(word))


def _plugin_ids():
    ids = set()
    for handlers in events.events.values():
        for h in handlers:
            ids.add(events._handler_name(h))
    from libs.command import _handlers, _dynamic_handlers
    for d in (_handlers, _dynamic_handlers):
        for h in d.values():
            ids.add(events._handler_name(h))
    return sorted(ids)


class _BindCompleter(Completer):
    def get_completions(self, document, complete_event):
        text = document.text_before_cursor
        idx = text.rfind(" ")
        word = text[idx + 1:] if idx >= 0 else text
        parts = text.split()
        if len(parts) <= 1 and not text.endswith(" "):
            items = _plugin_ids()
        else:
            items = list(session.list_accounts().keys())
        for item in items:
            if item.lower().startswith(word.lower()):
                yield Completion(item, start_position=-len(word))


# ---- init ----

@events.on_event("init_plugins")
def _start(payload):
    completer.register_hint(["/solian", "import"], "<token_file>")
    completer.register_hint(["/solian", "logout"], "<name>")
    completer.register_hint(["/solian", "reconnect"], "<name>")
    completer.register_hint(["/solian", "bind"], "<plugin_id> <account>")
    completer.register_hint(["/solian", "unbind"], "<plugin_id> [account]")
    completer.register_hint(["/solian", "status"], "")

    session.init(cfg_folder=payload.cfg.folder)
    for name, acc in session.list_accounts().items():
        if acc.token:
            _connect(name, acc.token)
    log.debug(f"auto-connected {len(_clients)} accounts")
    log.info(f"solian plugin initialized ({len(session.list_accounts())} accounts)")


# ---- import ----

@command.register(["/solian", "import"])
def _cmd_import(*args):
    if not args:
        log.info("usage: /solian import <token_file>")
        return

    token_path = " ".join(args)
    if not os.path.isfile(token_path):
        log.error(f"file not found: {token_path}")
        return

    with open(token_path) as f:
        token = f.read().strip()
    if not token:
        log.error("empty token")
        return

    temp_name = os.path.splitext(os.path.basename(token_path))[0]
    _connect(temp_name, token)

    http = _http_clients.get(temp_name)
    real_name = temp_name
    if http:
        try:
            real_name = http.accounts.get_current_account()["name"]
        except Exception:
            log.warning(f"failed to get account name\n{traceback.format_exc()}")

    if real_name != temp_name:
        log.debug(f"renamed account '{temp_name}' -> '{real_name}'")
        _clients[real_name] = _clients.pop(temp_name)
        _http_clients[real_name] = _http_clients.pop(temp_name)

    session.add_token_account(real_name, token)
    log.info(f"{real_name} imported")


# ---- account management ----

@command.register(["/solian", "logout"], dynamic=_NameCompleter(_active_accounts))
def _cmd_logout(*args):
    if not args:
        log.info("usage: /solian logout <name>")
        return
    name = args[0]
    _disconnect(name)
    session.remove_account(name)
    log.info(f"{name} logged out and removed")


@command.register(["/solian", "reconnect"], dynamic=_NameCompleter(_active_accounts))
def _cmd_reconnect(*args):
    if not args:
        log.info("reconnecting all accounts ...")
        for name in list(_clients.keys()):
            acc = session.get_account(name)
            if acc:
                _disconnect(name)
                _connect(name, acc.token)
                log.info(f"{name} reconnected")
        return
    name = args[0]
    acc = session.get_account(name)
    if not acc:
        log.error(f"account '{name}' not found")
        return
    _disconnect(name)
    _connect(name, acc.token)
    log.info(f"{name} reconnected")


# ---- plugin account binding ----

@command.register(["/solian", "bind"], dynamic=_BindCompleter())
def _cmd_bind(*args):
    if len(args) < 2:
        log.info("usage: /solian bind <plugin_id> <account>")
        return
    plugin_id = args[0]
    if plugin_id not in _plugin_ids():
        log.error(f"plugin '{plugin_id}' not found")
        return
    account_name = args[1]
    if not session.get_account(account_name):
        log.error(f"account '{account_name}' not found")
        return
    session.add_binding(plugin_id, account_name)
    log.info(f"'{plugin_id}' bound to '{account_name}'")


@command.register(["/solian", "unbind"], dynamic=_BindCompleter())
def _cmd_unbind(*args):
    if not args:
        log.info("usage: /solian unbind <plugin_id> [account]")
        return
    plugin_id = args[0]
    if session.get_bindings(plugin_id) is None:
        log.error(f"plugin '{plugin_id}' has no bindings")
        return
    if len(args) >= 2:
        session.remove_binding(plugin_id, args[1])
        log.info(f"'{plugin_id}' unbound from '{args[1]}'")
    else:
        session.remove_plugin(plugin_id)
        log.info(f"'{plugin_id}' unbound from all accounts")


# ---- status ----

@command.register(["/solian", "status"])
def _cmd_status():
    accounts = session.list_accounts()
    if not accounts:
        log.info("no accounts")
        return
    for name, acc in accounts.items():
        token_path = os.path.join(session.SESSIONS_DIR, f"{name}.token")
        client = _clients.get(name)
        if client and client.connected:
            st = client.status()
            log.info(f"{name} [{acc.auth_type}] connected {st['latency']:.0f}ms -> {token_path}")
        else:
            log.info(f"{name} [{acc.auth_type}] disconnected -> {token_path}")

    bindings = session.list_bindings()
    if bindings:
        for pid, accs in bindings.items():
            log.info(f"  {pid} -> {', '.join(accs)}")


import plugins.solian.debug
import plugins.solian.msg




import json
import sys
import traceback

from prompt_toolkit.completion import Completer, Completion

from libs import command, completer, logger, session

_LOG = logger.get_logger("Solian.debug")

# common API methods for completion
_COMMON_METHODS = [
    "accounts.get_current_account",
    "accounts.get_account_by_username",
    "accounts.get_account_by_id",
    "accounts.get_account_profile",
    "accounts.get_account_badges",
    "accounts.get_relationship",
    "accounts.get_followers",
    "accounts.get_following",
    "accounts.get_friends_overview",
    "accounts.check_in",
    "accounts.get_social_credits",
    "accounts.get_social_credit_history",
    "accounts.get_achievement_state",
    "accounts.get_quest_states",
    "accounts.get_daily_fortune",
    "accounts.get_random_fortune_saying",
    "accounts.get_event_calendar",
    "accounts.get_next_notable_day",
    "accounts.get_my_badges",
    "accounts.get_action_log",
    "accounts.get_my_realms",
    "accounts.join_realm",
    "accounts.leave_realm",
    "accounts.submit_abuse_report",
    "accounts.create_affiliation_spell",
    "accounts.list_affiliation_spells",
    "accounts.get_event_countdowns",
    "chat.get_rooms",
    "chat.get_messages",
    "chat.send_message",
    "chat.get_conversations",
    "chat.create_group",
    "chat.get_group_info",
    "sphere.get_sphere",
    "sphere.list_spheres",
    "sphere.join_sphere",
    "sphere.leave_sphere",
    "sphere.get_members",
    "sphere.get_roles",
    "wallet.get_balance",
    "wallet.get_transactions",
    "wallet.send",
    "auth.refresh",
    "auth.verify",
    "notifications.list",
    "notifications.mark_read",
    "thoughts.get_timeline",
    "thoughts.create_post",
    "drive.list_files",
    "drive.upload",
    "ws.send",
    "ws.status",
    "ws.connected",
    "ws.latency",
]


def _get_solian():
    return sys.modules.get("plugins.solian")


class _ApiCompleter(Completer):
    def get_completions(self, document, complete_event):
        text = document.text_before_cursor
        idx = text.rfind(" ")
        word = text[idx + 1:] if idx >= 0 else text
        parts = text.split()

        if len(parts) <= 1 and not text.endswith(" "):
            items = list(session.list_accounts().keys())
        else:
            items = _COMMON_METHODS

        for item in items:
            if item.lower().startswith(word.lower()):
                yield Completion(item, start_position=-len(word))


completer.register_hint(["/solian_api"], "<account> <method_path> {args}")


@command.register(["/solian_api"], dynamic=_ApiCompleter())
def _cmd_api(*args):
    if len(args) < 2:
        _LOG.info("usage: /solian_api <account> <method_path> [json_args]")
        _LOG.info("  HTTP: /solian_api Akatsuki accounts.get_current_account")
        _LOG.info("  HTTP: /solian_api Akatsuki accounts.get_account_by_username {\"username\":\"x\"}")
        _LOG.info("  WS:   /solian_api Akatsuki ws.send {\"type\":\"ping\",\"data\":{}}")
        _LOG.info("  WS:   /solian_api Akatsuki ws.status")
        return

    solian = _get_solian()
    if not solian:
        _LOG.error("solian plugin not loaded")
        return

    account = args[0]
    api_path = args[1]
    json_args = " ".join(args[2:]) if len(args) > 2 else "{}"

    try:
        kwargs = json.loads(json_args)
    except json.JSONDecodeError:
        _LOG.error("invalid json args")
        return

    if not isinstance(kwargs, dict):
        _LOG.error("args must be a json object")
        return

    if api_path.startswith("ws."):
        ws = solian._clients.get(account)
        if not ws:
            _LOG.error(f"no ws connection for '{account}'")
            return
        obj = ws
        path = api_path[3:]
    else:
        http = solian._http_clients.get(account)
        if not http:
            _LOG.error(f"no http client for '{account}'")
            return
        obj = http
        path = api_path

    parts = path.split(".")
    for part in parts:
        obj = getattr(obj, part, None)
        if obj is None:
            _LOG.error(f"attribute '{part}' not found in '{api_path}'")
            return

    def _fmt(val):
        if isinstance(val, (dict, list)):
            return "\n  " + json.dumps(val, indent=2, ensure_ascii=False).replace("\n", "\n  ")
        return f" {val}"

    if not callable(obj):
        _LOG.info(f"{api_path} ={_fmt(obj)}")
        return

    try:
        result = obj(**kwargs)
        _LOG.info(f"{api_path} ->{_fmt(result)}")
    except Exception:
        _LOG.error(f"{api_path} failed\n{traceback.format_exc()}")

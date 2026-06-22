from libs import events, logger
from plugins.solian.define import MESSAGES_NEW

META = {
    "name": "Solian.Message",
    "version": "1.0.0",
    "author": "CNlongY",
    "description": "Print incoming chat messages",
}


@events.on_event(MESSAGES_NEW)
def handler(payload):
    log = logger.get_logger(f"Solian.{payload.account}")
    data = payload.data
    content = data.get("content", "")
    sender = data.get("sender", {})
    chat_room = sender.get("chat_room", {})
    sender_account = sender.get("account", {})
    group = chat_room.get("name") or "私聊消息"
    user = sender_account.get("nick", "?")
    log.info(f"[{group}]<{user}> {content}")

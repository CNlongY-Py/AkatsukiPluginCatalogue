# `define.py` — 常量定义

## 网络

| 常量 | 值 | 说明 |
|------|-----|------|
| `BASE_URL` | `https://api.solian.app` | HTTP API 基础 URL |
| `WS_URL` | `wss://api.solian.app/ws` | WebSocket 连接 URL |

## 心跳与重连

| 常量 | 默认值 | 说明 |
|------|--------|------|
| `HEARTBEAT_INTERVAL` | 30 | 心跳间隔（秒），传给 `ping_interval` |
| `RECONNECT_DELAY` | 5 | 初始重连延迟（秒） |
| `RECONNECT_MAX_DELAY` | 60 | 最大重连延迟（秒） |

## 事件常量

所有 S2C 事件以 `solian.` 前缀命名，共 42 个：

| 常量 | 值 |
|------|-----|
| `MESSAGES_DELIVERED` | `solian.messages.delivered` |
| `MESSAGES_NEW` | `solian.messages.new` |
| `MESSAGES_UPDATE` | `solian.messages.update` |
| `MESSAGES_DELETE` | `solian.messages.delete` |
| `MESSAGES_TYPING` | `solian.messages.typing` |
| `MESSAGES_PINNED` | `solian.messages.pinned` |
| `MESSAGES_UNPINNED` | `solian.messages.unpinned` |
| `MESSAGES_READ` | `solian.messages.read` |
| `CHAT_PRESENCE_UPDATED` | `solian.chat.presence.updated` |
| `CHAT_PRESENCE_ACTIVITIES_UPDATED` | `solian.chat.presence.activities.updated` |
| `CALL_INVITED` | `solian.call.invited` |
| `ERROR` | `solian.error` |
| `PLACEHOLDER_UPDATE` | `solian.placeholder.update` |
| `PLACEHOLDER_EXPIRED` | `solian.placeholder.expired` |
| `PLACEHOLDER_FINALIZE` | `solian.placeholder.finalize` |
| `ACCOUNT_STATUS_UPDATED` | `solian.account.status.updated` |
| `ACCOUNT_PRESENCE_ACTIVITIES_UPDATED` | `solian.account.presence.activities.updated` |
| `PROGRESSION_COMPLETED` | `solian.progression.completed` |
| `AUTH_CHALLENGE_PENDING` | `solian.auth.challenge.pending` |
| `AUTH_CHALLENGE_APPROVED` | `solian.auth.challenge.approved` |
| `AUTH_CHALLENGE_DECLINED` | `solian.auth.challenge.declined` |
| `QR_LOGIN_SCANNED` | `solian.qr.login.scanned` |
| `QR_LOGIN_APPROVED` | `solian.qr.login.approved` |
| `QR_LOGIN_DECLINED` | `solian.qr.login.declined` |
| `E2EE_ENVELOPE` | `solian.e2ee.envelope` |
| `E2EE_GROUP_RESET` | `solian.e2ee.group.reset` |
| `KP_DEPLETED` | `solian.kp.depleted` |
| `POST_CREATED` | `solian.post.created` |
| `POST_UPDATED` | `solian.post.updated` |
| `POST_DELETED` | `solian.post.deleted` |
| `POST_REACTION` | `solian.post.reaction.*` |
| `STREAM_STARTED` | `solian.stream_started` |
| `STREAM_ENDED` | `solian.stream_ended` |
| `STREAM_UPDATED` | `solian.stream_updated` |
| `STREAM_AWARDED` | `solian.stream_awarded` |
| `WALLET_TRANSACTION_CREATED` | `solian.wallet.transaction.created` |
| `WALLET_TRANSACTION_CONFIRMED` | `solian.wallet.transaction.confirmed` |
| `WALLET_TRANSACTION_EXPIRED` | `solian.wallet.transaction.expired` |
| `WALLET_TRANSACTION_REFUNDED` | `solian.wallet.transaction.refunded` |
| `WALLET_POCKET_UPDATED` | `solian.wallet.pocket.updated` |
| `WALLET_FUND_CONTRIBUTED` | `solian.wallet.fund.contributed` |
| `WALLET_FUND_COMPLETED` | `solian.wallet.fund.completed` |

## 事件分组（`S2C_GROUPS`）

按主题分组，方便遍历：

```python
S2C_GROUPS = {
    "messages": ["delivered", "new", "update", ...],
    "chat": ["presence.updated", "presence.activities.updated"],
    "post": ["created", "updated", "deleted", "reaction.*"],
    "wallet": ["transaction.created", "transaction.confirmed", ...],
    ...
}
```

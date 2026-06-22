BASE_URL = "https://api.solian.app"
WS_URL = "wss://api.solian.app/ws"
HEARTBEAT_INTERVAL = 30
RECONNECT_DELAY = 5
RECONNECT_MAX_DELAY = 60
POST_REACTION_PREFIX = "solian.post.reaction."

MESSAGES_DELIVERED = "solian.messages.delivered"
MESSAGES_NEW = "solian.messages.new"
MESSAGES_UPDATE = "solian.messages.update"
MESSAGES_DELETE = "solian.messages.delete"
MESSAGES_TYPING = "solian.messages.typing"
MESSAGES_PINNED = "solian.messages.pinned"
MESSAGES_UNPINNED = "solian.messages.unpinned"
MESSAGES_READ = "solian.messages.read"
CHAT_PRESENCE_UPDATED = "solian.chat.presence.updated"
CHAT_PRESENCE_ACTIVITIES_UPDATED = "solian.chat.presence.activities.updated"
CALL_INVITED = "solian.call.invited"
ERROR = "solian.error"
PLACEHOLDER_UPDATE = "solian.placeholder.update"
PLACEHOLDER_EXPIRED = "solian.placeholder.expired"
PLACEHOLDER_FINALIZE = "solian.placeholder.finalize"

ACCOUNT_STATUS_UPDATED = "solian.account.status.updated"
ACCOUNT_PRESENCE_ACTIVITIES_UPDATED = "solian.account.presence.activities.updated"
PROGRESSION_COMPLETED = "solian.progression.completed"

AUTH_CHALLENGE_PENDING = "solian.auth.challenge.pending"
AUTH_CHALLENGE_APPROVED = "solian.auth.challenge.approved"
AUTH_CHALLENGE_DECLINED = "solian.auth.challenge.declined"
QR_LOGIN_SCANNED = "solian.qr.login.scanned"
QR_LOGIN_APPROVED = "solian.qr.login.approved"
QR_LOGIN_DECLINED = "solian.qr.login.declined"
E2EE_ENVELOPE = "solian.e2ee.envelope"
E2EE_GROUP_RESET = "solian.e2ee.group.reset"
KP_DEPLETED = "solian.kp.depleted"

POST_CREATED = "solian.post.created"
POST_UPDATED = "solian.post.updated"
POST_DELETED = "solian.post.deleted"
POST_REACTION = "solian.post.reaction.*"

STREAM_STARTED = "solian.stream_started"
STREAM_ENDED = "solian.stream_ended"
STREAM_UPDATED = "solian.stream_updated"
STREAM_AWARDED = "solian.stream_awarded"

WALLET_TRANSACTION_CREATED = "solian.wallet.transaction.created"
WALLET_TRANSACTION_CONFIRMED = "solian.wallet.transaction.confirmed"
WALLET_TRANSACTION_EXPIRED = "solian.wallet.transaction.expired"
WALLET_TRANSACTION_REFUNDED = "solian.wallet.transaction.refunded"
WALLET_POCKET_UPDATED = "solian.wallet.pocket.updated"
WALLET_FUND_CONTRIBUTED = "solian.wallet.fund.contributed"
WALLET_FUND_COMPLETED = "solian.wallet.fund.completed"

S2C_EVENTS = [
    MESSAGES_DELIVERED,
    MESSAGES_NEW,
    MESSAGES_UPDATE,
    MESSAGES_DELETE,
    MESSAGES_TYPING,
    MESSAGES_PINNED,
    MESSAGES_UNPINNED,
    MESSAGES_READ,
    CHAT_PRESENCE_UPDATED,
    CHAT_PRESENCE_ACTIVITIES_UPDATED,
    CALL_INVITED,
    ERROR,
    PLACEHOLDER_UPDATE,
    PLACEHOLDER_EXPIRED,
    PLACEHOLDER_FINALIZE,
    ACCOUNT_STATUS_UPDATED,
    ACCOUNT_PRESENCE_ACTIVITIES_UPDATED,
    PROGRESSION_COMPLETED,
    AUTH_CHALLENGE_PENDING,
    AUTH_CHALLENGE_APPROVED,
    AUTH_CHALLENGE_DECLINED,
    QR_LOGIN_SCANNED,
    QR_LOGIN_APPROVED,
    QR_LOGIN_DECLINED,
    E2EE_ENVELOPE,
    E2EE_GROUP_RESET,
    KP_DEPLETED,
    POST_CREATED,
    POST_UPDATED,
    POST_DELETED,
    POST_REACTION,
    STREAM_STARTED,
    STREAM_ENDED,
    STREAM_UPDATED,
    STREAM_AWARDED,
    WALLET_TRANSACTION_CREATED,
    WALLET_TRANSACTION_CONFIRMED,
    WALLET_TRANSACTION_EXPIRED,
    WALLET_TRANSACTION_REFUNDED,
    WALLET_POCKET_UPDATED,
    WALLET_FUND_CONTRIBUTED,
    WALLET_FUND_COMPLETED,
]

S2C_GROUPS = {
    "messages": ["delivered", "new", "update", "delete", "typing", "pinned", "unpinned", "read"],
    "chat": ["presence.updated", "presence.activities.updated"],
    "call": ["invited"],
    "error": [],
    "placeholder": ["update", "expired", "finalize"],
    "account": ["status.updated", "presence.activities.updated"],
    "progression": ["completed"],
    "auth": ["challenge.pending", "challenge.approved", "challenge.declined"],
    "qr": ["login.scanned", "login.approved", "login.declined"],
    "e2ee": ["envelope", "group.reset"],
    "kp": ["depleted"],
    "post": ["created", "updated", "deleted", "reaction.*"],
    "stream": ["started", "ended", "updated", "awarded"],
    "wallet": ["transaction.created", "transaction.confirmed", "transaction.expired", "transaction.refunded", "pocket.updated", "fund.contributed", "fund.completed"],
}

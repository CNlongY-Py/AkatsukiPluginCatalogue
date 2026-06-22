from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, Field

from ..accounts.account import SnAccount, SnAccountStatus
from ..drive.file import SnCloudFileReference
from ..realms.realm import SnRealm, SnRealmLabel


class SnChatGroup(BaseModel):
    id: str = ""
    account_id: str = ""
    name: str = ""
    color: Optional[str] = None
    icon: Optional[str] = None
    order: int = 0
    room_ids: list[str] = Field(default_factory=list)
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


class SnChatReaction(BaseModel):
    id: str = ""
    message_id: str = ""
    sender_id: str = ""
    sender: Optional[SnChatMember] = None
    symbol: str = ""
    attitude: int = 0
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None


class SnChatRoom(BaseModel):
    id: str = ""
    name: Optional[str] = None
    description: Optional[str] = None
    type: int = 0
    encryption_mode: int = 0
    mls_group_id: Optional[str] = None
    is_public: bool = False
    is_community: bool = False
    picture: Optional[SnCloudFileReference] = None
    background: Optional[SnCloudFileReference] = None
    realm_id: Optional[str] = None
    account_id: Optional[str] = None
    realm: Optional[SnRealm] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    members: Optional[list[SnChatMember]] = None
    is_pinned: bool = False


class SnChatMember(BaseModel):
    id: str = ""
    chat_room_id: str = ""
    chat_room: Optional[SnChatRoom] = None
    account_id: str = ""
    account: Optional[SnAccount] = None
    nick: Optional[str] = None
    notify: int = 0
    joined_at: Optional[str] = None
    break_until: Optional[str] = None
    timeout_until: Optional[str] = None
    chat_group_id: Optional[str] = None
    chat_group: Optional[SnChatGroup] = None
    last_read_at: Optional[str] = None
    status: Optional[SnAccountStatus] = None
    realm_nick: Optional[str] = None
    realm_bio: Optional[str] = None
    realm_experience: Optional[int] = None
    realm_level: Optional[int] = None
    realm_leveling_progress: Optional[float] = None
    realm_label: Optional[SnRealmLabel] = None
    last_typed: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None


class SnChatMessage(BaseModel):
    id: str = ""
    type: str = "text"
    content: Optional[str] = None
    client_message_id: Optional[str] = None
    nonce: Optional[str] = None
    meta: dict[str, Any] = Field(default_factory=dict)
    members_mentioned: list[str] = Field(default_factory=list)
    edited_at: Optional[str] = None
    attachments: list[SnCloudFileReference] = Field(default_factory=list)
    reactions: list[SnChatReaction] = Field(default_factory=list)
    reactions_count: dict[str, int] = Field(default_factory=dict)
    reactions_made: dict[str, bool] = Field(default_factory=dict)
    replied_message_id: Optional[str] = None
    forwarded_message_id: Optional[str] = None
    sender_id: str = ""
    sender: Optional[SnChatMember] = None
    chat_room_id: str = ""
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None


class SnChatSummary(BaseModel):
    unread_count: int = 0
    last_message: Optional[SnChatMessage] = None


class SnChatOnlineAccount(BaseModel):
    id: str = ""
    name: str = ""
    nick: str = ""


class SnChatOnlineStatus(BaseModel):
    online_count: int = 0
    direct_message_status: Optional[SnAccountStatus] = None
    online_user_names: list[str] = Field(default_factory=list)
    online_accounts: list[SnChatOnlineAccount] = Field(default_factory=list)


class CallParticipant(BaseModel):
    identity: str = ""
    name: str = ""
    joined_at: Optional[str] = None


class SnRealtimeCall(BaseModel):
    id: str = ""
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    ended_at: Optional[str] = None
    sender_id: str = ""
    sender: Optional[SnChatMember] = None
    room_id: str = ""
    room: Optional[SnChatRoom] = None
    upstream_config: dict[str, Any] = Field(default_factory=dict)
    provider_name: Optional[str] = None
    session_id: Optional[str] = None

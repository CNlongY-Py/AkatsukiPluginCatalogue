from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, Field

from ..accounts.account import SnAccount, SnAccountStatus
from ..drive.file import SnCloudFileReference


class SnRealm(BaseModel):
    id: str = ""
    slug: str = ""
    name: str = ""
    description: str = ""
    verified_as: Optional[str] = None
    verified_at: Optional[str] = None
    is_community: bool = False
    is_public: bool = False
    picture: Optional[SnCloudFileReference] = None
    background: Optional[SnCloudFileReference] = None
    account_id: str = ""
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    boost_points: int = 0
    boost_level: int = 0


class SnRealmMember(BaseModel):
    realm_id: str = ""
    realm: Optional[SnRealm] = None
    account_id: str = ""
    account: Optional[SnAccount] = None
    role: int = 0
    joined_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    status: Optional[SnAccountStatus] = None
    nick: Optional[str] = None
    bio: Optional[str] = None
    label_id: Optional[str] = None
    label: Optional[SnRealmLabel] = None
    experience: int = 0
    level: int = 0
    leveling_progress: float = 0.0


class SnRealmLabel(BaseModel):
    id: str = ""
    realm_id: str = ""
    name: str = ""
    description: str = ""
    color: Optional[str] = None
    icon: Optional[str] = None
    created_by_account_id: str = ""
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Any = None


class SnRealmRolePermission(BaseModel):
    role_level: int = 0
    can_chat: bool = True
    can_post: bool = True
    can_comment: bool = True
    can_upload_media: bool = True
    can_moderate_posts: bool = False
    can_moderate_chat: bool = False
    can_manage_members: bool = False
    can_manage_realm: bool = False


class SnRealmUserPermission(BaseModel):
    account_id: str = ""
    can_chat: Optional[bool] = None
    can_post: Optional[bool] = None
    can_comment: Optional[bool] = None
    can_upload_media: Optional[bool] = None
    can_moderate_posts: Optional[bool] = None
    can_moderate_chat: Optional[bool] = None
    can_manage_members: Optional[bool] = None
    can_manage_realm: Optional[bool] = None

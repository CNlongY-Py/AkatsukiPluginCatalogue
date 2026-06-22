from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, Field


class SnActivityPubInstance(BaseModel):
    id: str = ""
    domain: str = ""
    name: Optional[str] = None
    description: Optional[str] = None
    software: Optional[str] = None
    version: Optional[str] = None
    icon_url: Optional[str] = None
    thumbnail_url: Optional[str] = None
    contact_email: Optional[str] = None
    contact_account_username: Optional[str] = None
    active_users: Optional[int] = None
    is_blocked: bool = False
    is_silenced: bool = False
    block_reason: Optional[str] = None
    metadata: Optional[dict[str, Any]] = None
    last_fetched_at: Optional[str] = None
    last_activity_at: Optional[str] = None
    metadata_fetched_at: Optional[str] = None


class SnActivityPubUser(BaseModel):
    actor_uri: str = ""
    username: str = ""
    display_name: str = ""
    bio: str = ""
    avatar_url: str = ""
    followed_at: Optional[str] = None
    is_local: bool = False
    instance_domain: str = ""


class SnActivityPubActor(BaseModel):
    id: str = ""
    uri: str = ""
    type: str = "Person"
    full_handle: str = ""
    display_name: Optional[str] = None
    username: str = ""
    bio: Optional[str] = None
    inbox_uri: Optional[str] = None
    outbox_uri: Optional[str] = None
    followers_uri: Optional[str] = None
    following_uri: Optional[str] = None
    featured_uri: Optional[str] = None
    avatar_url: Optional[str] = None
    header_url: Optional[str] = None
    public_key_id: Optional[str] = None
    public_key: Optional[str] = None
    is_bot: bool = False
    is_locked: bool = False
    is_discoverable: bool = True
    endpoints: Optional[dict[str, Any]] = None
    public_key_data: Optional[dict[str, Any]] = None
    metadata: Optional[dict[str, Any]] = None
    last_fetched_at: Optional[str] = None
    last_activity_at: Optional[str] = None
    instance: Optional[SnActivityPubInstance] = None
    instance_id: str = ""
    is_following: Optional[bool] = None
    followers_count: Optional[int] = None
    following_count: Optional[int] = None
    total_post_count: Optional[int] = None
    web_url: Optional[str] = None
    recent_posts: Optional[list[Any]] = None


class SnActivityPubFollowResponse(BaseModel):
    success: bool = False
    message: str = ""


class SnActorStatusResponse(BaseModel):
    enabled: bool = False
    follower_count: int = 0
    actor: Optional[SnActivityPubActor] = None
    actor_uri: Optional[str] = None

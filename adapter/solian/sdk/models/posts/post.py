from __future__ import annotations

from enum import IntEnum
from typing import Any, Optional

from pydantic import BaseModel, Field

from ..accounts.account import SnAccount
from ..drive.file import SnCloudFileReference
from ..activity.activitypub import SnActivityPubActor
from .publisher import SnPublisher
from .post_tag import SnPostTag
from .post_category import SnPostCategory
from .post_collection import SnPostCollection
from ..realms.realm import SnRealm


class PostEmbedViewRenderer(IntEnum):
    web_view = 0


class SnPostEmbedView(BaseModel):
    uri: str = ""
    aspect_ratio: Optional[float] = None
    renderer: PostEmbedViewRenderer = PostEmbedViewRenderer.web_view


class SnPost(BaseModel):
    id: str = ""
    title: Optional[str] = None
    description: Optional[str] = None
    language: Optional[str] = None
    edited_at: Optional[str] = None
    drafted_at: Optional[str] = None
    published_at: Optional[str] = None
    visibility: int = 0
    content: Optional[str] = None
    slug: Optional[str] = None
    type: int = 0
    meta: Optional[dict[str, Any]] = None
    embed_view: Optional[SnPostEmbedView] = None
    views_unique: int = 0
    views_total: int = 0
    upvotes: int = 0
    downvotes: int = 0
    replies_count: int = 0
    threaded_replies_count: int = 0
    debug_rank: Optional[float] = None
    awarded_score: int = 0
    pin_mode: Optional[int] = None
    threaded_post_id: Optional[str] = None
    threaded_post: Optional[SnPost] = None
    replied_post_id: Optional[str] = None
    replied_post: Optional[SnPost] = None
    forwarded_post_id: Optional[str] = None
    forwarded_post: Optional[SnPost] = None
    realm_id: Optional[str] = None
    realm: Optional[SnRealm] = None
    publisher_id: Optional[str] = None
    publisher: Optional[SnPublisher] = None
    actorid: Optional[str] = None
    actor: Optional[SnActivityPubActor] = None
    fediverse_uri: Optional[str] = None
    fediverse_type: Optional[int] = None
    is_cached: bool = True
    content_type: int = 0
    attachments: list[SnCloudFileReference] = Field(default_factory=list)
    reactions_count: dict[str, int] = Field(default_factory=dict)
    reactions_made: dict[str, bool] = Field(default_factory=dict)
    reactions: list[Any] = Field(default_factory=list)
    tags: list[SnPostTag] = Field(default_factory=list)
    categories: list[SnPostCategory] = Field(default_factory=list)
    collections: list[Any] = Field(default_factory=list)
    publisher_collections: list[SnPostCollection] = Field(default_factory=list)
    featured_records: list[SnPostFeaturedRecord] = Field(default_factory=list)
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    replied_gone: bool = False
    forwarded_gone: bool = False
    is_truncated: bool = False
    boosted_by: Optional[SnActivityPubActor] = None
    boosted_at: Optional[str] = None
    is_bookmarked: bool = False


class SnPublisherStats(BaseModel):
    posts_created: int = 0
    sticker_packs_created: int = 0
    stickers_created: int = 0
    upvote_received: int = 0
    downvote_received: int = 0


class SnPublisherSubscriptionCompact(BaseModel):
    account_id: str = ""
    publisher_id: str = ""
    publisher: Optional[SnPublisher] = None


class ReactInfo(BaseModel):
    icon: str = ""
    attitude: int = 0


class SnPostAward(BaseModel):
    id: str = ""
    amount: float = 0.0
    attitude: int = 0
    message: Optional[str] = None
    post_id: str = ""
    account_id: str = ""
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None


class SnPostReaction(BaseModel):
    id: str = ""
    symbol: str = ""
    attitude: int = 0
    post_id: str = ""
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    actor_id: Optional[str] = None
    actor: Optional[SnActivityPubActor] = None
    account_id: Optional[str] = None
    account: Optional[SnAccount] = None
    is_local: Optional[bool] = None
    fediverse_uri: Optional[str] = None
    deleted_at: Optional[str] = None


class SnPostBookmark(BaseModel):
    id: str = ""
    post_id: str = ""
    account_id: str = ""
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


class UserReactionListingItem(BaseModel):
    reaction: Optional[SnPostReaction] = None
    post: Optional[SnPost] = None


class SnPostFeaturedRecord(BaseModel):
    id: str = ""
    post_id: str = ""
    featured_at: Optional[str] = None
    social_credits: int = 0
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None

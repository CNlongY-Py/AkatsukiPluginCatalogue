from __future__ import annotations

from enum import IntEnum
from typing import Optional

from pydantic import BaseModel, Field

from ..accounts.account import SnAccount, SnVerificationMark
from ..drive.file import SnCloudFileReference
from ..realms.realm import SnRealm, SnRealmLabel


class FollowRequestState(IntEnum):
    pending = 0
    accepted = 1
    rejected = 2


class SubscriptionEndReason:
    user_left = "UserLeft"
    removed_by_publisher = "RemovedByPublisher"


class SnPublisher(BaseModel):
    id: str = ""
    type: int = 0
    name: str = ""
    nick: str = ""
    bio: str = ""
    realm_nick: Optional[str] = None
    realm_bio: Optional[str] = None
    realm_experience: Optional[int] = None
    realm_level: Optional[int] = None
    realm_leveling_progress: Optional[float] = None
    realm_label: Optional[SnRealmLabel] = None
    picture: Optional[SnCloudFileReference] = None
    background: Optional[SnCloudFileReference] = None
    account: Optional[SnAccount] = None
    account_id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    realm_id: Optional[str] = None
    realm: Optional[SnRealm] = None
    verification: Optional[SnVerificationMark] = None
    is_shadowbanned: bool = False
    is_gatekept: bool = False
    is_moderate_subscription: bool = False
    rating: float = 100.0
    rating_level: int = 0


class SnPublisherMember(BaseModel):
    publisher_id: str = ""
    publisher: Optional[SnPublisher] = None
    account_id: str = ""
    account: Optional[SnAccount] = None
    role: int = 0
    joined_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None


class SnPublisherFollowRequest(BaseModel):
    id: str = ""
    publisher_id: str = ""
    account_id: str = ""
    state: FollowRequestState = FollowRequestState.pending
    reject_reason: Optional[str] = None
    created_at: Optional[str] = None
    reviewed_at: Optional[str] = None
    reviewed_by_account_id: Optional[str] = None
    account: Optional[SnAccount] = None


class SnPublisherFollowResponse(BaseModel):
    request_id: Optional[str] = None
    state: Optional[FollowRequestState] = None
    message: Optional[str] = None


class SnPublisherFollowRequestListResponse(BaseModel):
    requests: list[SnPublisherFollowRequest] = Field(default_factory=list)


class SnPublisherFollowStatus(BaseModel):
    is_subscribed: bool = False
    follow_request_state: Optional[FollowRequestState] = None
    follow_request_id: Optional[str] = None


class SnPublisherSubscription(BaseModel):
    id: str = ""
    publisher_id: str = ""
    account_id: str = ""
    last_read_at: Optional[str] = None
    notify: bool = True
    ended_at: Optional[str] = None
    end_reason: Optional[str] = None
    ended_by_account_id: Optional[str] = None
    is_active: bool = True
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


class SnPublisherSubscriptionStatus(BaseModel):
    subscription: Optional[SnPublisherSubscription] = None
    follow_request: Optional[SnPublisherFollowRequest] = None
    requires_approval: bool = False
    status: str = "none"
    message: str = ""
    is_pending: bool = False
    is_active: bool = False


class SnPublisherSubscriber(BaseModel):
    subscription: Optional[SnPublisherSubscription] = None
    account: Optional[SnAccount] = None


class SnPublisherRatingOverview(BaseModel):
    rating: float = 0.0
    rank: int = 0
    total_publishers: int = 0
    percentile: float = 0.0
    grade: str = ""

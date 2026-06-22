from __future__ import annotations

from enum import IntEnum
from typing import Any, Optional

from pydantic import BaseModel, Field

from ..drive.file import SnCloudFileReference


class SnWalletSubscriptionRef(BaseModel):
    id: str = ""
    is_active: bool = False
    account_id: str = ""
    created_at: Optional[str] = None
    deleted_at: Optional[str] = None
    updated_at: Optional[str] = None
    identifier: str = ""


class SnEventVisibility(IntEnum):
    private = 0
    friends = 100
    public = 200


class SnRecurrenceFrequency(IntEnum):
    none = 0
    daily = 1
    weekly = 2
    monthly = 3
    yearly = 4


class SnMergedEventType:
    user_event = "UserEvent"
    check_in = "CheckIn"
    status = "Status"
    notable_day = "NotableDay"


class SnNotificationPreferenceLevel(IntEnum):
    normal = 0
    silent = 1
    reject = 2


class SnNotificationPushSubscriptionProvider(IntEnum):
    fcm = 0
    apple = 1
    sop = 2
    unified_push = 3
    appk = 4


class ProfileLink(BaseModel):
    name: str = ""
    url: str = ""


class UsernameColor(BaseModel):
    type: str = "plain"
    value: Optional[str] = None
    direction: Optional[str] = None
    colors: Optional[list[str]] = None


class SnVerificationMark(BaseModel):
    type: int = 0
    title: Optional[str] = None
    description: Optional[str] = None
    verified_by: Optional[str] = None


class SnAccountProfileRef(BaseModel):
    id: str = ""
    first_name: str = ""
    middle_name: str = ""
    last_name: str = ""
    bio: str = ""
    picture: Optional[SnCloudFileReference] = None
    background: Optional[SnCloudFileReference] = None
    verification: Optional[SnVerificationMark] = None
    username_color: Optional[UsernameColor] = None


class SnAccountReference(BaseModel):
    id: str = ""
    name: str = ""
    nick: str = ""
    profile: Optional[SnAccountProfileRef] = None
    badges: list[SnAccountBadge] = Field(default_factory=list)
    automated_id: Optional[str] = None


class SnAccountProfile(BaseModel):
    id: str = ""
    first_name: str = ""
    middle_name: str = ""
    last_name: str = ""
    bio: str = ""
    gender: str = ""
    pronouns: str = ""
    location: str = ""
    time_zone: str = ""
    birthday: Optional[str] = None
    links: list[ProfileLink] = Field(default_factory=list)
    last_seen_at: Optional[str] = None
    active_badge: Optional[SnAccountBadge] = None
    experience: int = 0
    level: int = 0
    social_credits: float = 100.0
    social_credits_level: int = 0
    leveling_progress: float = 0.0
    picture: Optional[SnCloudFileReference] = None
    background: Optional[SnCloudFileReference] = None
    verification: Optional[SnVerificationMark] = None
    username_color: Optional[UsernameColor] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None


class SnAccount(BaseModel):
    id: str = ""
    name: str = ""
    nick: str = ""
    language: str = ""
    region: str = ""
    is_superuser: bool = False
    automated_id: Optional[str] = None
    profile: Optional[SnAccountProfile] = None
    perk_subscription: Optional[SnWalletSubscriptionRef] = None
    badges: list[SnAccountBadge] = Field(default_factory=list)
    contacts: list[SnContactMethod] = Field(default_factory=list)
    activated_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None


class SnAccountStatus(BaseModel):
    id: str = ""
    attitude: int = 0
    is_online: bool = False
    is_idle: bool = False
    idle_since: Optional[str] = None
    is_customized: bool = False
    type: int = 0
    label: str = ""
    symbol: Optional[str] = None
    meta: Optional[dict[str, Any]] = None
    cleared_at: Optional[str] = None
    app_identifier: Optional[str] = None
    is_automated: bool = False
    account_id: str = ""
    account: Optional[SnAccount] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None


class SnAccountBadge(BaseModel):
    id: str = ""
    type: str = ""
    label: Optional[str] = None
    caption: Optional[str] = None
    meta: dict[str, Any] = Field(default_factory=dict)
    expired_at: Optional[str] = None
    account_id: str = ""
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    activated_at: Optional[str] = None
    deleted_at: Optional[str] = None


class BadgeManifestSeries(BaseModel):
    identifier: str = ""
    title: Optional[str] = None
    order: int = 0


class BadgeManifestEntry(BaseModel):
    identifier: str = ""
    achievement_identifier: Optional[str] = None
    label: Optional[str] = None
    caption: Optional[str] = None
    icon: Optional[str] = None
    color: Optional[str] = None
    icon_url: Optional[str] = None
    localization_key: Optional[str] = None
    category: Optional[str] = None
    series: Optional[BadgeManifestSeries] = None
    hidden: bool = False


class SnContactMethod(BaseModel):
    id: str = ""
    type: int = 0
    verified_at: Optional[str] = None
    is_primary: bool = False
    is_public: bool = False
    content: str = ""
    account_id: str = ""
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None


class SnNotification(BaseModel):
    id: str = ""
    app_id: Optional[str] = None
    topic: str = ""
    title: str = ""
    subtitle: str = ""
    body: str = ""
    meta: dict[str, Any] = Field(default_factory=dict)
    viewed_at: Optional[str] = None
    account_id: str = ""
    created_at: Optional[str] = None


class SnNotificationTopic(BaseModel):
    topic: str = ""
    description: str = ""
    is_custom: bool = False


class SnNotificationPreference(BaseModel):
    id: str = ""
    account_id: str = ""
    topic: str = ""
    preference: SnNotificationPreferenceLevel = SnNotificationPreferenceLevel.normal
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None


class SnNotificationPushSubscription(BaseModel):
    id: str = ""
    account_id: str = ""
    app_id: Optional[str] = None
    device_id: str = ""
    device_token: str = ""
    device_name: Optional[str] = None
    provider: SnNotificationPushSubscriptionProvider = SnNotificationPushSubscriptionProvider.fcm
    is_activated: bool = False
    last_used_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


class SnExperienceRecord(BaseModel):
    id: str = ""
    delta: int = 0
    reason_type: str = ""
    reason: str = ""
    bonus_multiplier: Optional[float] = 1.0
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None


class SnSocialCreditRecord(BaseModel):
    id: str = ""
    delta: float = 0.0
    reason_type: str = ""
    reason: str = ""
    expired_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None


class SnAuthDevice(BaseModel):
    id: str = ""
    device_id: str = ""
    device_name: str = ""
    device_label: Optional[str] = None
    account_id: str = ""
    platform: int = 0
    is_current: bool = False


class SnPresenceActivity(BaseModel):
    id: str = ""
    type: int = 0
    manual_id: Optional[str] = None
    title: Optional[str] = None
    subtitle: Optional[str] = None
    caption: Optional[str] = None
    title_url: Optional[str] = None
    subtitle_url: Optional[str] = None
    small_image: Optional[str] = None
    large_image: Optional[str] = None
    meta: Optional[dict[str, Any]] = None
    lease_minutes: int = 0
    lease_expires_at: Optional[str] = None
    account_id: str = ""
    account: Optional[SnAccount] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None


class SnFriendOverviewItem(BaseModel):
    account: Optional[SnAccount] = None
    status: Optional[SnAccountStatus] = None
    activities: list[SnPresenceActivity] = Field(default_factory=list)


class SnNotableDay(BaseModel):
    date: Optional[str] = None
    local_name: str = ""
    global_name: str = ""
    country_code: Optional[str] = None
    localizable_key: Optional[str] = None
    holidays: list[int] = Field(default_factory=list)


class SnFortuneTip(BaseModel):
    is_positive: bool = False
    title: str = ""
    content: str = ""


class SnCheckInFortuneReport(BaseModel):
    version: int = 0
    poem: str = ""
    summary: str = ""
    summary_detail: Optional[str] = None
    wish: str = ""
    love: str = ""
    study: str = ""
    career: str = ""
    health: str = ""
    lost_item: str = ""
    lucky_color: str = ""
    lucky_direction: str = ""
    lucky_time: str = ""
    lucky_item: str = ""
    lucky_action: str = ""
    avoid_action: str = ""
    ritual: str = ""


class SnCheckInResult(BaseModel):
    id: str = ""
    level: int = 0
    tips: list[SnFortuneTip] = Field(default_factory=list)
    fortune_report: Optional[SnCheckInFortuneReport] = None
    account_id: str = ""
    account: Optional[SnAccount] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None


class SnRecurrencePattern(BaseModel):
    frequency: SnRecurrenceFrequency = SnRecurrenceFrequency.none
    interval: int = 1
    end_date: Optional[str] = None
    occurrences: Optional[int] = None
    days_of_week: Optional[list[str]] = None
    day_of_month: Optional[int] = None
    month_of_year: Optional[int] = None


class SnUserCalendarEvent(BaseModel):
    id: str = ""
    title: str = ""
    description: Optional[str] = None
    location: Optional[str] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    is_all_day: bool = False
    visibility: SnEventVisibility = SnEventVisibility.private
    recurrence: Optional[SnRecurrencePattern] = None
    meta: Optional[dict[str, Any]] = None
    icon: Optional[SnCloudFileReference] = None
    background: Optional[SnCloudFileReference] = None
    account_id: str = ""
    account: Optional[SnAccount] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None


class SnMergedCalendarEvent(BaseModel):
    id: Optional[str] = None
    type: str = ""
    title: str = ""
    description: Optional[str] = None
    location: Optional[str] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    is_all_day: bool = False
    meta: Optional[dict[str, Any]] = None


class SnEventCalendarEntry(BaseModel):
    date: Optional[str] = None
    check_in_result: Optional[SnCheckInResult] = None
    statuses: list[SnAccountStatus] = Field(default_factory=list)
    user_events: list[SnUserCalendarEvent] = Field(default_factory=list)
    notable_days: list[SnNotableDay] = Field(default_factory=list)
    merged_events: Optional[list[SnMergedCalendarEvent]] = None


class SnAccountTimelineItem(BaseModel):
    id: str = ""
    created_at: Optional[str] = None
    event_type: int = 0
    activity: Optional[SnPresenceActivity] = None
    status: Optional[SnAccountStatus] = None


class SnEventCountdownItem(BaseModel):
    event_id: Optional[str] = None
    event_type: int = 0
    title: str = ""
    description: Optional[str] = None
    location: Optional[str] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    is_all_day: bool = False
    days_remaining: int = 0
    hours_remaining: int = 0
    is_ongoing: bool = False
    meta: Optional[dict[str, Any]] = None
    account_id: Optional[str] = None
    background: Optional[SnCloudFileReference] = None
    icon: Optional[SnCloudFileReference] = None

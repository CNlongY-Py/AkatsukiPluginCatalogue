from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, Field

from ..accounts.account import (
    SnAccount,
    SnAccountStatus,
    SnCheckInResult,
    SnCloudFileReference,
    SnEventVisibility,
    SnMergedCalendarEvent,
    SnMergedEventType,
    SnNotableDay,
    SnRecurrenceFrequency,
    SnRecurrencePattern,
    SnUserCalendarEvent,
)


class SnTimelineEvent(BaseModel):
    id: str = ""
    type: str = ""
    resource_identifier: str = ""
    data: Any = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None


class SnEventCalendarEntry(BaseModel):
    date: Optional[str] = None
    check_in_result: Optional[SnCheckInResult] = None
    statuses: list[SnAccountStatus] = Field(default_factory=list)
    user_events: list[SnUserCalendarEvent] = Field(default_factory=list)
    notable_days: list[SnNotableDay] = Field(default_factory=list)
    merged_events: Optional[list[SnMergedCalendarEvent]] = None


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


class SnActivity(BaseModel):
    id: str = ""
    type: str = ""
    resource_identifier: str = ""
    data: Any = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None

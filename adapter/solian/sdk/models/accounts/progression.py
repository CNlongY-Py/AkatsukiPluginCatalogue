from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, Field


class SnProgressBadgeRewardDefinition(BaseModel):
    type: str = ""
    label: Optional[str] = None
    caption: Optional[str] = None
    meta: Optional[dict[str, Any]] = None


class SnProgressRewardDefinition(BaseModel):
    experience: int = 0
    source_points: int = 0
    source_points_currency: str = "points"
    badge: Optional[SnProgressBadgeRewardDefinition] = None


class SnQuestScheduleConfig(BaseModel):
    repeatability: str = "none"
    active_days_of_week: list[int] = Field(default_factory=list)


class SnSeriesStage(BaseModel):
    identifier: str = ""
    title: str = ""
    series_order: int = 0
    target_count: int = 1
    is_completed: bool = False
    completed_at: Optional[str] = None


class SnAchievementState(BaseModel):
    identifier: str = ""
    title: str = ""
    summary: str = ""
    icon: Optional[str] = None
    sort_order: int = 0
    hidden: bool = False
    is_enabled: bool = True
    target_count: int = 1
    progress_count: int = 0
    is_completed: bool = False
    completed_at: Optional[str] = None
    reward: Optional[SnProgressRewardDefinition] = None
    series_identifier: Optional[str] = None
    series_title: Optional[str] = None
    series_order: int = 0
    series_total_steps: int = 0
    series_completed_steps: int = 0
    series_stages: list[SnSeriesStage] = Field(default_factory=list)


class SnQuestState(BaseModel):
    identifier: str = ""
    title: str = ""
    summary: str = ""
    icon: Optional[str] = None
    sort_order: int = 0
    hidden: bool = False
    is_enabled: bool = True
    target_count: int = 1
    progress_count: int = 0
    is_completed: bool = False
    completed_at: Optional[str] = None
    period_key: str = ""
    next_reset_at: Optional[str] = None
    schedule: Optional[SnQuestScheduleConfig] = None
    reward: Optional[SnProgressRewardDefinition] = None
    series_identifier: Optional[str] = None
    series_title: Optional[str] = None
    series_order: int = 0
    series_total_steps: int = 0
    series_completed_steps: int = 0
    series_stages: list[SnSeriesStage] = Field(default_factory=list)


class SnProgressRewardGrant(BaseModel):
    id: str = ""
    account_id: str = ""
    definition_type: str = "achievement"
    definition_identifier: str = ""
    definition_title: str = ""
    reward_token: str = ""
    source_event_id: str = ""
    reward: Optional[SnProgressRewardDefinition] = None
    period_key: Optional[str] = None
    badge_granted_at: Optional[str] = None
    experience_granted_at: Optional[str] = None
    source_points_granted_at: Optional[str] = None
    notification_sent_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None

from __future__ import annotations

from enum import IntEnum
from typing import Optional

from pydantic import BaseModel, Field

from .workout import FitnessVisibility


class FitnessGoalType(IntEnum):
    weight_loss = 0
    weight_gain = 1
    steps = 2
    distance = 3
    duration = 4
    reps = 5
    strength = 6
    cardio = 7
    flexibility = 8
    custom = 9


class FitnessGoalStatus(IntEnum):
    active = 0
    completed = 1
    paused = 2
    cancelled = 3


class RepeatType(IntEnum):
    daily = 0
    weekly = 1
    biweekly = 2
    monthly = 3
    quarterly = 4
    yearly = 5


class SnFitnessGoal(BaseModel):
    id: str = ""
    account_id: str = ""
    goal_type: FitnessGoalType = FitnessGoalType.custom
    title: str = ""
    description: Optional[str] = None
    target_value: Optional[float] = None
    current_value: Optional[float] = None
    unit: Optional[str] = None
    bound_workout_type: Optional[int] = None
    bound_metric_type: Optional[int] = None
    auto_update_progress: bool = True
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    status: FitnessGoalStatus = FitnessGoalStatus.active
    notes: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    repeat_type: Optional[RepeatType] = None
    repeat_interval: Optional[int] = None
    repeat_count: Optional[int] = None
    current_repetition: Optional[int] = None
    parent_goal_id: Optional[str] = None
    visibility: FitnessVisibility = FitnessVisibility.private


class GoalStats(BaseModel):
    active_count: int = 0
    completed_count: int = 0


class CreateGoalRequest(BaseModel):
    title: str = ""
    goal_type: FitnessGoalType = FitnessGoalType.custom
    start_date: Optional[str] = None
    description: Optional[str] = None
    target_value: Optional[float] = None
    unit: Optional[str] = None
    bound_workout_type: Optional[int] = None
    bound_metric_type: Optional[int] = None
    auto_update_progress: bool = True
    end_date: Optional[str] = None
    notes: Optional[str] = None
    repeat_type: Optional[RepeatType] = None
    repeat_interval: Optional[int] = None
    repeat_count: Optional[int] = None
    visibility: FitnessVisibility = FitnessVisibility.private


class UpdateGoalRequest(BaseModel):
    title: str = ""
    goal_type: FitnessGoalType = FitnessGoalType.custom
    start_date: Optional[str] = None
    status: FitnessGoalStatus = FitnessGoalStatus.active
    description: Optional[str] = None
    target_value: Optional[float] = None
    current_value: Optional[float] = None
    unit: Optional[str] = None
    bound_workout_type: Optional[int] = None
    bound_metric_type: Optional[int] = None
    auto_update_progress: Optional[bool] = None
    end_date: Optional[str] = None
    notes: Optional[str] = None
    visibility: Optional[FitnessVisibility] = None


class UpdateProgressRequest(BaseModel):
    current_value: float = 0.0


class UpdateGoalStatusRequest(BaseModel):
    status: FitnessGoalStatus = FitnessGoalStatus.active

from __future__ import annotations

from enum import IntEnum
from typing import Optional

from pydantic import BaseModel, Field

from .workout import FitnessVisibility


class FitnessMetricType(IntEnum):
    weight = 0
    body_fat = 1
    steps = 2
    heart_rate = 3
    sleep = 4
    calories = 5
    water_intake = 6
    distance = 9
    custom = 10


class SnFitnessMetric(BaseModel):
    id: str = ""
    account_id: str = ""
    metric_type: FitnessMetricType = FitnessMetricType.custom
    value: float = 0.0
    unit: str = ""
    recorded_at: Optional[str] = None
    notes: Optional[str] = None
    source: Optional[str] = None
    visibility: FitnessVisibility = FitnessVisibility.private
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


class CreateMetricRequest(BaseModel):
    metric_type: FitnessMetricType = FitnessMetricType.custom
    value: float = 0.0
    unit: str = ""
    recorded_at: Optional[str] = None
    notes: Optional[str] = None
    source: Optional[str] = None
    external_id: Optional[str] = None
    visibility: FitnessVisibility = FitnessVisibility.private


class UpdateMetricRequest(BaseModel):
    metric_type: FitnessMetricType = FitnessMetricType.custom
    value: float = 0.0
    unit: str = ""
    recorded_at: Optional[str] = None
    notes: Optional[str] = None
    source: Optional[str] = None
    visibility: Optional[FitnessVisibility] = None


class CreateMetricsBatchRequest(BaseModel):
    metrics: list[CreateMetricRequest] = Field(default_factory=list)

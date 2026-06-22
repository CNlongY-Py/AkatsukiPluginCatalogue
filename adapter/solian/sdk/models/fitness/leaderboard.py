from __future__ import annotations

from enum import IntEnum
from typing import Optional

from pydantic import BaseModel, Field

from ..accounts.account import SnAccount


class LeaderboardType(IntEnum):
    calories = 0
    workouts = 1
    goals = 2


class LeaderboardPeriod(IntEnum):
    daily = 0
    weekly = 1
    monthly = 2
    all_time = 3


class LeaderboardEntry(BaseModel):
    rank: int = 0
    account_id: str = ""
    value: float = 0.0
    account: Optional[SnAccount] = None


class LeaderboardResponse(BaseModel):
    entries: list[LeaderboardEntry] = Field(default_factory=list)
    user_entry: Optional[LeaderboardEntry] = None
    total_count: int = 0

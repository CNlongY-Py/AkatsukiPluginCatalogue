from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class SnHeatmapItem(BaseModel):
    date: Optional[str] = None
    count: int = 0


class SnHeatmap(BaseModel):
    unit: str = ""
    period_start: Optional[str] = None
    period_end: Optional[str] = None
    items: list[SnHeatmapItem] = Field(default_factory=list)

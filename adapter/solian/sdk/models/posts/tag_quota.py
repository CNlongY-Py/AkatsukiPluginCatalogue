from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class SnProtectedTagRecord(BaseModel):
    id: str = ""
    slug: str = ""
    name: Optional[str] = None


class SnTagQuota(BaseModel):
    total: int = 0
    used: int = 0
    remaining: int = 0
    level: int = 0
    perk_level: int = 0
    records: list[SnProtectedTagRecord] = Field(default_factory=list)

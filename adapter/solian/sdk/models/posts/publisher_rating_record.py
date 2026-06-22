from __future__ import annotations

from enum import IntEnum
from typing import Optional

from pydantic import BaseModel


class SnPublisherRatingStatus(IntEnum):
    active = 0
    expired = 1


class SnPublisherRatingRecord(BaseModel):
    id: str = ""
    reason_type: str = ""
    reason: str = ""
    delta: float = 0.0
    status: SnPublisherRatingStatus = SnPublisherRatingStatus.active
    expired_at: Optional[str] = None
    publisher_id: str = ""
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None

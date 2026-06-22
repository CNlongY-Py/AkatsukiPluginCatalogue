from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

from ..drive.file import SnCloudFileReference


class SnPublisherLeaderboardEntry(BaseModel):
    publisher_id: str = ""
    name: str = ""
    nick: str = ""
    picture: Optional[SnCloudFileReference] = None
    rating: float = 0.0
    rank: int = 0
    percentile: float = 0.0
    grade: str = ""

from __future__ import annotations

from datetime import datetime
from typing import Optional


def datetime_to_iso(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%S.") + f"{dt.microsecond:06d}".rstrip("0").rstrip(".") + "Z"


def parse_datetime(value: Optional[str]) -> Optional[datetime]:
    if value is None:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00"))

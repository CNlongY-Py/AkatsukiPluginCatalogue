from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, Field

from ..auth.misc import GeoIpLocation


class SnActionLog(BaseModel):
    id: str = ""
    action: str = ""
    meta: dict[str, Any] = Field(default_factory=dict)
    user_agent: Optional[str] = None
    ip_address: Optional[str] = None
    location: Optional[GeoIpLocation] = None
    account_id: str = ""
    session_id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None

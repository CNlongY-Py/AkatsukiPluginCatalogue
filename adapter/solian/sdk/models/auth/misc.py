from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, Field


class GeoIpLocation(BaseModel):
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    country_code: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None


class AppToken(BaseModel):
    token: str = ""


class SnAuthFactor(BaseModel):
    id: str = ""
    type: int = 0
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    expired_at: Optional[str] = None
    enabled_at: Optional[str] = None
    trustworthy: int = 0
    created_response: Optional[dict[str, Any]] = None

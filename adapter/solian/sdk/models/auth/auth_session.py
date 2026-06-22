from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, Field

from .misc import GeoIpLocation


class SnAccountConnection(BaseModel):
    id: str = ""
    account_id: str = ""
    provider: str = ""
    provided_identifier: str = ""
    meta: dict[str, Any] = Field(default_factory=dict)
    last_used_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None


class SnAuthSession(BaseModel):
    id: str = ""
    label: Optional[str] = None
    last_granted_at: Optional[str] = None
    expired_at: Optional[str] = None
    audiences: list[str] = Field(default_factory=list)
    scopes: list[str] = Field(default_factory=list)
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    location: Optional[GeoIpLocation] = None
    type: int = 0
    account_id: str = ""
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    is_current: bool = False
    children_count: Optional[int] = None


class SnAuthDeviceWithSession(BaseModel):
    id: str = ""
    device_id: str = ""
    device_name: str = ""
    device_label: Optional[str] = None
    account_id: str = ""
    platform: int = 0
    sessions: list[SnAuthSession] = Field(default_factory=list)
    is_current: bool = False

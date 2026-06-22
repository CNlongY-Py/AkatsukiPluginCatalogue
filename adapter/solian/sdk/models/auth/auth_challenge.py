from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, Field


class SnAuthChallenge(BaseModel):
    id: str = ""
    expired_at: Optional[str] = None
    step_remain: int = 0
    step_total: int = 0
    failed_attempts: int = 0
    blacklist_factors: list[str] = Field(default_factory=list)
    audiences: list[Any] = Field(default_factory=list)
    scopes: list[Any] = Field(default_factory=list)
    ip_address: str = ""
    user_agent: str = ""
    nonce: Optional[str] = None
    country_code: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    device_id: Optional[str] = None
    device_name: Optional[str] = None
    platform: Optional[int] = None
    approved_at: Optional[str] = None
    declined_at: Optional[str] = None
    approved_by_session_id: Optional[str] = None
    account_id: str = ""
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None

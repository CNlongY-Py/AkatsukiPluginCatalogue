from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

from .account import SnAccount


class SnRelationship(BaseModel):
    account_id: str = ""
    account: Optional[SnAccount] = None
    related_id: str = ""
    related: Optional[SnAccount] = None
    status: int = 0
    alias: Optional[str] = None
    degrade_to_status: Optional[int] = None
    expired_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class SnAbuseReport(BaseModel):
    id: str = ""
    resource_identifier: str = ""
    type: int = 0
    reason: str = ""
    resolved_at: Optional[str] = None
    resolution: Optional[str] = None
    account_id: str = ""
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None

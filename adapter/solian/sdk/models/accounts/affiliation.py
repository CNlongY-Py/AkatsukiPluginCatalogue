from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, Field


class SnAffiliationSpell(BaseModel):
    id: str = ""
    spell: str = ""
    type: int = 0
    expires_at: Optional[str] = None
    affected_at: Optional[str] = None
    meta: dict[str, Any] = Field(default_factory=dict)
    account_id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None


class SnAffiliationResult(BaseModel):
    id: str = ""
    resource_identifier: str = ""
    spell_id: str = ""
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None

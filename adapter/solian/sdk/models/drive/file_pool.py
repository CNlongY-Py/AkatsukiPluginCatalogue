from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel


class SnFilePool(BaseModel):
    id: str = ""
    name: str = ""
    description: Optional[str] = None
    storage_config: Optional[dict[str, Any]] = None
    billing_config: Optional[dict[str, Any]] = None
    policy_config: Optional[dict[str, Any]] = None
    is_hidden: Optional[bool] = None
    account_id: Optional[str] = None
    resource_identifier: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None

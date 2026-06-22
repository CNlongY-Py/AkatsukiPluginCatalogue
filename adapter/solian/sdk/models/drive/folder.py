from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class SnCloudFolder(BaseModel):
    id: str = ""
    name: str = ""
    parent_folder_id: Optional[str] = None
    account_id: str = ""
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

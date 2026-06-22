from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class SnFilePermissionStatus(BaseModel):
    readable: bool = False
    writable: bool = False
    manageable: bool = False
    visibility: str = ""
    inherited_from: Optional[str] = None


class SnFilePermission(BaseModel):
    id: Optional[str] = None
    file_id: str = ""
    subject_type: str = ""
    subject_id: str = ""
    permission: str = ""
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None

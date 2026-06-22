from __future__ import annotations

from enum import IntEnum
from typing import Any, Optional

from pydantic import BaseModel, Field


class UniversalFileType(IntEnum):
    image = 0
    video = 1
    audio = 2
    file = 3


class SnCloudFileObject(BaseModel):
    id: str = ""
    size: int = 0
    meta: Optional[dict[str, Any]] = None
    mime_type: Optional[str] = None
    hash: Optional[str] = None
    has_compression: bool = False
    has_thumbnail: bool = False
    file_replicas: list[SnFileReplica] = Field(default_factory=list)
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None


class SnFileReplica(BaseModel):
    id: str = ""
    object_id: str = ""
    pool_id: str = ""
    pool: Optional[SnFilePool] = None
    storage_id: str = ""
    status: int = 0
    is_primary: bool = False
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None


class SnCloudFileReference(BaseModel):
    id: str = ""
    name: str = ""
    file_meta: dict[str, Any] = Field(default_factory=dict)
    user_meta: dict[str, Any] = Field(default_factory=dict)
    sensitive_marks: list[int] = Field(default_factory=list)
    mime_type: str = ""
    hash: str = ""
    size: int = 0
    has_compression: bool = False
    storage_url: Optional[str] = None
    width: Optional[float] = None
    height: Optional[float] = None
    blur: Optional[str] = None
    usage: Optional[str] = None
    application_type: Optional[str] = None


class SnCloudFile(BaseModel):
    id: str = ""
    account_id: str = ""
    description: Optional[str] = None
    indexed: bool = False
    is_folder: bool = False
    is_marked_recycle: bool = False
    name: str = ""
    object: Optional[SnCloudFileObject] = None
    object_id: Optional[str] = None
    parent_id: Optional[str] = None
    resource_identifier: str = ""
    storage_id: Optional[str] = None
    storage_url: Optional[str] = None
    mime_type: str = ""
    application_type: Optional[str] = None
    usage: Optional[str] = None
    sensitive_marks: list[int] = Field(default_factory=list)
    file_meta: dict[str, Any] = Field(default_factory=dict)
    user_meta: dict[str, Any] = Field(default_factory=dict)
    children: list[SnCloudFile] = Field(default_factory=list)
    children_count: int = 0
    permission_status: Optional[SnFilePermissionStatus] = None
    uploaded_at: Optional[str] = None
    expired_at: Optional[str] = None
    updated_at: Optional[str] = None
    created_at: Optional[str] = None
    deleted_at: Optional[str] = None


class UniversalFile(BaseModel):
    data: Any = None
    type: UniversalFileType = UniversalFileType.file
    is_link: bool = False
    display_name: Optional[str] = None

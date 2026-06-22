from __future__ import annotations

from enum import IntEnum
from typing import Optional

from pydantic import BaseModel, Field

from .file import SnCloudFileReference


class DriveTaskStatus(IntEnum):
    pending = 0
    in_progress = 1
    paused = 2
    completed = 3
    failed = 4
    expired = 5
    cancelled = 6


class DriveTask(BaseModel):
    id: str = ""
    task_id: str = ""
    file_name: str = ""
    content_type: str = ""
    file_size: int = 0
    uploaded_bytes: int = 0
    total_chunks: int = 0
    uploaded_chunks: int = 0
    status: DriveTaskStatus = DriveTaskStatus.pending
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    type: str = ""
    transmission_progress: Optional[float] = None
    error_message: Optional[str] = None
    status_message: Optional[str] = None
    result: Optional[SnCloudFileReference] = None
    pool_id: Optional[str] = None
    bundle_id: Optional[str] = None
    encrypt_password: Optional[str] = None
    expired_at: Optional[str] = None

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

from ..drive.file import SnCloudFileReference
from .publisher import SnPublisher


class SnPostCollection(BaseModel):
    id: str = ""
    slug: str = ""
    name: Optional[str] = None
    description: Optional[str] = None
    publisher_id: str = ""
    publisher: Optional[SnPublisher] = None
    background: Optional[SnCloudFileReference] = None
    icon: Optional[SnCloudFileReference] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

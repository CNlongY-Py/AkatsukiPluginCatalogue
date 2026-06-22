from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, Field


class SnPostTag(BaseModel):
    id: str = ""
    slug: str = ""
    name: Optional[str] = None
    description: Optional[str] = None
    owner_publisher_id: Optional[str] = None
    is_protected: bool = False
    is_event: bool = False
    event_ends_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    posts: list[Any] = Field(default_factory=list)
    usage: int = 0

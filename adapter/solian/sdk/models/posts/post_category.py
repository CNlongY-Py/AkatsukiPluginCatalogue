from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, Field

from .post_tag import SnPostTag


class SnPostCategory(BaseModel):
    id: str = ""
    slug: str = ""
    name: Optional[str] = None
    posts: list[Any] = Field(default_factory=list)
    usage: int = 0


class SnCategorySubscription(BaseModel):
    id: str = ""
    account_id: str = ""
    category_id: Optional[str] = None
    category: Optional[SnPostCategory] = None
    tag_id: Optional[str] = None
    tag: Optional[SnPostTag] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None

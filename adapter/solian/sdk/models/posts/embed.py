from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class SnScrappedLink(BaseModel):
    type: str = ""
    url: str = ""
    title: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
    favicon_url: Optional[str] = None
    site_name: Optional[str] = None
    content_type: Optional[str] = None
    author: Optional[str] = None
    published_date: Optional[str] = None

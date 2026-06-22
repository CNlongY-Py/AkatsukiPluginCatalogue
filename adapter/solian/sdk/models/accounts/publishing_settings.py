from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class SnPublishingSettings(BaseModel):
    id: str = ""
    account_id: str = ""
    default_posting_publisher_id: Optional[str] = None
    default_reply_publisher_id: Optional[str] = None
    default_fediverse_publisher_id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

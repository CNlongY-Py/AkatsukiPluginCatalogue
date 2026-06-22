from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from .account import SnAccount
from ..drive.file import SnCloudFileReference


class SnTicket(BaseModel):
    id: str = ""
    title: str = ""
    content: Optional[str] = None
    type: int = 0
    status: int = 0
    priority: int = 0
    creator_id: str = ""
    creator: Optional[SnAccount] = None
    assignee_id: Optional[str] = None
    assignee: Optional[SnAccount] = None
    resolved_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    messages: list[SnTicketMessage] = Field(default_factory=list)
    file_ids: list[str] = Field(default_factory=list)
    resources: list[Optional[str]] = Field(default_factory=list)


class SnTicketMessage(BaseModel):
    id: str = ""
    ticket_id: str = ""
    sender_id: str = ""
    sender: Optional[SnAccount] = None
    content: str = ""
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    files: list[SnCloudFileReference] = Field(default_factory=list)

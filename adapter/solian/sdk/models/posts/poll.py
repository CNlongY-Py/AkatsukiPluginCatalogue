from __future__ import annotations

from enum import IntEnum
from typing import Any, Optional

from pydantic import BaseModel, Field

from ..accounts.account import SnAccount
from .publisher import SnPublisher


class SnPollQuestionType(IntEnum):
    single_choice = 0
    multiple_choice = 1
    yes_no = 2
    rating = 3
    free_text = 4


class SnPollOption(BaseModel):
    id: str = ""
    label: str = ""
    description: Optional[str] = None
    order: int = 0


class SnPollQuestion(BaseModel):
    id: str = ""
    type: SnPollQuestionType = SnPollQuestionType.single_choice
    options: Optional[list[SnPollOption]] = None
    title: str = ""
    description: Optional[str] = None
    order: int = 0
    is_required: bool = False


class SnPoll(BaseModel):
    id: str = ""
    questions: list[SnPollQuestion] = Field(default_factory=list)
    title: Optional[str] = None
    description: Optional[str] = None
    ended_at: Optional[str] = None
    publisher_id: str = ""
    publisher: Optional[SnPublisher] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None


class SnPollWithStats(BaseModel):
    user_answer: Optional[SnPollAnswer] = None
    stats: dict[str, Any] = Field(default_factory=dict)
    id: str = ""
    questions: list[SnPollQuestion] = Field(default_factory=list)
    title: Optional[str] = None
    description: Optional[str] = None
    ended_at: Optional[str] = None
    publisher_id: str = ""
    publisher: Optional[SnPublisher] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None


class SnPollAnswer(BaseModel):
    id: str = ""
    answer: dict[str, Any] = Field(default_factory=dict)
    account_id: str = ""
    poll_id: str = ""
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    account: Optional[SnAccount] = None

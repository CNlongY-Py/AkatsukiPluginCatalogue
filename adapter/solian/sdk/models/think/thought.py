from __future__ import annotations

from enum import IntEnum
from typing import Any, Optional

from pydantic import BaseModel, Field

from ..drive.file import SnCloudFileReference


class ThinkingThoughtRole(IntEnum):
    assistant = 0
    user = 1
    system = 2


class ThinkingMessagePartType(IntEnum):
    text = 0
    function_call = 1
    function_result = 2
    reasoning = 3


class SnFunctionCall(BaseModel):
    id: str = ""
    name: str = ""
    arguments: str = ""


class SnFunctionResult(BaseModel):
    call_id: str = ""
    result: Any = None
    is_error: bool = False


class SnThinkingMessagePart(BaseModel):
    type: ThinkingMessagePartType = ThinkingMessagePartType.text
    text: Optional[str] = None
    reasoning: Optional[str] = None
    metadata: Optional[dict[str, Any]] = None
    files: Optional[list[SnCloudFileReference]] = None
    function_call: Optional[SnFunctionCall] = None
    function_result: Optional[SnFunctionResult] = None


class SnThinkingSequence(BaseModel):
    id: str = ""
    topic: Optional[str] = None
    total_token: int = 0
    paid_token: int = 0
    account_id: str = ""
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    agent_initiated: bool = False
    user_last_read_at: Optional[str] = None
    last_message_at: Optional[str] = None
    is_public: bool = False
    bot_name: Optional[str] = None


class SnThinkingThought(BaseModel):
    id: str = ""
    parts: list[SnThinkingMessagePart] = Field(default_factory=list)
    role: ThinkingThoughtRole = ThinkingThoughtRole.user
    token_count: Optional[int] = None
    model_name: Optional[str] = None
    bot_name: Optional[str] = None
    sequence_id: str = ""
    sequence: Optional[SnThinkingSequence] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    is_archived: bool = False


class ThoughtServiceModel(BaseModel):
    id: str = ""
    display_name: str = ""
    min_perk_level: int = 0
    is_default: bool = False


class ThoughtService(BaseModel):
    id: str = ""
    name: str = ""
    description: str = ""
    available_models: list[ThoughtServiceModel] = Field(default_factory=list)


class ThoughtServicesResponse(BaseModel):
    default_bot: str = ""
    services: list[ThoughtService] = Field(default_factory=list)


class PersonalityConversation(BaseModel):
    id: str = ""
    account_id: str = ""
    agent_id: str = ""
    title: str = ""
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


class PersonalityMessage(BaseModel):
    id: str = ""
    thread_id: str = ""
    role: str = ""
    content: str = ""
    sequence: int = 0
    created_at: Optional[str] = None


class PersonalityRun(BaseModel):
    id: str = ""
    status: str = ""
    model: Optional[str] = None


class PersonalityRunResponse(BaseModel):
    thread: Optional[PersonalityConversation] = None
    run: Optional[PersonalityRun] = None
    request_message: Optional[PersonalityMessage] = None
    response_message: Optional[PersonalityMessage] = None
    content: str = ""

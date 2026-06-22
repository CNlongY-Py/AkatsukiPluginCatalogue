from __future__ import annotations

from enum import IntEnum
from typing import Optional

from pydantic import BaseModel, Field

from .account import SnAccount


class PunishmentType(IntEnum):
    permission_modification = 0
    block_login = 1
    disable_account = 2
    strike = 3


class SnAccountPunishment(BaseModel):
    id: str = ""
    reason: str = ""
    expired_at: Optional[str] = None
    type: PunishmentType = PunishmentType.permission_modification
    blocked_permissions: Optional[list[str]] = None
    account_id: str = ""
    account: Optional[SnAccount] = None
    creator_id: Optional[str] = None
    creator: Optional[SnAccount] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None

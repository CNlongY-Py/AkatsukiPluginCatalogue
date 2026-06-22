from __future__ import annotations

from pydantic import BaseModel


class SnFortuneSaying(BaseModel):
    content: str = ""
    source: str = ""
    language: str = ""

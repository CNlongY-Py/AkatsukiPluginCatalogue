from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, Field


class SnDiscoveryInterest(BaseModel):
    kind: str = ""
    reference_id: str = ""
    label: str = ""
    score: float = 0.0
    interaction_count: int = 0
    last_interacted_at: Optional[str] = None
    last_signal_type: str = ""


class SnSuggestedData(BaseModel):
    kind: int = 0
    reference_id: str = ""
    label: str = ""
    score: float = 0.0
    reasons: list[str] = Field(default_factory=list)
    data: Any = None


class SnDiscoveryProfile(BaseModel):
    generated_at: Optional[str] = None
    interests: list[SnDiscoveryInterest] = Field(default_factory=list)
    suggested_publishers: list[SnSuggestedData] = Field(default_factory=list)
    suggested_accounts: list[SnSuggestedData] = Field(default_factory=list)
    suggested_realms: list[SnSuggestedData] = Field(default_factory=list)
    suppressed: list[Any] = Field(default_factory=list)


class SnFediversePublisherAvailability(BaseModel):
    publisher_id: str = ""
    publisher_name: str = ""
    fediverse_handle: str = ""
    fediverse_uri: str = ""
    avatar_url: Optional[str] = None
    is_enabled: bool = False
    followers_count: int = 0
    following_count: int = 0
    posts_count: int = 0


class SnFediverseAvailabilityResponse(BaseModel):
    is_enabled: bool = False
    publishers: list[SnFediversePublisherAvailability] = Field(default_factory=list)

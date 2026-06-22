from dataclasses import dataclass, field
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class PaginationState(Generic[T]):
    items: list[T] = field(default_factory=list)
    is_loading: bool = False
    is_reloading: bool = False
    total_count: int | None = None
    has_more: bool = True
    cursor: str | None = None

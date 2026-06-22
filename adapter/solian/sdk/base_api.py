from __future__ import annotations

from typing import Any, Generic, TypeVar

from httpx import Client, Response

T = TypeVar("T")


class PaginatedResult(Generic[T]):
    def __init__(
        self,
        items: list[T],
        total_count: int = 0,
        has_more: bool = True,
        cursor: str | None = None,
    ):
        self.items = items
        self.total_count = total_count
        self.has_more = has_more
        self.cursor = cursor


class BaseApi:
    def __init__(self, client: Client):
        self._client = client

    def _get(
        self,
        path: str,
        params: dict[str, Any] | None = None,
        **kwargs,
    ) -> Response:
        return self._client.get(path, params=params, **kwargs)

    def _post(
        self,
        path: str,
        json: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        **kwargs,
    ) -> Response:
        return self._client.post(path, json=json, params=params, **kwargs)

    def _put(
        self,
        path: str,
        json: dict[str, Any] | None = None,
        **kwargs,
    ) -> Response:
        return self._client.put(path, json=json, **kwargs)

    def _patch(
        self,
        path: str,
        json: dict[str, Any] | None = None,
        **kwargs,
    ) -> Response:
        return self._client.patch(path, json=json, **kwargs)

    def _delete(
        self,
        path: str,
        json: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        **kwargs,
    ) -> Response:
        return self._client.delete(path, json=json, params=params, **kwargs)

    def _parse_list(
        self, response: Response, from_json: type[T]
    ) -> list[T]:
        data = response.json()
        if not isinstance(data, list):
            return []
        return [from_json(**item) for item in data]

    def _parse_item(self, response: Response, from_json: type[T]) -> T:
        return from_json(**response.json())

    def _get_total_count(self, response: Response) -> int:
        val = response.headers.get("X-Total", "0")
        try:
            return int(val)
        except (ValueError, TypeError):
            return 0

    def _clean_none(self, data: dict[str, Any]) -> dict[str, Any]:
        return {k: v for k, v in data.items() if v is not None}

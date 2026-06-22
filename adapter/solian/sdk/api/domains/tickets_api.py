from typing import Any

from ...base_api import BaseApi, PaginatedResult


class TicketsApi(BaseApi):
    _base_path = '/passport'

    def get_tickets(self, status: int | None = None, offset: int = 0, take: int = 20, mime: bool = False) -> PaginatedResult[dict[str, Any]]:
        path = f'{self._base_path}/tickets/me' if mime else f'{self._base_path}/tickets'
        params = self._clean_none({'status': status, 'offset': offset, 'take': take})
        response = self._get(path, params=params)
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_ticket(self, ticket_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/tickets/{ticket_id}')
        return response.json()

    def create_ticket(self, title: str, type: int, content: str | None = None, priority: int | None = None, file_ids: list[str] | None = None, resources: list[str | None] | None = None) -> dict[str, Any]:
        data = self._clean_none({'title': title, 'content': content, 'type': type, 'priority': priority, 'file_ids': file_ids, 'resources': resources})
        response = self._post(f'{self._base_path}/tickets', json=data)
        return response.json()

    def update_ticket(self, ticket_id: str, title: str | None = None, content: str | None = None, type: int | None = None, priority: int | None = None, resources: list[str | None] | None = None) -> dict[str, Any]:
        data = self._clean_none({'title': title, 'content': content, 'type': type, 'priority': priority, 'resources': resources})
        response = self._put(f'{self._base_path}/tickets/{ticket_id}', json=data)
        return response.json()

    def close_ticket(self, ticket_id: str) -> None:
        self._post(f'{self._base_path}/tickets/{ticket_id}/close')

    def reopen_ticket(self, ticket_id: str) -> None:
        self._post(f'{self._base_path}/tickets/{ticket_id}/reopen')

    def delete_ticket(self, ticket_id: str) -> None:
        self._delete(f'{self._base_path}/tickets/{ticket_id}')

    def get_ticket_messages(self, ticket_id: str, offset: int = 0, take: int = 50) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/tickets/{ticket_id}/messages', params={'offset': offset, 'take': take})
        return response.json()

    def add_ticket_message(self, ticket_id: str, content: str, file_ids: list[str] | None = None) -> dict[str, Any]:
        data = self._clean_none({'content': content, 'file_ids': file_ids})
        response = self._post(f'{self._base_path}/tickets/{ticket_id}/messages', json=data)
        return response.json()

    def update_ticket_message(self, ticket_id: str, message_id: str, message: str) -> dict[str, Any]:
        response = self._patch(f'{self._base_path}/tickets/{ticket_id}/messages/{message_id}', json={'message': message})
        return response.json()

    def delete_ticket_message(self, ticket_id: str, message_id: str) -> None:
        self._delete(f'{self._base_path}/tickets/{ticket_id}/messages/{message_id}')

    def update_ticket_status(self, ticket_id: str, status: int) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/tickets/{ticket_id}/status', json={'status': status})
        return response.json()

    def assign_ticket(self, ticket_id: str, assignee_id: str | None = None) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/tickets/{ticket_id}/assign', json={'assignee_id': assignee_id})
        return response.json()

    def get_ticket_count(self, status: int | None = None) -> int:
        params = self._clean_none({'status': status})
        response = self._get(f'{self._base_path}/tickets/count', params=params)
        data = response.json()
        return int(data.get('count', 0))

from typing import Any

from ...base_api import BaseApi, PaginatedResult


class ChatApi(BaseApi):
    _base_path = '/messager'

    def get_rooms(self, offset: int = 0, take: int = 20) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/chat/rooms', params={'offset': offset, 'take': take})
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_room(self, room_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/chat/rooms/{room_id}')
        return response.json()

    def create_room(self, name: str, type: str, member_ids: list[str] | None = None) -> dict[str, Any]:
        data = self._clean_none({'name': name, 'type': type, 'member_ids': member_ids})
        response = self._post(f'{self._base_path}/chat/rooms', json=data)
        return response.json()

    def update_room(self, room_id: str, data: dict[str, Any]) -> dict[str, Any]:
        response = self._patch(f'{self._base_path}/chat/rooms/{room_id}', json=data)
        return response.json()

    def delete_room(self, room_id: str) -> None:
        self._delete(f'{self._base_path}/chat/rooms/{room_id}')

    def get_chat_summary(self) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/chat/summary')
        return response.json()

    def get_messages(self, room_id: str, offset: int = 0, take: int = 50) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/chat/rooms/{room_id}/messages', params={'offset': offset, 'take': take})
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def send_message(self, room_id: str, content: str, attachments: list[dict[str, Any]] | None = None) -> dict[str, Any]:
        data = self._clean_none({'content': content, 'attachments': attachments})
        response = self._post(f'{self._base_path}/chat/rooms/{room_id}/messages', json=data)
        return response.json()

    def edit_message(self, room_id: str, message_id: str, content: str) -> dict[str, Any]:
        response = self._patch(f'{self._base_path}/chat/rooms/{room_id}/messages/{message_id}', json={'content': content})
        return response.json()

    def delete_message(self, room_id: str, message_id: str) -> None:
        self._delete(f'{self._base_path}/chat/rooms/{room_id}/messages/{message_id}')

    def create_placeholder(self, room_id: str, kind: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/chat/rooms/{room_id}/messages/placeholder', json={'kind': kind})
        return response.json()

    def mark_as_read(self, room_id: str, message_id: str) -> None:
        self._post(f'{self._base_path}/chat/rooms/{room_id}/read', json={'message_id': message_id})

    def redirect_messages(self, room_id: str, message_ids: list[str]) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/chat/{room_id}/messages/redirect', json={'message_ids': message_ids})
        return response.json()

    def get_members(self, room_id: str, offset: int = 0, take: int = 50) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/chat/rooms/{room_id}/members', params={'offset': offset, 'take': take})
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def add_member(self, room_id: str, account_id: str) -> None:
        self._post(f'{self._base_path}/chat/rooms/{room_id}/members', json={'account_id': account_id})

    def remove_member(self, room_id: str, account_id: str) -> None:
        self._delete(f'{self._base_path}/chat/rooms/{room_id}/members/{account_id}')

    def leave_room(self, room_id: str) -> None:
        self._delete(f'{self._base_path}/chat/rooms/{room_id}/members/me')

    def promote_to_admin(self, room_id: str, account_id: str) -> None:
        self._post(f'{self._base_path}/chat/rooms/{room_id}/members/{account_id}/admin')

    def demote_from_admin(self, room_id: str, account_id: str) -> None:
        self._delete(f'{self._base_path}/chat/rooms/{room_id}/members/{account_id}/admin')

    def add_reaction(self, room_id: str, message_id: str, reaction_type: str) -> None:
        self._post(f'{self._base_path}/chat/rooms/{room_id}/messages/{message_id}/reactions', json={'type': reaction_type})

    def remove_reaction(self, room_id: str, message_id: str) -> None:
        self._delete(f'{self._base_path}/chat/rooms/{room_id}/messages/{message_id}/reactions')

    def get_direct_chat(self, account_id: str) -> dict[str, Any] | None:
        try:
            response = self._get(f'{self._base_path}/chat/direct/{account_id}')
            return response.json()
        except Exception:
            return None

    def create_direct_chat(self, account_id: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/chat/direct', json={'related_user_id': account_id})
        return response.json()

    def get_or_create_direct_chat(self, account_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/chat/direct/{account_id}')
        return response.json()

    def get_online_status(self, account_ids: list[str]) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/chat/online', params={'account_ids': ','.join(account_ids)})
        return response.json()

    def update_online_status(self, status: str) -> None:
        self._post(f'{self._base_path}/chat/online', json={'status': status})

    def get_realm_chat_rooms(self, realm_slug: str) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/realms/{realm_slug}/chat')
        return response.json()

    def get_groups(self) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/chat/groups')
        return response.json()

    def create_group(self, name: str, color: str | None = None, icon: str | None = None, order: int | None = None) -> dict[str, Any]:
        data = self._clean_none({'name': name, 'color': color, 'icon': icon, 'order': order})
        response = self._post(f'{self._base_path}/chat/groups', json=data)
        return response.json()

    def update_group(self, group_id: str, name: str | None = None, color: str | None = None, icon: str | None = None, order: int | None = None) -> dict[str, Any]:
        data = self._clean_none({'name': name, 'color': color, 'icon': icon, 'order': order})
        response = self._patch(f'{self._base_path}/chat/groups/{group_id}', json=data)
        return response.json()

    def delete_group(self, group_id: str) -> None:
        self._delete(f'{self._base_path}/chat/groups/{group_id}')

    def move_room_to_group(self, room_id: str, group_id: str | None = None) -> None:
        self._patch(f'{self._base_path}/chat/rooms/{room_id}/group', json={'group_id': group_id})

    def initiate_call(self, room_id: str, type: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/chat/rooms/{room_id}/calls', json={'type': type})
        return response.json()

    def join_call(self, room_id: str, call_id: str) -> None:
        self._post(f'{self._base_path}/chat/rooms/{room_id}/calls/{call_id}/join')

    def leave_call(self, room_id: str, call_id: str) -> None:
        self._post(f'{self._base_path}/chat/rooms/{room_id}/calls/{call_id}/leave')

    def end_call(self, room_id: str, call_id: str) -> None:
        self._delete(f'{self._base_path}/chat/rooms/{room_id}/calls/{call_id}')

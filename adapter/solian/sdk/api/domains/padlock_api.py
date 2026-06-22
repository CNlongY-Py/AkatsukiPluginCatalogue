from typing import Any

from ...base_api import BaseApi, PaginatedResult


class PadlockApi(BaseApi):
    _base_path = '/padlock'

    def get_action_logs(self, offset: int = 0, take: int = 20, action: str | None = None) -> PaginatedResult[dict[str, Any]]:
        params = self._clean_none({'offset': offset, 'take': take, 'action': action})
        response = self._get(f'{self._base_path}/actions', params=params)
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_sessions(self, offset: int = 0, take: int = 20, type: int | None = None, client_id: str | None = None, include_children: bool | None = None) -> PaginatedResult[dict[str, Any]]:
        params = self._clean_none({'offset': offset, 'take': take, 'type': type, 'clientId': client_id, 'includeChildren': include_children})
        response = self._get(f'{self._base_path}/sessions', params=params)
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_session_children(self, session_id: str, offset: int = 0, take: int = 20) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/sessions/{session_id}/children', params={'offset': offset, 'take': take})
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def revoke_session(self, session_id: str) -> None:
        self._delete(f'{self._base_path}/sessions/{session_id}')

    def revoke_all_other_sessions(self) -> None:
        self._delete(f'{self._base_path}/sessions/other')

    def get_devices(self, offset: int = 0, take: int = 20) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/devices', params={'offset': offset, 'take': take})
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def revoke_device(self, device_id: str) -> None:
        self._delete(f'{self._base_path}/devices/{device_id}')

    def revoke_all_other_devices(self) -> None:
        self._delete(f'{self._base_path}/devices/other')

    def update_device_label(self, device_id: str, label: str) -> None:
        self._patch(f'{self._base_path}/devices/{device_id}/label', json=label)

    def get_authorized_apps(self, type: int | None = None) -> list[dict[str, Any]]:
        params = self._clean_none({'type': type})
        response = self._get(f'{self._base_path}/authorized-apps', params=params)
        return response.json()

    def deauthorize_app(self, app_id: str, type: int | None = None) -> None:
        params = self._clean_none({'type': type})
        self._delete(f'{self._base_path}/authorized-apps/{app_id}', params=params)

    def get_account_punishment_overview(self, username: str) -> dict[str, Any] | None:
        response = self._get(f'{self._base_path}/accounts/{username}/punishments/overview')
        if response.text:
            return response.json()
        return None

    def get_account_punishments(self, username: str, offset: int = 0, take: int = 20) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/accounts/{username}/punishments', params={'offset': offset, 'take': take})
        total_count = self._get_total_count(response)
        items = response.json()
        has_more = len(items) == take
        cursor = str(offset + take) if has_more else None
        return PaginatedResult(items=items, total_count=total_count, has_more=has_more, cursor=cursor)

    def create_punishment(self, username: str, reason: str, type: int, expired_at: str | None = None, blocked_permissions: list[str] | None = None, social_credit_reduction: float | None = None) -> dict[str, Any]:
        data = self._clean_none({'reason': reason, 'type': type, 'expired_at': expired_at, 'blocked_permissions': blocked_permissions, 'social_credit_reduction': social_credit_reduction})
        response = self._post(f'{self._base_path}/admin/accounts/{username}/punishments', json=data)
        return response.json()

    def update_punishment(self, username: str, punishment_id: str, reason: str | None = None, type: int | None = None, expired_at: str | None = None, blocked_permissions: list[str] | None = None) -> dict[str, Any]:
        data = self._clean_none({'reason': reason, 'type': type, 'expired_at': expired_at, 'blocked_permissions': blocked_permissions})
        response = self._patch(f'{self._base_path}/admin/accounts/{username}/punishments/{punishment_id}', json=data)
        return response.json()

    def delete_punishment(self, username: str, punishment_id: str) -> None:
        self._delete(f'{self._base_path}/admin/accounts/{username}/punishments/{punishment_id}')

    def get_admin_created_punishments(self, offset: int = 0, take: int = 20) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/admin/accounts/punishments/created', params={'offset': offset, 'take': take})
        total_count = self._get_total_count(response)
        items = response.json()
        has_more = len(items) == take
        cursor = str(offset + take) if has_more else None
        return PaginatedResult(items=items, total_count=total_count, has_more=has_more, cursor=cursor)

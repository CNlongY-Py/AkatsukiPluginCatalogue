from typing import Any

from ...base_api import BaseApi, PaginatedResult


class NotificationsApi(BaseApi):
    _base_path = '/ring'

    def get_notifications(self, offset: int = 0, take: int = 20, app: str | None = None) -> PaginatedResult[dict[str, Any]]:
        params: dict[str, Any] = {'offset': offset, 'take': take}
        if app:
            params['app'] = app
        response = self._get(f'{self._base_path}/notifications', params=params)
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_notification(self, notification_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/notifications/{notification_id}')
        return response.json()

    def mark_as_read(self, notification_id: str) -> None:
        self._post(f'{self._base_path}/notifications/{notification_id}/read')

    def mark_all_as_read(self, app: str | None = None) -> None:
        params = None
        if app:
            params = {'app': app}
        self._post(f'{self._base_path}/notifications/all/read', params=params)

    def delete_notification(self, notification_id: str) -> None:
        self._delete(f'{self._base_path}/notifications/{notification_id}')

    def delete_all_notifications(self) -> None:
        self._delete(f'{self._base_path}/notifications')

    def get_unread_count(self, app: str | None = None) -> int:
        params = None
        if app:
            params = {'app': app}
        response = self._get(f'{self._base_path}/notifications/count', params=params)
        data = response.json()
        if isinstance(data, (int, float)):
            return int(data)
        if isinstance(data, dict):
            return int(data.get('count', 0))
        return 0

    def get_preferences(self) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/notifications/preferences')
        return response.json()

    def get_preference(self, topic: str) -> int:
        response = self._get(f'{self._base_path}/notifications/preferences/{topic}')
        data = response.json()
        return int(data.get('preference', 0))

    def set_preference(self, topic: str, preference: int) -> None:
        self._put(f'{self._base_path}/notifications/preferences/{topic}', json={'preference': preference})

    def delete_preference(self, topic: str) -> None:
        self._delete(f'{self._base_path}/notifications/preferences/{topic}')

    def add_custom_topic(self, topic: str, description: str) -> None:
        self._post(f'{self._base_path}/notifications/topics', json={'topic': topic, 'description': description})

    def get_subscriptions(self, app: str | None = None) -> list[dict[str, Any]]:
        params = None
        if app:
            params = {'app': app}
        response = self._get(f'{self._base_path}/notifications/subscription', params=params)
        return response.json()

    def get_current_subscription(self, app: str | None = None) -> dict[str, Any] | None:
        params = None
        if app:
            params = {'app': app}
        response = self._get(f'{self._base_path}/notifications/subscription/current', params=params)
        if not response.text:
            return None
        return response.json()

    def delete_subscription(self, subscription_id: str) -> None:
        self._delete(f'{self._base_path}/notifications/subscription/{subscription_id}')

    def register_push_subscription(self, device_token: str, provider: int, device_name: str | None = None, app_id: str | None = None) -> None:
        data: dict[str, Any] = {'device_token': device_token, 'provider': provider}
        if device_name:
            data['device_name'] = device_name
        if app_id:
            data['app_id'] = app_id
        self._put(f'{self._base_path}/notifications/subscription', json=data)

    def register_sop_subscription(self, device_name: str, app_id: str | None = None) -> dict[str, Any]:
        data: dict[str, Any] = {'device_name': device_name}
        if app_id:
            data['app_id'] = app_id
        response = self._post(f'{self._base_path}/notifications/sop/subscription', json=data)
        return response.json() if response.text else {}

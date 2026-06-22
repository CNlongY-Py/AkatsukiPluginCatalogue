from typing import Any

from ...base_api import BaseApi


class DevelopersApi(BaseApi):
    _base_path = '/developer'

    def get_projects(self) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/projects')
        return response.json()

    def get_project(self, project_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/projects/{project_id}')
        return response.json()

    def create_project(self, name: str, description: str | None = None) -> dict[str, Any]:
        data = self._clean_none({'name': name, 'description': description})
        response = self._post(f'{self._base_path}/projects', json=data)
        return response.json()

    def update_project(self, project_id: str, data: dict[str, Any]) -> dict[str, Any]:
        response = self._patch(f'{self._base_path}/projects/{project_id}', json=data)
        return response.json()

    def delete_project(self, project_id: str) -> None:
        self._delete(f'{self._base_path}/projects/{project_id}')

    def get_bots(self, project_id: str) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/projects/{project_id}/bots')
        return response.json()

    def get_bot(self, bot_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/bots/{bot_id}')
        return response.json()

    def create_bot(self, project_id: str, name: str, description: str | None = None) -> dict[str, Any]:
        data = self._clean_none({'name': name, 'description': description})
        response = self._post(f'{self._base_path}/projects/{project_id}/bots', json=data)
        return response.json()

    def update_bot(self, bot_id: str, data: dict[str, Any]) -> dict[str, Any]:
        response = self._patch(f'{self._base_path}/bots/{bot_id}', json=data)
        return response.json()

    def delete_bot(self, bot_id: str) -> None:
        self._delete(f'{self._base_path}/bots/{bot_id}')

    def get_bot_logs(self, bot_id: str, offset: int = 0, take: int = 100) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/bots/{bot_id}/logs', params={'offset': offset, 'take': take})
        return response.json()

    def get_apps(self, project_id: str) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/projects/{project_id}/apps')
        return response.json()

    def get_app(self, app_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/apps/{app_id}')
        return response.json()

    def create_app(self, project_id: str, name: str, redirect_uris: list[str], scopes: list[str]) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/projects/{project_id}/apps', json={'name': name, 'redirect_uris': redirect_uris, 'scopes': scopes})
        return response.json()

    def update_app(self, app_id: str, data: dict[str, Any]) -> dict[str, Any]:
        response = self._patch(f'{self._base_path}/apps/{app_id}', json=data)
        return response.json()

    def delete_app(self, app_id: str) -> None:
        self._delete(f'{self._base_path}/apps/{app_id}')

    def get_bot_keys(self, bot_id: str) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/bots/{bot_id}/keys')
        return response.json()

    def create_bot_key(self, bot_id: str, name: str, permissions: list[str] | None = None) -> dict[str, Any]:
        data = self._clean_none({'name': name, 'permissions': permissions})
        response = self._post(f'{self._base_path}/bots/{bot_id}/keys', json=data)
        return response.json()

    def revoke_bot_key(self, bot_id: str, key_id: str) -> None:
        self._delete(f'{self._base_path}/bots/{bot_id}/keys/{key_id}')

    def get_app_secrets(self, app_id: str) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/apps/{app_id}/secrets')
        return response.json()

    def create_app_secret(self, app_id: str, name: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/apps/{app_id}/secrets', json={'name': name})
        return response.json()

    def revoke_app_secret(self, app_id: str, secret_id: str) -> None:
        self._delete(f'{self._base_path}/apps/{app_id}/secrets/{secret_id}')

    def get_webhooks(self, app_id: str) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/apps/{app_id}/webhooks')
        return response.json()

    def create_webhook(self, app_id: str, url: str, events: list[str], secret: str | None = None) -> dict[str, Any]:
        data = self._clean_none({'url': url, 'events': events, 'secret': secret})
        response = self._post(f'{self._base_path}/apps/{app_id}/webhooks', json=data)
        return response.json()

    def update_webhook(self, webhook_id: str, data: dict[str, Any]) -> dict[str, Any]:
        response = self._patch(f'{self._base_path}/webhooks/{webhook_id}', json=data)
        return response.json()

    def delete_webhook(self, webhook_id: str) -> None:
        self._delete(f'{self._base_path}/webhooks/{webhook_id}')

    def test_webhook(self, webhook_id: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/webhooks/{webhook_id}/test')
        return response.json()

    def get_documentation(self) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/docs')
        return response.json()

    def get_changelog(self, offset: int = 0, take: int = 20) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/changelog', params={'offset': offset, 'take': take})
        return response.json()

    def get_api_status(self) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/status')
        return response.json()

    def get_rate_limit_info(self) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/rate-limit')
        return response.json()

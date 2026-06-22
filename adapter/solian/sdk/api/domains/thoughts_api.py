from typing import Any

from ...base_api import BaseApi


class ThoughtsApi(BaseApi):
    _base_path = '/personality'

    def get_sequences(self, offset: int = 0, take: int = 20) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/conversations', params={'offset': offset, 'take': take})
        return response.json()

    def get_sequence(self, sequence_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/conversations/{sequence_id}')
        return response.json()

    def create_conversation(self, agent_id: str, title: str | None = None) -> dict[str, Any]:
        data = self._clean_none({'agent_id': agent_id, 'title': title})
        response = self._post(f'{self._base_path}/conversations', json=data)
        return response.json()

    def get_sequence_messages(self, sequence_id: str, offset: int = 0, take: int = 50) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/conversations/{sequence_id}/messages', params={'offset': offset, 'take': take})
        data = response.json()
        if isinstance(data, list):
            return list(reversed(data))
        return []

    def add_message(self, conversation_id: str, content: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/conversations/{conversation_id}/messages', json={'content': content})
        return response.json()

    def create_run(self, conversation_id: str, data: dict[str, Any], stream: bool = False) -> Any:
        return self._post(f'{self._base_path}/conversations/{conversation_id}/runs', json=data)

    def get_services(self) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/agents')
        data = response.json() if isinstance(response.json(), list) else []
        services = [s for s in data if s.get('id')]
        return {
            'default_bot': services[0]['id'] if services else '',
            'services': services,
        }

    def get_billing_status(self) -> dict[str, Any]:
        return {'status': 'ok'}

    def get_quota(self) -> dict[str, Any]:
        return {'enabled': False, 'free_remaining': 0, 'free_used': 0, 'free_total': 0}

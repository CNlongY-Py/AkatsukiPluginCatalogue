from typing import Any

from ...base_api import BaseApi


class E2EEApi(BaseApi):
    _base_path = '/e2ee'

    def get_public_key(self, account_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/keys/{account_id}')
        return response.json()

    def upload_public_key(self, key_data: str, key_type: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/keys', json={'key_data': key_data, 'key_type': key_type})
        return response.json()

    def get_key_backup(self) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/keys/backup')
        return response.json()

    def create_key_backup(self, backup_data: dict[str, Any]) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/keys/backup', json=backup_data)
        return response.json()

    def rotate_keys(self, new_key_data: dict[str, Any]) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/keys/rotate', json=new_key_data)
        return response.json()

    def get_mls_groups(self) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/mls/groups')
        return response.json()

    def create_mls_group(self, name: str, member_ids: list[str]) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/mls/groups', json={'name': name, 'member_ids': member_ids})
        return response.json()

    def get_mls_group(self, group_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/mls/groups/{group_id}')
        return response.json()

    def update_mls_group(self, group_id: str, data: dict[str, Any]) -> dict[str, Any]:
        response = self._patch(f'{self._base_path}/mls/groups/{group_id}', json=data)
        return response.json()

    def delete_mls_group(self, group_id: str) -> None:
        self._delete(f'{self._base_path}/mls/groups/{group_id}')

    def add_mls_group_members(self, group_id: str, member_ids: list[str]) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/mls/groups/{group_id}/members', json={'member_ids': member_ids})
        return response.json()

    def remove_mls_group_members(self, group_id: str, member_ids: list[str]) -> dict[str, Any]:
        response = self._delete(f'{self._base_path}/mls/groups/{group_id}/members', json={'member_ids': member_ids})
        return response.json()

    def get_mls_group_messages(self, group_id: str, offset: int = 0, take: int = 50) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/mls/groups/{group_id}/messages', params={'offset': offset, 'take': take})
        return response.json()

    def send_mls_group_message(self, group_id: str, encrypted_content: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/mls/groups/{group_id}/messages', json={'encrypted_content': encrypted_content})
        return response.json()

    def get_mls_group_key_package(self, group_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/mls/groups/{group_id}/kp')
        return response.json()

    def process_mls_commit(self, group_id: str, commit_data: dict[str, Any]) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/mls/groups/{group_id}/commit', json=commit_data)
        return response.json()

    def encrypt_for_recipient(self, recipient_id: str, data: dict[str, Any]) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/encrypt/{recipient_id}', json=data)
        return response.json()

    def decrypt(self, encrypted_data: dict[str, Any]) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/decrypt', json=encrypted_data)
        return response.json()

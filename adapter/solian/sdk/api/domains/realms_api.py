from typing import Any

from ...base_api import BaseApi, PaginatedResult


class RealmsApi(BaseApi):
    _base_path = '/passport/realms'

    def get_realms(self, offset: int = 0, take: int = 20) -> PaginatedResult[dict[str, Any]]:
        response = self._get(self._base_path, params={'offset': offset, 'take': take})
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_realm(self, slug: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/{slug}')
        return response.json()

    def create_realm(self, slug: str, name: str, description: str | None = None, is_public: bool = True) -> dict[str, Any]:
        data = self._clean_none({'slug': slug, 'name': name, 'description': description, 'is_public': is_public})
        response = self._post(self._base_path, json=data)
        return response.json()

    def update_realm(self, slug: str, data: dict[str, Any]) -> dict[str, Any]:
        response = self._patch(f'{self._base_path}/{slug}', json=data)
        return response.json()

    def delete_realm(self, slug: str) -> None:
        self._delete(f'{self._base_path}/{slug}')

    def get_members(self, slug: str, offset: int = 0, take: int = 50, account_name: str | None = None, label_id: str | None = None, with_status: bool = False) -> PaginatedResult[dict[str, Any]]:
        params: dict[str, Any] = {'offset': offset, 'take': take, 'withStatus': with_status}
        if account_name:
            params['accountName'] = account_name
        if label_id:
            params['labelId'] = label_id
        response = self._get(f'{self._base_path}/{slug}/members', params=params)
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def join_realm(self, slug: str) -> None:
        self._post(f'{self._base_path}/{slug}/members/me')

    def leave_realm(self, slug: str) -> None:
        self._delete(f'{self._base_path}/{slug}/members/me')

    def get_my_membership(self, slug: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/{slug}/members/me')
        return response.json()

    def update_my_membership(self, slug: str, data: dict[str, Any]) -> dict[str, Any]:
        response = self._patch(f'{self._base_path}/{slug}/members/me/profile', json=data)
        return response.json()

    def kick_member(self, slug: str, account_id: str) -> None:
        self._delete(f'{self._base_path}/{slug}/members/{account_id}')

    def update_member_role(self, slug: str, account_id: str, role: int) -> dict[str, Any]:
        response = self._patch(f'{self._base_path}/{slug}/members/{account_id}/role', json=role)
        return response.json()

    def get_labels(self, slug: str) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/{slug}/labels')
        return response.json()

    def create_label(self, slug: str, name: str, description: str | None = None, color: str | None = None) -> dict[str, Any]:
        data = self._clean_none({'name': name, 'description': description, 'color': color})
        response = self._post(f'{self._base_path}/{slug}/labels', json=data)
        return response.json()

    def update_label(self, slug: str, label_id: str, data: dict[str, Any]) -> dict[str, Any]:
        response = self._patch(f'{self._base_path}/{slug}/labels/{label_id}', json=data)
        return response.json()

    def delete_label(self, slug: str, label_id: str) -> None:
        self._delete(f'{self._base_path}/{slug}/labels/{label_id}')

    def assign_label(self, slug: str, account_id: str, label_id: str | None) -> None:
        self._patch(f'{self._base_path}/{slug}/members/{account_id}/label', json={'label_id': label_id})

    def get_boost_status(self, slug: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/{slug}/boosts')
        return response.json()

    def get_boost_leaderboard(self, slug: str, take: int = 20) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/{slug}/boosts/leaderboard', params={'take': take})
        return response.json()

    def boost_realm(self, slug: str, shares: int, currency: str | None) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/{slug}/boosts', json={'shares': shares, 'currency': currency})
        return response.json()

    def get_role_permissions(self, slug: str) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/{slug}/permissions/roles')
        return response.json()

    def update_role_permission(self, slug: str, role_level: int, permissions: dict[str, Any]) -> dict[str, Any]:
        data = {'roleLevel': role_level}
        data.update(permissions)
        response = self._post(f'{self._base_path}/{slug}/permissions/roles', json=data)
        return response.json()

    def get_user_permission(self, slug: str, account_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/{slug}/permissions/users/{account_id}')
        return response.json()

    def update_user_permission(self, slug: str, account_id: str, permissions: dict[str, Any]) -> dict[str, Any]:
        data = {'accountId': account_id}
        data.update(permissions)
        response = self._post(f'{self._base_path}/{slug}/permissions/users', json=data)
        return response.json()

    def get_realm_chat(self, slug: str) -> list[dict[str, Any]]:
        response = self._get(f'/messager/realms/{slug}/chat')
        return response.json()

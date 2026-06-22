from typing import Any

from httpx import Response

from ...base_api import BaseApi


class StickersApi(BaseApi):
    _base_path = '/sphere/stickers'

    def list_sticker_packs(self, offset: int = 0, take: int = 20, pub_name: str | None = None, order: str | None = None, query: str | None = None) -> Response:
        params = {'offset': offset, 'take': take}
        if pub_name is not None:
            params['pub'] = pub_name
        if order is not None:
            params['order'] = order
        if query is not None:
            params['query'] = query
        return self._get(self._base_path, params=params)

    def list_owned_sticker_packs(self) -> Response:
        return self._get(f'{self._base_path}/me')

    def reorder_owned_sticker_packs(self, items: list[dict[str, Any]]) -> None:
        self._patch(f'{self._base_path}/me/order', json={'items': items})

    def get_sticker_pack(self, pack_id: str) -> Response:
        return self._get(f'{self._base_path}/{pack_id}')

    def create_sticker_pack(self, publisher_name: str, name: str, prefix: str, icon_id: str | None = None, description: str | None = None) -> Response:
        data = {'name': name, 'prefix': prefix}
        if icon_id is not None:
            data['icon_id'] = icon_id
        if description is not None:
            data['description'] = description
        return self._post(self._base_path, params={'pub': publisher_name}, json=data)

    def update_sticker_pack(self, pack_id: str, icon_id: str | None = None, name: str | None = None, description: str | None = None, prefix: str | None = None) -> Response:
        data: dict[str, Any] = {}
        if icon_id is not None:
            data['icon_id'] = icon_id
        if name is not None:
            data['name'] = name
        if description is not None:
            data['description'] = description
        if prefix is not None:
            data['prefix'] = prefix
        return self._patch(f'{self._base_path}/{pack_id}', json=data)

    def delete_sticker_pack(self, pack_id: str) -> None:
        self._delete(f'{self._base_path}/{pack_id}')

    def list_stickers(self, pack_id: str) -> Response:
        return self._get(f'{self._base_path}/{pack_id}/content')

    def get_sticker_by_identifier(self, identifier: str) -> Response:
        return self._get(f'{self._base_path}/lookup/{identifier}')

    def open_sticker_by_identifier(self, identifier: str) -> Response:
        return self._get(f'{self._base_path}/lookup/{identifier}/open')

    def search_stickers(self, query: str, take: int = 10, offset: int = 0) -> Response:
        return self._get(f'{self._base_path}/search', params={'query': query, 'take': take, 'offset': offset})

    def get_sticker(self, pack_id: str, sticker_id: str) -> Response:
        return self._get(f'{self._base_path}/{pack_id}/content/{sticker_id}')

    def create_sticker(self, pack_id: str, slug: str, image_id: str) -> Response:
        return self._post(f'{self._base_path}/{pack_id}/content', json={'slug': slug, 'image_id': image_id})

    def update_sticker(self, pack_id: str, sticker_id: str, slug: str | None = None, image_id: str | None = None) -> Response:
        data: dict[str, Any] = {}
        if slug is not None:
            data['slug'] = slug
        if image_id is not None:
            data['image_id'] = image_id
        return self._patch(f'{self._base_path}/{pack_id}/content/{sticker_id}', json=data)

    def delete_sticker(self, pack_id: str, sticker_id: str) -> None:
        self._delete(f'{self._base_path}/{pack_id}/content/{sticker_id}')

    def reorder_pack_stickers(self, pack_id: str, items: list[dict[str, Any]]) -> None:
        self._patch(f'{self._base_path}/{pack_id}/content/order', json={'items': items})

    def get_sticker_pack_ownership(self, pack_id: str) -> Response:
        return self._get(f'{self._base_path}/{pack_id}/own')

    def acquire_sticker_pack(self, pack_id: str) -> Response:
        return self._post(f'{self._base_path}/{pack_id}/own')

    def release_sticker_pack(self, pack_id: str) -> None:
        self._delete(f'{self._base_path}/{pack_id}/own')

    def get_pack_stickers(self, pack_id: str) -> list[dict[str, Any]]:
        response = self.list_stickers(pack_id)
        return response.json()

    def add_pack_to_collection(self, pack_id: str) -> None:
        self.acquire_sticker_pack(pack_id)

    def remove_pack_from_collection(self, pack_id: str) -> None:
        self.release_sticker_pack(pack_id)

    def get_user_packs(self) -> list[dict[str, Any]]:
        response = self.list_owned_sticker_packs()
        return response.json()

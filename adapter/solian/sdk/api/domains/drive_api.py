from typing import Any

from httpx import Client, Response

from ...base_api import BaseApi, PaginatedResult


class DriveApi(BaseApi):
    _base_path = '/drive'

    def open_file(self, file_id: str, download: bool = False, original: bool = False, thumbnail: bool = False, override_mime_type: str | None = None, passcode: str | None = None) -> Response:
        params: dict[str, Any] = {}
        if download:
            params['download'] = True
        if original:
            params['original'] = True
        if thumbnail:
            params['thumbnail'] = True
        if override_mime_type is not None:
            params['overrideMimeType'] = override_mime_type
        if passcode is not None:
            params['passcode'] = passcode
        return self._get(f'{self._base_path}/files/{file_id}', params=params)

    def download_file(self, file_id: str, save_path: str) -> Response:
        with Client() as client:
            response = client.get(f'{self._base_path}/files/{file_id}')
            with open(save_path, 'wb') as f:
                f.write(response.content)
            return response

    def get_e2ee_meta(self, file_id: str, passcode: str | None = None) -> dict[str, Any] | None:
        params = self._clean_none({'passcode': passcode})
        response = self._get(f'{self._base_path}/files/{file_id}/e2ee', params=params)
        return response.json() if response.text else None

    def get_file_info(self, file_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/files/{file_id}/info')
        return response.json()

    def get_file_references(self, file_id: str) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/files/{file_id}/references')
        return response.json()

    def get_file_permissions(self, file_id: str) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/files/{file_id}/permissions')
        return response.json()

    def update_file_name(self, file_id: str, new_name: str) -> dict[str, Any]:
        response = self._patch(f'{self._base_path}/files/{file_id}', json={'name': new_name})
        return response.json()

    def update_sensitive_marks(self, file_id: str, marks: list[str]) -> dict[str, Any]:
        response = self._put(f'{self._base_path}/files/{file_id}/marks', json={'sensitive_marks': marks})
        return response.json()

    def update_user_meta(self, file_id: str, meta: dict[str, Any]) -> dict[str, Any]:
        response = self._put(f'{self._base_path}/files/{file_id}/meta', json=meta)
        return response.json()

    def update_file_permissions(self, file_id: str, items: list[dict[str, Any]]) -> None:
        self._put(f'{self._base_path}/files/{file_id}/permissions', json={'items': items})

    def delete_file(self, file_id: str) -> None:
        self._delete(f'{self._base_path}/files/{file_id}')

    def batch_delete_files(self, file_ids: list[str]) -> int:
        response = self._delete(f'{self._base_path}/files/batches/delete', json={'file_ids': file_ids})
        data = response.json()
        return int(data.get('count', 0))

    def list_root_children(self, offset: int = 0, take: int = 50, query: str | None = None, name: str | None = None, extension: str | None = None, order: str | None = None, order_desc: bool = True, pool_id: str | None = None, usage: str | None = None, application_type: str | None = None, content_type: str | None = None, mime_type: str | None = None, parent_id: str | None = None, indexed: bool | None = None, is_folder: bool | None = None, has_thumbnail: bool | None = None, has_compression: bool | None = None, min_size: int | None = None, max_size: int | None = None, created_after: str | None = None, created_before: str | None = None, updated_after: str | None = None, updated_before: str | None = None) -> PaginatedResult[dict[str, Any]]:
        resolved_content_type = content_type or mime_type
        params = self._clean_none({'offset': offset, 'take': take, 'query': query, 'name': name, 'extension': extension, 'order': order, 'orderDesc': order_desc, 'pool': pool_id, 'usage': usage, 'application_type': application_type, 'content_type': resolved_content_type, 'parent_id': parent_id, 'indexed': indexed, 'is_folder': is_folder, 'has_thumbnail': has_thumbnail, 'has_compression': has_compression, 'min_size': min_size, 'max_size': max_size, 'created_after': created_after, 'created_before': created_before, 'updated_after': updated_after, 'updated_before': updated_before})
        response = self._get(f'{self._base_path}/files/root/children', params=params)
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def list_folder_children(self, parent_id: str, offset: int = 0, take: int = 50, query: str | None = None, name: str | None = None, extension: str | None = None, order: str | None = None, order_desc: bool = True, pool_id: str | None = None, usage: str | None = None, application_type: str | None = None, content_type: str | None = None, mime_type: str | None = None, indexed: bool | None = None, is_folder: bool | None = None, has_thumbnail: bool | None = None, has_compression: bool | None = None, min_size: int | None = None, max_size: int | None = None, created_after: str | None = None, created_before: str | None = None, updated_after: str | None = None, updated_before: str | None = None) -> PaginatedResult[dict[str, Any]]:
        resolved_content_type = content_type or mime_type
        params = self._clean_none({'offset': offset, 'take': take, 'query': query, 'name': name, 'extension': extension, 'order': order, 'orderDesc': order_desc, 'pool': pool_id, 'usage': usage, 'application_type': application_type, 'content_type': resolved_content_type, 'indexed': indexed, 'is_folder': is_folder, 'has_thumbnail': has_thumbnail, 'has_compression': has_compression, 'min_size': min_size, 'max_size': max_size, 'created_after': created_after, 'created_before': created_before, 'updated_after': updated_after, 'updated_before': updated_before})
        response = self._get(f'{self._base_path}/files/{parent_id}/children', params=params)
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def create_folder(self, name: str, parent_id: str | None = None) -> dict[str, Any]:
        data = self._clean_none({'name': name, 'parent_id': parent_id})
        response = self._post(f'{self._base_path}/files/folders', json=data)
        return response.json()

    def move_file(self, file_id: str, parent_id: str | None = None, indexed: bool | None = None) -> dict[str, Any]:
        data = self._clean_none({'parent_id': parent_id, 'indexed': indexed})
        response = self._patch(f'{self._base_path}/files/{file_id}/hierarchy', json=data)
        return response.json()

    def list_unindexed_files(self, pool_id: str | None = None, recycled: bool = False, offset: int = 0, take: int = 20, query: str | None = None, name: str | None = None, extension: str | None = None, order: str | None = None, order_desc: bool = True, usage: str | None = None, application_type: str | None = None, content_type: str | None = None, mime_type: str | None = None, is_folder: bool | None = None, has_thumbnail: bool | None = None, has_compression: bool | None = None, min_size: int | None = None, max_size: int | None = None, created_after: str | None = None, created_before: str | None = None, updated_after: str | None = None, updated_before: str | None = None) -> PaginatedResult[dict[str, Any]]:
        resolved_content_type = content_type or mime_type
        params = self._clean_none({'pool': pool_id, 'recycled': recycled, 'offset': offset, 'take': take, 'query': query, 'name': name, 'extension': extension, 'order': order, 'orderDesc': order_desc, 'usage': usage, 'application_type': application_type, 'content_type': resolved_content_type, 'is_folder': is_folder, 'has_thumbnail': has_thumbnail, 'has_compression': has_compression, 'min_size': min_size, 'max_size': max_size, 'created_after': created_after, 'created_before': created_before, 'updated_after': updated_after, 'updated_before': updated_before})
        response = self._get(f'{self._base_path}/files/unindexed', params=params)
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def list_my_files(self, pool_id: str | None = None, recycled: bool = False, offset: int = 0, take: int = 20, query: str | None = None, name: str | None = None, extension: str | None = None, order: str | None = None, order_desc: bool = True, usage: str | None = None, application_type: str | None = None, content_type: str | None = None, mime_type: str | None = None, is_folder: bool | None = None, has_thumbnail: bool | None = None, has_compression: bool | None = None, min_size: int | None = None, max_size: int | None = None, created_after: str | None = None, created_before: str | None = None, updated_after: str | None = None, updated_before: str | None = None) -> PaginatedResult[dict[str, Any]]:
        resolved_content_type = content_type or mime_type
        params = self._clean_none({'pool': pool_id, 'recycled': recycled, 'offset': offset, 'take': take, 'query': query, 'name': name, 'extension': extension, 'order': order, 'orderDesc': order_desc, 'usage': usage, 'application_type': application_type, 'content_type': resolved_content_type, 'is_folder': is_folder, 'has_thumbnail': has_thumbnail, 'has_compression': has_compression, 'min_size': min_size, 'max_size': max_size, 'created_after': created_after, 'created_before': created_before, 'updated_after': updated_after, 'updated_before': updated_before})
        response = self._get(f'{self._base_path}/files/me', params=params)
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def delete_recycled_files(self) -> int:
        response = self._delete(f'{self._base_path}/files/me/recycle')
        data = response.json()
        return int(data.get('count', 0))

    def delete_all_recycled_files(self) -> int:
        response = self._delete(f'{self._base_path}/files/recycle')
        data = response.json()
        return int(data.get('count', 0))

    def create_upload_task(self, hash: str, file_name: str, file_size: int, content_type: str, pool_id: str | None = None, bundle_id: str | None = None, encryption_scheme: str | None = None, encryption_header: str | None = None, encryption_signature: str | None = None, expired_at: str | None = None, chunk_size: int | None = None, parent_id: str | None = None, usage: str | None = None, application_type: str | None = None) -> dict[str, Any]:
        data = self._clean_none({'hash': hash, 'file_name': file_name, 'file_size': file_size, 'content_type': content_type, 'pool_id': pool_id, 'bundle_id': bundle_id, 'encryption_scheme': encryption_scheme, 'encryption_header': encryption_header, 'encryption_signature': encryption_signature, 'expired_at': expired_at, 'chunk_size': chunk_size, 'parent_id': parent_id, 'usage': usage, 'application_type': application_type})
        response = self._post(f'{self._base_path}/files/upload/create', json=data)
        return response.json()

    def upload_chunk(self, task_id: str, chunk_index: int, chunk_data: bytes, file_name: str | None = None) -> None:
        files = {'chunk': (file_name or f'chunk_{chunk_index}', chunk_data)}
        self._post(f'{self._base_path}/files/upload/chunk/{task_id}/{chunk_index}', files=files)

    def complete_upload(self, task_id: str) -> Response:
        return self._post(f'{self._base_path}/files/upload/complete/{task_id}')

    def direct_upload(self, file_bytes: bytes, file_name: str, content_type: str | None = None, pool_id: str | None = None, bundle_id: str | None = None, encryption_scheme: str | None = None, encryption_header: str | None = None, encryption_signature: str | None = None, expired_at: str | None = None, parent_id: str | None = None, usage: str | None = None, application_type: str | None = None) -> dict[str, Any]:
        files = {'file': (file_name, file_bytes)}
        data = self._clean_none({'content_type': content_type, 'pool_id': pool_id, 'bundle_id': bundle_id, 'encryption_scheme': encryption_scheme, 'encryption_header': encryption_header, 'encryption_signature': encryption_signature, 'expired_at': expired_at, 'parent_id': parent_id, 'usage': usage, 'application_type': application_type})
        response = self._post(f'{self._base_path}/files/upload/direct', files=files, data=data)
        return response.json()

    def list_upload_tasks(self, status: str | None = None, sort_by: str = 'lastActivity', sort_descending: bool = True, offset: int = 0, limit: int = 50) -> list[dict[str, Any]]:
        params = self._clean_none({'status': status, 'sortBy': sort_by, 'sortDescending': sort_descending, 'offset': offset, 'limit': limit})
        response = self._get(f'{self._base_path}/files/upload/tasks', params=params)
        return response.json()

    def get_upload_progress(self, task_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/files/upload/progress/{task_id}')
        return response.json()

    def resume_upload(self, task_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/files/upload/resume/{task_id}')
        return response.json()

    def cancel_upload(self, task_id: str) -> None:
        self._delete(f'{self._base_path}/files/upload/task/{task_id}')

    def get_upload_stats(self) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/files/upload/stats')
        return response.json()

    def get_recent_tasks(self, limit: int = 10) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/files/upload/tasks/recent', params={'limit': limit})
        return response.json()

    def get_task_details(self, task_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/files/upload/tasks/{task_id}/details')
        return response.json()

    def cleanup_failed_tasks(self) -> str:
        response = self._delete(f'{self._base_path}/files/upload/tasks/cleanup')
        data = response.json()
        return data.get('message', '')

    def get_bundle(self, bundle_id: str, passcode: str | None = None) -> dict[str, Any]:
        params = self._clean_none({'passcode': passcode})
        response = self._get(f'{self._base_path}/bundles/{bundle_id}', params=params)
        return response.json()

    def list_my_bundles(self, term: str | None = None, offset: int = 0, take: int = 20) -> PaginatedResult[dict[str, Any]]:
        params = self._clean_none({'term': term, 'offset': offset, 'take': take})
        response = self._get(f'{self._base_path}/bundles/me', params=params)
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def create_bundle(self, slug: str | None = None, name: str | None = None, description: str | None = None, passcode: str | None = None, expired_at: str | None = None) -> dict[str, Any]:
        data = self._clean_none({'slug': slug, 'name': name, 'description': description, 'passcode': passcode, 'expired_at': expired_at})
        response = self._post(f'{self._base_path}/bundles', json=data)
        return response.json()

    def update_bundle(self, bundle_id: str, slug: str | None = None, name: str | None = None, description: str | None = None, passcode: str | None = None, expired_at: str | None = None) -> dict[str, Any]:
        data = self._clean_none({'slug': slug, 'name': name, 'description': description, 'passcode': passcode, 'expired_at': expired_at})
        response = self._put(f'{self._base_path}/bundles/{bundle_id}', json=data)
        return response.json()

    def delete_bundle(self, bundle_id: str) -> None:
        self._delete(f'{self._base_path}/bundles/{bundle_id}')

    def list_pools(self) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/pools')
        return response.json()

    def delete_pool_recycled_files(self, pool_id: str) -> int:
        response = self._delete(f'{self._base_path}/pools/{pool_id}/recycle')
        data = response.json()
        return int(data.get('count', 0))

    def get_total_usage(self) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/billing/usage')
        return response.json()

    def get_pool_usage(self, pool_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/billing/usage/{pool_id}')
        return response.json()

    def get_quota(self) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/billing/quota')
        return response.json()

    def get_quota_records(self, expired: bool = False, offset: int = 0, take: int = 20) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/billing/quota/records', params={'expired': expired, 'offset': offset, 'take': take})
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

from typing import Any

from ...base_api import BaseApi, PaginatedResult


class SphereApi(BaseApi):
    _base_path = '/sphere'

    def get_post(self, post_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/posts/{post_id}')
        return response.json()

    def list_publisher_collections(self, publisher_name: str) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/publishers/{publisher_name}/collections')
        return response.json()

    def get_publisher_collection(self, publisher_name: str, slug: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/publishers/{publisher_name}/collections/{slug}')
        return response.json()

    def create_publisher_collection(self, publisher_name: str, slug: str, name: str | None = None, description: str | None = None, background_id: str | None = None, icon_id: str | None = None) -> dict[str, Any]:
        data = self._clean_none({'slug': slug, 'name': name, 'description': description, 'background_id': background_id, 'icon_id': icon_id})
        response = self._post(f'{self._base_path}/publishers/{publisher_name}/collections', json=data)
        return response.json()

    def update_publisher_collection(self, publisher_name: str, slug: str, name: str | None = None, description: str | None = None, background_id: str | None = None, clear_background: bool = False, icon_id: str | None = None, clear_icon: bool = False) -> dict[str, Any]:
        data: dict[str, Any] = {}
        if name is not None:
            data['name'] = name
        if description is not None:
            data['description'] = description
        if clear_background:
            data['background_id'] = None
        elif background_id is not None:
            data['background_id'] = background_id
        if clear_icon:
            data['icon_id'] = None
        elif icon_id is not None:
            data['icon_id'] = icon_id
        response = self._patch(f'{self._base_path}/publishers/{publisher_name}/collections/{slug}', json=data)
        return response.json()

    def delete_publisher_collection(self, publisher_name: str, slug: str) -> None:
        self._delete(f'{self._base_path}/publishers/{publisher_name}/collections/{slug}')

    def list_publisher_collection_posts(self, publisher_name: str, slug: str, offset: int = 0, take: int = 20) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/publishers/{publisher_name}/collections/{slug}/posts', params={'offset': offset, 'take': take})
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def reorder_publisher_collection_posts(self, publisher_name: str, slug: str, post_ids: list[str]) -> None:
        self._put(f'{self._base_path}/publishers/{publisher_name}/collections/{slug}/posts/reorder', json={'post_ids': post_ids})

    def get_publisher_collection_prev_post(self, publisher_name: str, slug: str, post_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/publishers/{publisher_name}/collections/{slug}/posts/{post_id}/prev')
        return response.json()

    def get_publisher_collection_next_post(self, publisher_name: str, slug: str, post_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/publishers/{publisher_name}/collections/{slug}/posts/{post_id}/next')
        return response.json()

    def add_post_to_collection(self, publisher_name: str, slug: str, post_id: str, order: int | None = None) -> None:
        data = self._clean_none({'post_id': post_id, 'order': order})
        self._post(f'{self._base_path}/publishers/{publisher_name}/collections/{slug}/posts', json=data)

    def remove_post_from_collection(self, publisher_name: str, slug: str, post_id: str) -> None:
        self._delete(f'{self._base_path}/publishers/{publisher_name}/collections/{slug}/posts/{post_id}')

    def batch_add_posts_to_collection(self, publisher_name: str, slug: str, post_ids: list[str]) -> None:
        self._post(f'{self._base_path}/publishers/{publisher_name}/collections/{slug}/posts/batch', json={'post_ids': post_ids})

    def batch_remove_posts_from_collection(self, publisher_name: str, slug: str, post_ids: list[str]) -> None:
        self._post(f'{self._base_path}/publishers/{publisher_name}/collections/{slug}/posts/batch/remove', json={'post_ids': post_ids})

    def batch_delete_posts(self, post_ids: list[str]) -> None:
        self._post(f'{self._base_path}/posts/batch/delete', json={'post_ids': post_ids})

    def batch_update_post_visibility(self, post_ids: list[str], visibility: str | None = None, drafted_at: str | None = None, published_at: str | None = None) -> None:
        data = self._clean_none({'post_ids': post_ids, 'visibility': visibility, 'drafted_at': drafted_at, 'published_at': published_at})
        self._post(f'{self._base_path}/posts/batch/visibility', json=data)

    def get_posts(self, offset: int = 0, take: int = 20, sort: str | None = None) -> PaginatedResult[dict[str, Any]]:
        params = self._clean_none({'offset': offset, 'take': take, 'sort': sort})
        response = self._get(f'{self._base_path}/posts', params=params)
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def create_post(self, content: str, metadata: dict[str, Any] | None = None) -> dict[str, Any]:
        data = {'content': content}
        if metadata:
            data.update(metadata)
        response = self._post(f'{self._base_path}/posts', json=data)
        return response.json()

    def update_post(self, post_id: str, data: dict[str, Any]) -> dict[str, Any]:
        response = self._patch(f'{self._base_path}/posts/{post_id}', json=data)
        return response.json()

    def delete_post(self, post_id: str) -> None:
        self._delete(f'{self._base_path}/posts/{post_id}')

    def pin_post(self, post_id: str) -> None:
        self._post(f'{self._base_path}/posts/{post_id}/pin')

    def unpin_post(self, post_id: str) -> None:
        self._delete(f'{self._base_path}/posts/{post_id}/pin')

    def boost_post(self, post_id: str) -> None:
        self._post(f'{self._base_path}/posts/{post_id}/boost')

    def unboost_post(self, post_id: str) -> None:
        self._delete(f'{self._base_path}/posts/{post_id}/boost')

    def get_post_bookmark(self, post_id: str) -> dict[str, Any] | None:
        response = self._get(f'{self._base_path}/posts/{post_id}/bookmark')
        if response.status_code == 204:
            return None
        return response.json()

    def bookmark_post(self, post_id: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/posts/{post_id}/bookmark')
        return response.json()

    def unbookmark_post(self, post_id: str) -> None:
        self._delete(f'{self._base_path}/posts/{post_id}/bookmark')

    def get_bookmarks(self, offset: int = 0, take: int = 20, order: str | None = None) -> PaginatedResult[dict[str, Any]]:
        params = self._clean_none({'offset': offset, 'take': take, 'order': order})
        response = self._get(f'{self._base_path}/posts/bookmarks', params=params)
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_post_replies(self, post_id: str, offset: int = 0, take: int = 20) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/posts/{post_id}/replies', params={'offset': offset, 'take': take})
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_featured_replies(self, post_id: str) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/posts/{post_id}/replies/featured')
        return response.json()

    def create_reply(self, post_id: str, content: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/posts/{post_id}/replies', json={'content': content})
        return response.json()

    def get_post_reactions(self, post_id: str, symbol: str | None = None, offset: int = 0, take: int = 20, order: str | None = None) -> PaginatedResult[dict[str, Any]]:
        params = self._clean_none({'offset': offset, 'take': take, 'symbol': symbol, 'order': order})
        response = self._get(f'{self._base_path}/posts/{post_id}/reactions', params=params)
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def add_reaction(self, post_id: str, reaction_type: str) -> None:
        self._post(f'{self._base_path}/posts/{post_id}/reactions', json={'type': reaction_type})

    def remove_reaction(self, post_id: str) -> None:
        self._delete(f'{self._base_path}/posts/{post_id}/reactions')

    def get_user_reactions(self, name: str, offset: int = 0, take: int = 20, order: str | None = None) -> PaginatedResult[dict[str, Any]]:
        params = self._clean_none({'offset': offset, 'take': take, 'order': order})
        response = self._get(f'{self._base_path}/posts/reactions/users/{name}', params=params)
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_post_awards(self, post_id: str) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/posts/{post_id}/awards')
        return response.json()

    def give_award(self, post_id: str, award_type: str) -> None:
        self._post(f'{self._base_path}/posts/{post_id}/awards', json={'type': award_type})

    def get_post_heatmap(self, username: str | None = None, year: int | None = None, month: int | None = None) -> dict[str, Any]:
        params = self._clean_none({'username': username, 'year': year, 'month': month})
        response = self._get(f'{self._base_path}/posts/heatmap', params=params)
        return response.json()

    def get_publisher(self, username: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/publishers/{username}')
        return response.json()

    def create_publisher(self, name: str, metadata: dict[str, Any] | None = None) -> dict[str, Any]:
        data = {'name': name}
        if metadata:
            data.update(metadata)
        response = self._post(f'{self._base_path}/publishers', json=data)
        return response.json()

    def update_publisher(self, username: str, data: dict[str, Any]) -> dict[str, Any]:
        response = self._patch(f'{self._base_path}/publishers/{username}', json=data)
        return response.json()

    def delete_publisher(self, username: str) -> None:
        self._delete(f'{self._base_path}/publishers/{username}')

    def get_publisher_posts(self, username: str, offset: int = 0, take: int = 20) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/publishers/{username}/posts', params={'offset': offset, 'take': take})
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_publisher_subscription_status(self, username: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/publishers/{username}/subscription')
        return response.json()

    def subscribe_to_publisher(self, username: str) -> None:
        self._post(f'{self._base_path}/publishers/{username}/subscribe')

    def unsubscribe_from_publisher(self, username: str) -> None:
        self._post(f'{self._base_path}/publishers/{username}/unsubscribe')

    def get_publisher_rating(self, name: str) -> float:
        response = self._get(f'{self._base_path}/publishers/{name}/rating')
        value = response.json()
        if isinstance(value, (int, float)):
            return float(value)
        return 0.0

    def get_publisher_rating_history(self, name: str, take: int = 20, offset: int = 0) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/publishers/{name}/rating/history', params={'take': take, 'offset': offset})
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_publisher_rating_overview(self, name: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/publishers/{name}/rating/overview')
        return response.json()

    def get_publisher_leaderboard(self, take: int = 20, offset: int = 0) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/publishers/leaderboard', params={'take': take, 'offset': offset})
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_publisher_features(self, username: str) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/publishers/{username}/features')
        return response.json()

    def get_publisher_heatmap(self, username: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/publishers/{username}/heatmap')
        return response.json()

    def get_categories(self) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/categories')
        return response.json()

    def get_category(self, slug: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/categories/{slug}')
        return response.json()

    def get_category_posts(self, slug: str, offset: int = 0, take: int = 20) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/categories/{slug}/posts', params={'offset': offset, 'take': take})
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def subscribe_to_category(self, slug: str) -> None:
        self._post(f'{self._base_path}/categories/{slug}/subscribe')

    def unsubscribe_from_category(self, slug: str) -> None:
        self._post(f'{self._base_path}/categories/{slug}/unsubscribe')

    def get_category_subscription_status(self, slug: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/categories/{slug}/subscription')
        return response.json()

    def get_posts_by_tag(self, tag: str, offset: int = 0, take: int = 20) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/tags/{tag}/posts', params={'offset': offset, 'take': take})
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_tag(self, slug: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/posts/tags/{slug}')
        return response.json()

    def create_tag(self, slug: str, name: str | None = None, description: str | None = None, publisher_name: str | None = None) -> dict[str, Any]:
        params = self._clean_none({'pub': publisher_name})
        data = self._clean_none({'slug': slug, 'name': name, 'description': description})
        response = self._post(f'{self._base_path}/posts/tags', params=params, json=data)
        return response.json()

    def update_tag(self, slug: str, name: str | None = None, description: str | None = None, publisher_name: str | None = None) -> dict[str, Any]:
        params = self._clean_none({'pub': publisher_name})
        data = self._clean_none({'name': name, 'description': description})
        response = self._patch(f'{self._base_path}/posts/tags/{slug}', params=params, json=data)
        return response.json()

    def claim_tag(self, slug: str, publisher_name: str | None = None) -> dict[str, Any]:
        params = self._clean_none({'pub': publisher_name})
        response = self._post(f'{self._base_path}/posts/tags/{slug}/claim', params=params)
        return response.json()

    def get_protected_tag_quota(self, slug: str, publisher_name: str | None = None) -> dict[str, Any]:
        params = self._clean_none({'pub': publisher_name})
        response = self._get(f'{self._base_path}/posts/tags/{slug}/quota', params=params)
        return response.json()

    def assign_tag_ownership(self, slug: str, publisher_id: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/admin/posts/tags/{slug}/assign', json={'publisher_id': publisher_id})
        return response.json()

    def toggle_tag_protection(self, slug: str, is_protected: bool) -> dict[str, Any]:
        response = self._patch(f'{self._base_path}/admin/posts/tags/{slug}/protect', json={'is_protected': is_protected})
        return response.json()

    def set_tag_event_status(self, slug: str, is_event: bool, ends_at: str | None = None) -> dict[str, Any]:
        data = self._clean_none({'is_event': is_event, 'ends_at': ends_at})
        response = self._patch(f'{self._base_path}/admin/posts/tags/{slug}/event', json=data)
        return response.json()

    def admin_update_tag(self, slug: str, name: str | None = None, description: str | None = None) -> dict[str, Any]:
        data = self._clean_none({'name': name, 'description': description})
        response = self._patch(f'{self._base_path}/admin/posts/tags/{slug}', json=data)
        return response.json()

    def get_home_timeline(self, offset: int = 0, take: int = 20) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/timeline/home', params={'offset': offset, 'take': take})
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def search_posts(self, query: str, offset: int = 0, take: int = 20) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/search/posts', params={'q': query, 'offset': offset, 'take': take})
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def search_publishers(self, query: str, offset: int = 0, take: int = 20) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/search/publishers', params={'q': query, 'offset': offset, 'take': take})
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_link_preview(self, url: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/embed/preview', params={'url': url})
        return response.json()

    def get_account_publishers(self, account_id: str) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/publishers/of/{account_id}')
        return response.json()

    def get_discovery_profile(self) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/timeline/discovery/profile')
        return response.json()

    def reset_discovery_profile(self) -> None:
        self._post(f'{self._base_path}/timeline/discovery/reset')

    def get_publishing_settings(self) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/account/publishing')
        return response.json()

    def update_publishing_settings(self, default_posting_publisher_id: str | None = None, default_reply_publisher_id: str | None = None, default_fediverse_publisher_id: str | None = None) -> dict[str, Any]:
        data = self._clean_none({'default_posting_publisher_id': default_posting_publisher_id, 'default_reply_publisher_id': default_reply_publisher_id, 'default_fediverse_publisher_id': default_fediverse_publisher_id})
        response = self._patch(f'{self._base_path}/account/publishing', json=data)
        return response.json()

    def get_fediverse_availability(self) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/fediverse/actors/availability')
        return response.json()

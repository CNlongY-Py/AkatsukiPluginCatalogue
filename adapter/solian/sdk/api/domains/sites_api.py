from typing import Any

from ...base_api import BaseApi


class SitesApi(BaseApi):
    _base_path = '/site'

    def get_sites(self) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/sites')
        return response.json()

    def get_site(self, site_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/sites/{site_id}')
        return response.json()

    def create_site(self, name: str, slug: str, description: str | None = None) -> dict[str, Any]:
        data = self._clean_none({'name': name, 'slug': slug, 'description': description})
        response = self._post(f'{self._base_path}/sites', json=data)
        return response.json()

    def update_site(self, site_id: str, data: dict[str, Any]) -> dict[str, Any]:
        response = self._patch(f'{self._base_path}/sites/{site_id}', json=data)
        return response.json()

    def delete_site(self, site_id: str) -> None:
        self._delete(f'{self._base_path}/sites/{site_id}')

    def get_site_analytics(self, site_id: str, period: str = 'month') -> dict[str, Any]:
        response = self._get(f'{self._base_path}/sites/{site_id}/analytics', params={'period': period})
        return response.json()

    def get_pages(self, site_id: str) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/sites/{site_id}/pages')
        return response.json()

    def get_page(self, site_id: str, page_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/sites/{site_id}/pages/{page_id}')
        return response.json()

    def create_page(self, site_id: str, title: str, slug: str, content: str | None = None) -> dict[str, Any]:
        data = self._clean_none({'title': title, 'slug': slug, 'content': content})
        response = self._post(f'{self._base_path}/sites/{site_id}/pages', json=data)
        return response.json()

    def update_page(self, site_id: str, page_id: str, data: dict[str, Any]) -> dict[str, Any]:
        response = self._patch(f'{self._base_path}/sites/{site_id}/pages/{page_id}', json=data)
        return response.json()

    def delete_page(self, site_id: str, page_id: str) -> None:
        self._delete(f'{self._base_path}/sites/{site_id}/pages/{page_id}')

    def publish_page(self, site_id: str, page_id: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/sites/{site_id}/pages/{page_id}/publish')
        return response.json()

    def unpublish_page(self, site_id: str, page_id: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/sites/{site_id}/pages/{page_id}/unpublish')
        return response.json()

    def get_templates(self) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/templates')
        return response.json()

    def get_template(self, template_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/templates/{template_id}')
        return response.json()

    def apply_template(self, site_id: str, template_id: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/sites/{site_id}/templates/{template_id}')
        return response.json()

    def get_theme_settings(self, site_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/sites/{site_id}/theme')
        return response.json()

    def update_theme_settings(self, site_id: str, settings: dict[str, Any]) -> dict[str, Any]:
        response = self._patch(f'{self._base_path}/sites/{site_id}/theme', json=settings)
        return response.json()

    def get_themes(self) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/themes')
        return response.json()

    def apply_theme(self, site_id: str, theme_id: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/sites/{site_id}/theme/{theme_id}')
        return response.json()

    def get_custom_domains(self, site_id: str) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/sites/{site_id}/domains')
        return response.json()

    def add_custom_domain(self, site_id: str, domain: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/sites/{site_id}/domains', json={'domain': domain})
        return response.json()

    def remove_custom_domain(self, site_id: str, domain: str) -> None:
        self._delete(f'{self._base_path}/sites/{site_id}/domains/{domain}')

    def verify_custom_domain(self, site_id: str, domain: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/sites/{site_id}/domains/{domain}/verify')
        return response.json()

    def deploy_site(self, site_id: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/sites/{site_id}/deploy')
        return response.json()

    def get_deployments(self, site_id: str, offset: int = 0, take: int = 20) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/sites/{site_id}/deployments', params={'offset': offset, 'take': take})
        return response.json()

    def get_deployment_status(self, site_id: str, deployment_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/sites/{site_id}/deployments/{deployment_id}')
        return response.json()

    def rollback_deployment(self, site_id: str, deployment_id: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/sites/{site_id}/deployments/{deployment_id}/rollback')
        return response.json()

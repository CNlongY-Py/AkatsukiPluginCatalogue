from typing import Any

from ...base_api import BaseApi


class AuthApi(BaseApi):
    _base_path = '/padlock'

    def authenticate(self, username: str, password: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/auth/token', json={'username': username, 'password': password})
        return response.json()

    def refresh_token(self, refresh_token: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/auth/token', json={'grant_type': 'refresh_token', 'refresh_token': refresh_token})
        return response.json()

    def revoke_token(self) -> None:
        self._delete(f'{self._base_path}/auth/token')

    def get_pending_challenges(self) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/auth/challenge/pending')
        return response.json()

    def approve_challenge(self, challenge_id: str, pin_code: str | None = None) -> None:
        self._post(f'{self._base_path}/auth/challenge/{challenge_id}/approve', json={'pin_code': pin_code})

    def decline_challenge(self, challenge_id: str, pin_code: str | None = None) -> None:
        self._post(f'{self._base_path}/auth/challenge/{challenge_id}/decline', json={'pin_code': pin_code})

    def get_current_session(self) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/sessions/current')
        return response.json()

    def revoke_current_session(self) -> None:
        self._delete(f'{self._base_path}/sessions/current')

    def get_sessions(self) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/sessions')
        return response.json()

    def revoke_session(self, session_id: str) -> None:
        self._delete(f'{self._base_path}/sessions/{session_id}')

    def revoke_all_other_sessions(self) -> None:
        self._delete(f'{self._base_path}/sessions/other')

    def get_factors(self) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/factors')
        return response.json()

    def create_factor(self, type: int, secret: str | None = None) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/factors', json={'type': type, 'secret': secret})
        return response.json()

    def delete_factor(self, factor_id: str) -> None:
        self._delete(f'{self._base_path}/factors/{factor_id}')

    def disable_factor(self, factor_id: str) -> None:
        self._post(f'{self._base_path}/factors/{factor_id}/disable')

    def enable_factor(self, factor_id: str) -> None:
        self._post(f'{self._base_path}/factors/{factor_id}/enable')

    def create_factor_challenge(self, factor_id: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/factors/{factor_id}/challenge')
        return response.json()

    def verify_factor_challenge(self, factor_id: str, challenge_id: str, response_value: str) -> bool:
        response = self._post(f'{self._base_path}/factors/{factor_id}/challenges/{challenge_id}', json={'response': response_value})
        data = response.json()
        if isinstance(data, bool):
            return data
        return False

    def start_passkey_registration(self, device_id: str, device_name: str, rp_id: str, rp_name: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/factors/passkey/start', json={'device_id': device_id, 'device_name': device_name, 'rp_id': rp_id, 'rp_name': rp_name})
        return response.json()

    def complete_passkey_registration(self, device_id: str, device_name: str | None = None, attestation_object: str = '', client_data_json: str = '') -> dict[str, Any]:
        response = self._post(f'{self._base_path}/factors/passkey/complete', json={'device_id': device_id, 'device_name': device_name, 'attestation_object': attestation_object, 'client_data_json': client_data_json})
        return response.json()

    def start_passkey_authentication(self, challenge_id: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/auth/challenge/{challenge_id}/passkey/start')
        return response.json()

    def complete_passkey_authentication(self, challenge_id: str, factor_id: str, credential_id: str, client_data_json: str, authenticator_data: str, signature: str, user_handle: str | None = None) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/auth/challenge/{challenge_id}/passkey/complete', json={'factor_id': factor_id, 'credential_id': credential_id, 'client_data_json': client_data_json, 'authenticator_data': authenticator_data, 'signature': signature, 'user_handle': user_handle})
        return response.json()

    def get_contacts(self) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/contacts')
        return response.json()

    def add_contact(self, type: int, content: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/contacts', json={'type': type, 'content': content})
        return response.json()

    def delete_contact(self, contact_id: str) -> None:
        self._delete(f'{self._base_path}/contacts/{contact_id}')

    def get_connections(self) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/connections')
        return response.json()

    def disconnect(self, connection_id: str) -> None:
        self._delete(f'{self._base_path}/connections/{connection_id}')

    def get_devices(self) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/devices')
        return response.json()

    def revoke_device(self, device_id: str) -> None:
        self._delete(f'{self._base_path}/devices/{device_id}')

    def revoke_all_other_devices(self) -> None:
        self._delete(f'{self._base_path}/devices/other')

    def initiate_web_auth(self, app_slug: str, redirect_uri: str, state: str | None = None) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/auth/web', json={'app': app_slug, 'redirect_uri': redirect_uri, 'state': state})
        return response.json()

    def exchange_web_auth(self, signed_challenge: str, device_info: dict[str, Any] | None = None, secret_id: str | None = None) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/auth/web/exchange', json={'signed_challenge': signed_challenge, 'device_info': device_info, 'secret_id': secret_id})
        return response.json()

    def get_oauth_authorization_url(self, app_id: str, redirect_uri: str, scopes: list[str], state: str | None = None) -> str:
        response = self._get(f'{self._base_path}/oauth/authorize', params={'app_id': app_id, 'redirect_uri': redirect_uri, 'scope': ','.join(scopes), 'state': state})
        data = response.json()
        return data.get('url', '')

    def exchange_oauth_code(self, code: str, redirect_uri: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/oauth/token', json={'grant_type': 'authorization_code', 'code': code, 'redirect_uri': redirect_uri})
        return response.json()

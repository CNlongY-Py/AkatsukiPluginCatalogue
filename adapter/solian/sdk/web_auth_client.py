from dataclasses import dataclass, field
from enum import Enum
from httpx import Client


class WebAuthStatus(Enum):
    CHALLENGE = "challenge"
    SUCCESS = "success"
    ERROR = "error"
    DENIED = "denied"


@dataclass
class WebAuthResult:
    status: WebAuthStatus
    challenge: str | None = None
    token: str | None = None
    refresh_token: str | None = None
    expires_in: int | None = None
    refresh_expires_in: int | None = None
    error: str | None = None


class WebAuthClient:
    def __init__(self, base_url: str, port: int, web_url: str):
        self._base_url = base_url
        self._port = port
        self._web_url = web_url

    def set_port(self, port: int):
        self._port = port

    async def get_authentication_url(self) -> str:
        return f"{self._web_url}/auth/web?port={self._port}"

    def get_protocol_challenge_url(
        self,
        app_slug: str,
        redirect_uri: str,
        state: str | None = None,
    ) -> str:
        params = f"app={app_slug}&redirect_uri={redirect_uri}"
        if state:
            params += f"&state={state}"
        return f"solian://auth/web?{params}"

    def get_protocol_exchange_url(
        self,
        signed_challenge: str,
        redirect_uri: str,
        secret_id: str | None = None,
        state: str | None = None,
    ) -> str:
        parts = [
            f"signed_challenge={signed_challenge}",
            f"redirect_uri={redirect_uri}",
        ]
        if secret_id:
            parts.append(f"secret_id={secret_id}")
        if state:
            parts.append(f"state={state}")
        return f"solian://auth/web?{'&'.join(parts)}"

    def wait_for_auth(self) -> WebAuthResult:
        with Client() as client:
            resp = client.get(f"http://127.0.0.1:{self._port}/alive")
            if resp.status_code == 200:
                data = resp.json()
                status = data.get("status")
                if status == "denied":
                    return WebAuthResult(status=WebAuthStatus.DENIED)
                return WebAuthResult(
                    status=WebAuthStatus.CHALLENGE,
                    challenge=data.get("challenge"),
                )
            raise Exception("Failed to get challenge")

    def exchange_token(
        self,
        signed_challenge: str,
        device_info: dict | None = None,
        secret_id: str | None = None,
    ) -> WebAuthResult:
        payload: dict = {"signed_challenge": signed_challenge}
        if device_info is not None:
            payload["device_info"] = device_info
        if secret_id:
            payload["secret_id"] = secret_id

        with Client() as client:
            resp = client.post(
                f"http://127.0.0.1:{self._port}/exchange",
                json=payload,
            )
            data = resp.json() if resp.content else {}
            if resp.status_code == 200:
                return WebAuthResult(
                    status=WebAuthStatus.SUCCESS,
                    token=data.get("token"),
                    refresh_token=data.get("refresh_token"),
                    expires_in=_to_int(data.get("expires_in")),
                    refresh_expires_in=_to_int(data.get("refresh_expires_in")),
                )
            return WebAuthResult(
                status=WebAuthStatus.ERROR,
                error=data.get("error"),
            )


def _to_int(value):
    if isinstance(value, (int, float)):
        return int(value)
    return None

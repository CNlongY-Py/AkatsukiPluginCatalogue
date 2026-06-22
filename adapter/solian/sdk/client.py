from httpx import Client, Limits, Timeout

from .api.domains.auth_api import AuthApi
from .api.domains.accounts_api import AccountsApi
from .api.domains.sphere_api import SphereApi
from .api.domains.wallet_api import WalletApi
from .api.domains.chat_api import ChatApi
from .api.domains.thoughts_api import ThoughtsApi
from .api.domains.e2ee_api import E2EEApi
from .api.domains.drive_api import DriveApi
from .api.domains.stickers_api import StickersApi
from .api.domains.notifications_api import NotificationsApi
from .api.domains.tickets_api import TicketsApi
from .api.domains.polls_api import PollsApi
from .api.domains.sites_api import SitesApi
from .api.domains.developers_api import DevelopersApi
from .api.domains.payments_api import PaymentsApi
from .api.domains.realms_api import RealmsApi
from .api.domains.padlock_api import PadlockApi
from .api.domains.fitness_api import FitnessApi


class SolarNetworkClient:
    def __init__(
        self,
        base_url: str,
        connect_timeout: float = 10.0,
        read_timeout: float = 10.0,
        headers: dict | None = None,
        **kwargs,
    ):
        default_headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        if headers:
            default_headers.update(headers)

        self._client = Client(
            base_url=base_url,
            timeout=Timeout(connect_timeout, read=read_timeout),
            limits=Limits(max_keepalive_connections=20, max_connections=100),
            headers=default_headers,
            **kwargs,
        )

        self.auth = AuthApi(self._client)
        self.accounts = AccountsApi(self._client)
        self.sphere = SphereApi(self._client)
        self.wallet = WalletApi(self._client)
        self.chat = ChatApi(self._client)
        self.thoughts = ThoughtsApi(self._client)
        self.e2ee = E2EEApi(self._client)
        self.drive = DriveApi(self._client)
        self.stickers = StickersApi(self._client)
        self.notifications = NotificationsApi(self._client)
        self.tickets = TicketsApi(self._client)
        self.polls = PollsApi(self._client)
        self.sites = SitesApi(self._client)
        self.developers = DevelopersApi(self._client)
        self.payments = PaymentsApi(self._client)
        self.realms = RealmsApi(self._client)
        self.padlock = PadlockApi(self._client)
        self.fitness = FitnessApi(self._client)

    @property
    def client(self) -> Client:
        return self._client

    def close(self):
        self._client.close()

    def set_base_url(self, base_url: str):
        self._client.base_url = base_url

    def set_default_headers(self, headers: dict):
        self._client.headers.update(headers)

    def remove_default_header(self, key: str):
        self._client.headers.pop(key, None)

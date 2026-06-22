from typing import Any

from ...base_api import BaseApi, PaginatedResult


class WalletApi(BaseApi):
    _base_path = '/wallet'

    def get_wallet(self) -> dict[str, Any] | None:
        try:
            response = self._get(f'{self._base_path}/wallets')
            return response.json()
        except Exception:
            return None

    def get_wallets(self) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/wallets/all')
        return response.json()

    def get_wallet_by_id(self, id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/wallets/{id}')
        return response.json()

    def create_wallet(self, name: str | None = None, realm_id: str | None = None) -> dict[str, Any]:
        data = self._clean_none({'name': name, 'realm_id': realm_id})
        response = self._post(f'{self._base_path}/wallets', json=data)
        return response.json()

    def set_default_wallet(self, id: str) -> None:
        self._post(f'{self._base_path}/wallets/{id}/default')

    def enable_public_id(self, id: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/wallets/{id}/public-id/enable')
        return response.json()

    def disable_public_id(self, id: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/wallets/{id}/public-id/disable')
        return response.json()

    def get_wallet_stats(self) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/wallets/stats')
        return response.json()

    def get_funds(self, offset: int = 0, take: int = 20) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/wallets/funds', params={'offset': offset, 'take': take})
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_fund(self, fund_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/wallets/funds/{fund_id}')
        return response.json()

    def create_fund(self, currency: str, total_amount: float, amount_of_splits: int, split_type: int, recipient_account_ids: list[str] | None = None, message: str | None = None, expiration_hours: int | None = None, pin_code: str | None = None, is_raising: bool = False, target_amount: float = 0, contribution_type: int = 0, contribution_amount: float = 0, is_open: bool = True, deadline_at: str | None = None) -> dict[str, Any]:
        data = self._clean_none({'currency': currency, 'total_amount': total_amount, 'amount_of_splits': amount_of_splits, 'split_type': split_type, 'recipient_account_ids': recipient_account_ids or [], 'message': message, 'expiration_hours': expiration_hours, 'pin_code': pin_code, 'is_raising': is_raising, 'target_amount': target_amount, 'contribution_type': contribution_type, 'contribution_amount': contribution_amount, 'is_open': is_open, 'deadline_at': deadline_at})
        response = self._post(f'{self._base_path}/wallets/funds', json=data)
        return response.json()

    def update_fund(self, fund_id: str, data: dict[str, Any]) -> dict[str, Any]:
        response = self._patch(f'{self._base_path}/wallets/funds/{fund_id}', json=data)
        return response.json()

    def delete_fund(self, fund_id: str) -> None:
        self._delete(f'{self._base_path}/wallets/funds/{fund_id}')

    def contribute_to_fund(self, fund_id: str, amount: float = 0) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/wallets/funds/{fund_id}/contribute', json={'amount': amount})
        return response.json()

    def get_fund_contributors(self, fund_id: str) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/wallets/funds/{fund_id}/contributors')
        return response.json()

    def transfer(self, amount: float, currency: str, pin_code: str, payer_wallet_id: str | None = None, payee_wallet_id: str | None = None, payee_account_id: str | None = None, payee_public_id: str | None = None, remark: str | None = None, freeze: bool = False, require_confirmation: bool = False) -> dict[str, Any]:
        data = self._clean_none({'amount': amount, 'currency': currency, 'pin_code': pin_code, 'payer_wallet_id': payer_wallet_id, 'payee_wallet_id': payee_wallet_id, 'payee_account_id': payee_account_id, 'payee_public_id': payee_public_id, 'remark': remark, 'freeze': freeze, 'require_confirmation': require_confirmation})
        response = self._post(f'{self._base_path}/wallets/transfer', json=data)
        return response.json()

    def get_transactions(self, offset: int = 0, take: int = 20, wallet: str | None = None, direction: str | None = None, type: str | None = None) -> PaginatedResult[dict[str, Any]]:
        params = self._clean_none({'offset': offset, 'take': take, 'wallet': wallet, 'direction': direction, 'type': type})
        response = self._get(f'{self._base_path}/wallets/transactions', params=params)
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_transaction(self, transaction_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/wallets/transactions/{transaction_id}')
        return response.json()

    def confirm_transaction(self, transaction_id: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/wallets/transactions/{transaction_id}/confirm')
        return response.json()

    def reject_transaction(self, transaction_id: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/wallets/transactions/{transaction_id}/reject')
        return response.json()

    def get_pending_transactions(self, offset: int = 0, take: int = 20) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/wallets/transactions/pending', params={'offset': offset, 'take': take})
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_subscriptions(self) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/wallets/subscriptions')
        return response.json()

    def get_subscription(self, subscription_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/wallets/subscriptions/{subscription_id}')
        return response.json()

    def cancel_subscription(self, subscription_id: str) -> None:
        self._delete(f'{self._base_path}/wallets/subscriptions/{subscription_id}')

    def get_subscription_catalog(self) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/wallets/subscriptions/catalog')
        return response.json()

    def get_active_subscriptions(self) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/wallets/subscriptions/active')
        return response.json()

    def create_order(self, product_id: str, quantity: int = 1) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/wallets/orders', json={'product_id': product_id, 'quantity': quantity})
        return response.json()

    def get_orders(self, offset: int = 0, take: int = 20, wallet: str | None = None, status: str | None = None, direction: str | None = None, type: str | None = None) -> PaginatedResult[dict[str, Any]]:
        params = self._clean_none({'offset': offset, 'take': take, 'wallet': wallet, 'status': status, 'direction': direction, 'type': type})
        response = self._get(f'{self._base_path}/wallets/orders', params=params)
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_order(self, order_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/orders/{order_id}')
        return response.json()

    def send_gift(self, to_wallet_id: str, gift_id: str, message: str | None = None) -> dict[str, Any]:
        data = self._clean_none({'to_wallet_id': to_wallet_id, 'gift_id': gift_id, 'message': message})
        response = self._post(f'{self._base_path}/gifts', json=data)
        return response.json()

    def get_gifts(self, offset: int = 0, take: int = 20) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/gifts', params={'offset': offset, 'take': take})
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

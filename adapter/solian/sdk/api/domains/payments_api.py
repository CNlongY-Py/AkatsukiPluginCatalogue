from typing import Any

from httpx import Response

from ...base_api import BaseApi, PaginatedResult


class PaymentsApi(BaseApi):
    _base_path = '/payment'

    def get_payments(self, status: str | None = None, offset: int = 0, take: int = 20) -> PaginatedResult[dict[str, Any]]:
        params = self._clean_none({'status': status, 'offset': offset, 'take': take})
        response = self._get(f'{self._base_path}/payments', params=params)
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_payment(self, payment_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/payments/{payment_id}')
        return response.json()

    def create_payment(self, amount: float, currency: str, method_id: str, description: str | None = None, metadata: dict[str, Any] | None = None) -> dict[str, Any]:
        data = self._clean_none({'amount': amount, 'currency': currency, 'method_id': method_id, 'description': description, 'metadata': metadata})
        response = self._post(f'{self._base_path}/payments', json=data)
        return response.json()

    def cancel_payment(self, payment_id: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/payments/{payment_id}/cancel')
        return response.json()

    def refund_payment(self, payment_id: str, amount: float | None = None, reason: str | None = None) -> dict[str, Any]:
        data = self._clean_none({'amount': amount, 'reason': reason})
        response = self._post(f'{self._base_path}/payments/{payment_id}/refund', json=data)
        return response.json()

    def get_payment_methods(self) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/methods')
        return response.json()

    def get_payment_method(self, method_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/methods/{method_id}')
        return response.json()

    def add_payment_method(self, type: str, data: dict[str, Any], set_as_default: bool = False) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/methods', json={'type': type, 'data': data, 'set_as_default': set_as_default})
        return response.json()

    def update_payment_method(self, method_id: str, data: dict[str, Any]) -> dict[str, Any]:
        response = self._patch(f'{self._base_path}/methods/{method_id}', json=data)
        return response.json()

    def delete_payment_method(self, method_id: str) -> None:
        self._delete(f'{self._base_path}/methods/{method_id}')

    def set_default_payment_method(self, method_id: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/methods/{method_id}/default')
        return response.json()

    def get_default_payment_method(self) -> dict[str, Any] | None:
        try:
            response = self._get(f'{self._base_path}/methods/default')
            return response.json()
        except Exception:
            return None

    def get_invoices(self, status: str | None = None, offset: int = 0, take: int = 20) -> PaginatedResult[dict[str, Any]]:
        params = self._clean_none({'status': status, 'offset': offset, 'take': take})
        response = self._get(f'{self._base_path}/invoices', params=params)
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_invoice(self, invoice_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/invoices/{invoice_id}')
        return response.json()

    def create_invoice(self, items: list[dict[str, Any]], customer_info: dict[str, Any], due_date: str | None = None) -> dict[str, Any]:
        data: dict[str, Any] = {'items': items, 'customer_info': customer_info}
        if due_date is not None:
            data['due_date'] = due_date
        response = self._post(f'{self._base_path}/invoices', json=data)
        return response.json()

    def send_invoice(self, invoice_id: str, email: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/invoices/{invoice_id}/send', json={'email': email})
        return response.json()

    def download_invoice_pdf(self, invoice_id: str) -> Response:
        return self._get(f'{self._base_path}/invoices/{invoice_id}/pdf')

    def get_subscriptions(self) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/subscriptions')
        return response.json()

    def get_subscription(self, subscription_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/subscriptions/{subscription_id}')
        return response.json()

    def create_subscription(self, plan_id: str, payment_method_id: str, metadata: dict[str, Any] | None = None) -> dict[str, Any]:
        data = self._clean_none({'plan_id': plan_id, 'payment_method_id': payment_method_id, 'metadata': metadata})
        response = self._post(f'{self._base_path}/subscriptions', json=data)
        return response.json()

    def cancel_subscription(self, subscription_id: str, cancel_at_period_end: bool = True) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/subscriptions/{subscription_id}/cancel', json={'cancel_at_period_end': cancel_at_period_end})
        return response.json()

    def update_subscription(self, subscription_id: str, data: dict[str, Any]) -> dict[str, Any]:
        response = self._patch(f'{self._base_path}/subscriptions/{subscription_id}', json=data)
        return response.json()

    def change_subscription_plan(self, subscription_id: str, new_plan_id: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/subscriptions/{subscription_id}/change-plan', json={'new_plan_id': new_plan_id})
        return response.json()

    def get_plans(self) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/plans')
        return response.json()

    def get_plan(self, plan_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/plans/{plan_id}')
        return response.json()

    def get_plan_pricing(self, plan_id: str, currency: str = 'USD') -> dict[str, Any]:
        response = self._get(f'{self._base_path}/plans/{plan_id}/pricing', params={'currency': currency})
        return response.json()

    def get_transactions(self, offset: int = 0, take: int = 20) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/transactions', params={'offset': offset, 'take': take})
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_transaction(self, transaction_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/transactions/{transaction_id}')
        return response.json()

    def get_balance(self) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/balance')
        return response.json()

    def get_balance_transactions(self, offset: int = 0, take: int = 20) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/balance/transactions', params={'offset': offset, 'take': take})
        return response.json()

    def withdraw_balance(self, amount: float, method_id: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/balance/withdraw', json={'amount': amount, 'method_id': method_id})
        return response.json()

    def get_refunds(self, offset: int = 0, take: int = 20) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/refunds', params={'offset': offset, 'take': take})
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_refund(self, refund_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/refunds/{refund_id}')
        return response.json()

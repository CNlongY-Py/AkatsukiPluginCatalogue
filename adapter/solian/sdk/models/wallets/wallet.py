from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, Field

from ..accounts.account import SnAccount


class SnWalletPocket(BaseModel):
    id: str = ""
    currency: str = ""
    amount: float = 0.0
    held_amount: float = 0.0
    wallet_id: str = ""
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None


class SnWallet(BaseModel):
    id: str = ""
    pockets: list[SnWalletPocket] = Field(default_factory=list)
    account_id: Optional[str] = None
    realm_id: Optional[str] = None
    name: str = ""
    is_primary: bool = False
    public_id: Optional[str] = None
    account: Optional[SnAccount] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None


class SnWalletStats(BaseModel):
    period_begin: Optional[str] = None
    period_end: Optional[str] = None
    total_transactions: int = 0
    total_orders: int = 0
    total_income: float = 0.0
    total_outgoing: float = 0.0
    sum: float = 0.0
    income_categories: dict[str, float] = Field(default_factory=dict)
    outgoing_categories: dict[str, float] = Field(default_factory=dict)


class SnTransaction(BaseModel):
    id: str = ""
    currency: str = ""
    amount: float = 0.0
    remarks: Optional[str] = None
    type: int = 0
    status: int = 2
    is_frozen: bool = False
    require_confirmation: bool = False
    frozen_at: Optional[str] = None
    expires_at: Optional[str] = None
    confirmed_at: Optional[str] = None
    payer_wallet_id: Optional[str] = None
    payer_wallet: Optional[SnWallet] = None
    payee_wallet_id: Optional[str] = None
    payee_wallet: Optional[SnWallet] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None


class SnWalletSubscriptionRef(BaseModel):
    id: str = ""
    is_active: bool = False
    account_id: str = ""
    created_at: Optional[str] = None
    deleted_at: Optional[str] = None
    updated_at: Optional[str] = None
    identifier: str = ""


class SnWalletSubscription(BaseModel):
    id: str = ""
    begun_at: Optional[str] = None
    ended_at: Optional[str] = None
    identifier: str = ""
    group_identifier: Optional[str] = None
    is_active: bool = True
    is_free_trial: bool = False
    status: int = 1
    payment_method: Optional[str] = None
    payment_details: Optional[dict[str, Any]] = None
    base_price: Optional[float] = None
    coupon_id: Optional[str] = None
    coupon: Any = None
    renewal_at: Optional[str] = None
    account_id: str = ""
    account: Optional[SnAccount] = None
    is_available: bool = True
    is_pending_activation: bool = False
    final_price: Optional[float] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None


class SnSubscriptionDisplayConfig(BaseModel):
    color: str = ""
    background_color: Any = None
    badge_text: Any = None


class SnProductProviderMappings(BaseModel):
    afdian: list[str] = Field(default_factory=list)
    paddle: list[str] = Field(default_factory=list)
    apple_store: list[str] = Field(default_factory=list)


class SnSubscriptionCatalog(BaseModel):
    identifier: str = ""
    group_identifier: str = ""
    display_name: str = ""
    currency: str = ""
    base_price: int = 0
    perk_level: int = 0
    minimum_account_level: int = 0
    experience_multiplier: float = 0.0
    golden_point_reward: int = 0
    display_config: Optional[SnSubscriptionDisplayConfig] = None
    allowed_payment_methods: list[str] = Field(default_factory=list)
    provider_mappings: Optional[SnProductProviderMappings] = None


class SnSubscriptionGroupCatalog(BaseModel):
    group_identifier: str = ""
    display_name: str = ""
    max_perk_level: int = 0
    display_config: Optional[SnSubscriptionDisplayConfig] = None
    items: list[SnSubscriptionCatalog] = Field(default_factory=list)


class SnActiveSubscription(BaseModel):
    subscription: Optional[SnWalletSubscription] = None
    definition: Optional[SnSubscriptionCatalog] = None


class SnSubscriptionGroup(BaseModel):
    group_identifier: str = ""
    catalog: Optional[SnSubscriptionGroupCatalog] = None
    current: Optional[SnActiveSubscription] = None
    next: Optional[SnActiveSubscription] = None
    subscriptions: list[SnActiveSubscription] = Field(default_factory=list)


class SnWalletOrder(BaseModel):
    id: str = ""
    status: int = 0
    currency: str = ""
    remarks: Optional[str] = None
    app_identifier: str = ""
    meta: dict[str, Any] = Field(default_factory=dict)
    amount: int = 0
    expired_at: Optional[str] = None
    payee_wallet_id: Optional[str] = None
    transaction_id: Optional[str] = None
    issuer_app_id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None


class SnWalletGift(BaseModel):
    id: str = ""
    gift_code: str = ""
    subscription_identifier: str = ""
    recipient_id: Optional[str] = None
    recipient: Optional[SnAccount] = None
    gifter_id: str = ""
    gifter: Optional[SnAccount] = None
    redeemer_id: Optional[str] = None
    redeemer: Optional[SnAccount] = None
    message: Optional[str] = None
    status: int = 0
    redeemed_at: Optional[str] = None
    expired_at: Optional[str] = None
    subscription_id: Optional[str] = None
    subscription: Optional[SnWalletSubscription] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None


class SnWalletFundRecipient(BaseModel):
    id: str = ""
    fund_id: str = ""
    recipient_account_id: str = ""
    recipient_account: Optional[SnAccount] = None
    amount: float = 0.0
    is_received: bool = False
    received_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None


class SnWalletFund(BaseModel):
    id: str = ""
    currency: str = ""
    total_amount: float = 0.0
    remaining_amount: float = 0.0
    amount_of_splits: int = 0
    split_type: int = 0
    status: int = 0
    message: Optional[str] = None
    creator_account_id: str = ""
    creator_account: Optional[SnAccount] = None
    is_raising: bool = False
    target_amount: float = 0.0
    contribution_type: int = 0
    contribution_amount: float = 0.0
    deadline_at: Optional[str] = None
    expired_at: Optional[str] = None
    recipients: list[SnWalletFundRecipient] = Field(default_factory=list)
    is_open: bool = False
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None

from dataclasses import dataclass
from typing import Iterable
from uuid import UUID


@dataclass
class CheckoutItem:
    """CheckoutItem represents the data for an item in a checkout."""

    product_id: UUID
    quantity: int


@dataclass
class CheckoutOrder:
    """CheckoutOrderRequest encapsulates all necessary data for performing a checkout."""

    customer_id: UUID
    items: Iterable[CheckoutItem]


@dataclass
class CheckoutResult:
    """CheckoutOrderResponse provides the outcome of the checkout operation."""

    number: UUID


__all__ = ["CheckoutItem", "CheckoutOrder", "CheckoutResult"]

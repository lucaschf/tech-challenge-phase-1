from dataclasses import dataclass
from datetime import datetime
from typing import Iterable
from uuid import UUID

from src.core.domain.value_objects import OrderStatus


@dataclass
class OrderItemResult:
    """OrderItemResult represents the details of an order item."""

    product_name: str
    quantity: int
    unit_price: float


@dataclass
class CustomerSummaryResult:
    """CustomerSummaryResult represents the details of a customer."""

    name: str
    email: str
    cpf: str


@dataclass
class OrderDetailsResult:
    """OrderDetails represents the details of an order."""

    uuid: UUID
    created_at: datetime
    updated_at: datetime
    status: OrderStatus
    total_value: float
    items: Iterable[OrderItemResult]
    customer: CustomerSummaryResult


__all__ = ["CustomerSummaryResult", "OrderDetailsResult", "OrderItemResult"]

from dataclasses import dataclass, field
from enum import StrEnum, auto

from src.core.domain.base import AggregateRoot, AssertionConcern

from .order import Order


class PaymentStatus(StrEnum):
    """An Enum that represents a Payment Status."""

    PENDING = auto()  # Default status when a payment is created, means it's waiting for processing
    PROCESSING = auto()  # Payment is being processed by the payment gateway
    APPROVED = auto()  # Payment was approved
    REJECTED = auto()  # Payment was rejected
    FAILED = auto()  # Payment failed for some reason


@dataclass(kw_only=True)
class Payment(AggregateRoot):
    """Represents a payment in the system."""

    order: Order
    status: PaymentStatus = field(default=PaymentStatus.PENDING)
    details: dict

    def validate(self) -> None:
        """Validates the payment's attributes."""
        AssertionConcern.assert_argument_not_null(self.order, "Order is required")
        AssertionConcern.assert_argument_not_null(self.status, "Status is required")
        AssertionConcern.assert_argument_not_empty(self.details, "Details are required")


__all__ = ["Payment", "PaymentStatus"]

from dataclasses import dataclass, field
from enum import StrEnum, auto
from typing import Dict, Iterable

from src.core.domain.base import AggregateRoot, AssertionConcern

from ..exceptions import InvalidStatusTransitionError
from .order import Order


class PaymentStatus(StrEnum):
    """An Enum that represents a Payment Status."""

    PENDING = auto()  # Default status when a payment is created, means it's waiting for processing
    PROCESSING = auto()  # Payment is being processed by the payment gateway
    APPROVED = auto()  # Payment was approved
    REJECTED = auto()  # Payment was rejected
    FAILED = auto()  # Payment failed for some reason

    def get_allowed_transitions(self) -> Iterable["PaymentStatus"]:
        """Returns the allowed transitions for the given status."""
        _transitions: Dict["PaymentStatus", Iterable["PaymentStatus"]] = {
            PaymentStatus.PENDING: [PaymentStatus.PROCESSING],
            PaymentStatus.PROCESSING: [
                PaymentStatus.APPROVED,
                PaymentStatus.REJECTED,
                PaymentStatus.FAILED,
            ],
            PaymentStatus.FAILED: [PaymentStatus.PROCESSING],
        }

        return _transitions.get(self, [])


@dataclass(kw_only=True)
class Payment(AggregateRoot):
    """Represents a payment in the system."""

    order: Order
    status: PaymentStatus = field(default=PaymentStatus.PENDING)
    details: dict

    def update_status(self, new_status: PaymentStatus) -> None:
        """Updates the status of the payment.

        Args:
            new_status: The new status of the payment.

        Raises:
            InvalidStatusTransitionError: If the new status is invalid.
        """
        if new_status not in self.status.get_allowed_transitions():
            raise InvalidStatusTransitionError(self.status, new_status)
        self.status = new_status

    def validate(self) -> None:
        """Validates the payment's attributes."""
        AssertionConcern.assert_argument_not_null(self.order, "Order is required")
        AssertionConcern.assert_argument_not_null(self.status, "Status is required")
        AssertionConcern.assert_argument_not_empty(self.details, "Details are required")


__all__ = ["Payment", "PaymentStatus"]

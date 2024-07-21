import copy
from dataclasses import dataclass, field
from typing import List

from ..base import AggregateRoot, AssertionConcern
from ..exceptions import InvalidStatusTransitionError
from ..value_objects import OrderStatus
from .customer import Customer
from .order_item import OrderItem


@dataclass(kw_only=True)
class Order(AggregateRoot):
    """Represents an order in the system."""

    _customer: Customer
    _items: List[OrderItem] = field(default_factory=list)
    _total_value: float = field(default=0.0)
    _status: OrderStatus = field(default_factory=lambda: OrderStatus.PAYMENT_PENDING)

    def __post_init__(self) -> None:
        self.validate()
        self._recalculate_total_value()

    @property
    def status(self) -> OrderStatus:  # noqa: D102
        return self._status

    @property
    def total_value(self) -> float:  # noqa: D102
        return self._total_value

    @property
    def items(self) -> List[OrderItem]:
        """Returns a list of items in the order."""
        return copy.deepcopy(self._items)

    @property
    def customer(self) -> Customer:
        """Returns the customer who made the order."""
        return self._customer

    def _recalculate_total_value(self) -> None:
        self._total_value = sum(item.unit_price * item.quantity for item in self._items)

    @status.setter
    def status(self, new_status: OrderStatus) -> None:
        """Updates the status of the order.

        Args:
            new_status: The new status of the order.

        Raises:
            InvalidStatusTransitionError: If the new status is invalid.
        """
        if new_status not in self.status.get_allowed_transitions():
            raise InvalidStatusTransitionError(self.status, new_status)
        self._status = new_status

    def validate(self) -> None:
        """Validates the order's attributes.

        This method checks if the user_uuid, products, and status are valid.
        If any of these conditions are not met,
         a DomainError will be raised with a relevant message.

        Raises:
            DomainError: If any of the order's attributes are invalid.
        """
        AssertionConcern.assert_argument_not_null(self.customer, "Customer is required")
        AssertionConcern.assert_argument_not_null(self.items, "Items are required")
        AssertionConcern.assert_argument_not_empty(self.items, "Items are required")
        AssertionConcern.assert_argument_not_null(self.status, "Status is required")


__all__ = ["Order"]

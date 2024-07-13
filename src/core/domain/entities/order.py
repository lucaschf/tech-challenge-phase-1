from dataclasses import dataclass, field
from typing import List

from ..base import AggregateRoot, AssertionConcern
from ..value_objects import OrderStatus
from .customer import Customer
from .order_item import OrderItem


@dataclass(kw_only=True)
class Order(AggregateRoot):
    """Represents an order in the system."""

    customer: Customer
    _items: List[OrderItem] = field(default_factory=list)
    _total_value: float = field(default=0.0)
    _status: OrderStatus = field(default_factory=lambda: OrderStatus.PENDING)

    def __post_init__(self) -> None:
        self._total_value = sum(item.unit_price * item.quantity for item in self._items)

    @property
    def status(self) -> OrderStatus:  # noqa: D102
        return self._status

    @property
    def total_value(self) -> float:  # noqa: D102
        return self._total_value

    @property
    def items(self) -> List[OrderItem]:  # noqa: D102
        return [*self._items]

    def add_item(self, new_item: OrderItem) -> None:
        """Adds an item to the order and invalidates the total_value cache."""
        for item in self._items:
            if item.product == new_item.product:
                item.quantity += new_item.quantity
                self._total_value += new_item.unit_price * new_item.quantity
                break
        else:
            self._items.append(new_item)
            self._total_value += new_item.unit_price * new_item.quantity

    def add_items(self, items: List[OrderItem]) -> None:
        """Adds multiple items to the order and invalidates the total_value cache."""
        for item in items:
            self.add_item(item)

    def remove_item(self, item: OrderItem) -> None:
        """Removes an item from the order and invalidates the total_value cache."""
        self._items.remove(item)
        self._total_value -= item.unit_price * item.quantity

    def update_status(self, new_status: OrderStatus) -> None:
        """Updates the status of the order.

        Args:
            new_status: The new status of the order.

        Raises:
            InvalidOrderStatusError: If the new status is invalid.
        """
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

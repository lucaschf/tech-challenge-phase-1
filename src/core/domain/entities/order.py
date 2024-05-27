from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4

from src.core.domain.base import AggregateRoot, AssertionConcern
from src.core.domain.entities.order_product import OrderProduct
from src.core.domain.exceptions.order_status_error import InvalidOrderStatusError
from src.core.domain.value_objects.order_status import OrderStatus


@dataclass(kw_only=True)
class Order(AggregateRoot):
    """Represents an order in the system.

    Attributes:
    user_uuid: The UUID of the user who placed the order.
    products: The list of products in the order.
    status: OrderStatus
    created_at: The timestamp when the order was created.
    updated_at: The timestamp when the order was last updated.
    """

    user_uuid: UUID
    products: List[OrderProduct]
    status: OrderStatus = field(default_factory=lambda: OrderStatus("pending"))
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = field(default=None)
    uuid: UUID = field(default_factory=uuid4)

    def validate(self) -> None:
        """Validates the order's attributes.

        This method checks if the user_uuid, products, and status are valid.
        If any of these conditions are not met, a DomainError will be raised with a relevant message.

        Raises:
            DomainError: If any of the order's attributes are invalid.
        """
        AssertionConcern.assert_argument_not_null(self.user_uuid, "User uuid is required")
        AssertionConcern.assert_argument_not_null(self.products, "Products are required")
        if isinstance(self.products, (list, tuple)):
            AssertionConcern.assert_argument_not_empty(self.products, "Products are required")
        AssertionConcern.assert_argument_not_null(self.status, "Status is required")
        AssertionConcern.assert_argument_in_set(
            self.status.status, OrderStatus.ALLOWED_STATUSES, "Invalid order status"
        )

    def update_status(self, new_status: str) -> None:
        """Updates the status of the order.

        Args:
            new_status (str): The new status of the order.

        Raises:
            InvalidOrderStatusError: If the new status is invalid.
        """
        if not OrderStatus._is_valid(new_status):
            raise InvalidOrderStatusError(status=new_status)
        self.status = OrderStatus(new_status)


__all__ = ["Order"]

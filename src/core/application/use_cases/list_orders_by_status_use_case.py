from typing import List

from src.core.domain.entities.order import Order
from src.core.domain.repositories.order_repository import OrderRepository


class ListOrdersByStatusUseCase:
    """Use case for listing orders by status order."""

    def __init__(self, repository: OrderRepository) -> None:
        """Initializes a new instance of the ListOrdersByStatusUseCase class.

        Args:
            repository (OrderRepository): The repository instance for order persistence operations.
        """
        self.repository = repository

    def list_orders_sorted_by_status(self) -> List[Order]:
        """Retrieves orders sorted by a custom status order: READY, PREPARING, RECEIVED and sorted py the creation date.

        Returns:
            List[Order]: List of orders sorted by custom status order and .
        """
        statuses = ["ready", "preparing", "received"]
        orders = self.repository.list_orders_sorted_by_status(statuses)
        custom_order = {"ready": 1, "preparing": 2, "received": 3}
        return sorted(
            orders, key=lambda order: (custom_order.get(order.status.status, 999), order.created_at)
        )

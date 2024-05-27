from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from src.core.domain.entities.order import Order
from src.core.domain.value_objects.order_status import OrderStatus


class OrderRepository(ABC):
    """OrderRepository is an abstract base class that defines the contract for order persistence operations.

    This class outlines the methods that any concrete implementation of an order repository must provide.
    """

    @abstractmethod
    def create(self, order: Order) -> Order:
        """Persists a new order in the repository.

        Args:
            order (Order): The order to be created.

        Returns:
            Order: The created order with its uuid and other persistence details populated.
        """
        pass

    @abstractmethod
    def update_status(self, order_uuid: UUID, status: OrderStatus) -> Order:
        """Updates the status of an existing order in the repository.

        Args:
            order_uuid (UUID): The uuid of the order to be updated.
            status (OrderStatus): The new status for the order.

        Returns:
            Order: The updated order.
        """
        pass

    @abstractmethod
    def list_all(self) -> List[Order]:
        """Retrieves all orders from the repository.

        Returns:
            List[Order]: A list of all orders.
        """
        pass

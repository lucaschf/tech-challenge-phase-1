from abc import ABC, abstractmethod

from src.core.application.dto import OrderInputDTO
from src.core.domain.entities.order import Order


class OrderUseCase(ABC):
    """Interface for the OrderUseCase class."""

    @abstractmethod
    def create_order(self, order_data: OrderInputDTO) -> Order:
        """Create a new order in the system.

        Args:
            order_data: The order data.

        Returns:
            Order: An Order object representing the newly created order.
        """

    @abstractmethod
    def get_orders(self) -> list[Order]:
        """Get all orders in the system.

        Returns:
            list[Order]: A list of Order objects.
        """


__all__ = ["OrderUseCase"]

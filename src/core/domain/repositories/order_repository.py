from abc import ABC, abstractmethod

from src.core.domain.entities.order import Order


class OrderRepository(ABC):
    """Repository for handling orders persistence."""

    @abstractmethod
    def add(self, order: Order) -> Order:
        """Add a new order to the database.

        Args:
            order: The order data.

        Returns:
            Order: The added order data.
        """

    @abstractmethod
    def get_all(self) -> list[Order]:
        """Get all orders in the database.

        Returns:
            list[Order]: A list of Order objects.
        """


__all__ = ["OrderRepository"]

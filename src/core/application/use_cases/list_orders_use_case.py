from typing import List

from src.core.domain.entities.order import Order
from src.core.domain.repositories.order_repository import OrderRepository


class ListOrdersUseCase:
    """ListOrdersUseCase encapsulates the business logic for retrieving orders."""

    def __init__(self, repository: OrderRepository) -> None:
        """Initializes a new instance of the ListOrdersUseCase class.

        Args:
            repository (OrderRepository): The repository instance for order persistence operations.
        """
        self.repository = repository

    def list_orders(self) -> List[Order]:
        """Retrieves all orders.

        Returns:
            List[Order]: A list of all orders.
        """
        return self.repository.list_all()

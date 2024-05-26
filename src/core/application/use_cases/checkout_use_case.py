from typing import List
from uuid import UUID

from src.core.domain.entities.order import Order, OrderProduct
from src.core.domain.repositories.order_repository import OrderRepository


class CheckoutUseCase:
    """CheckoutUseCase encapsulates the business logic for creating orders."""

    def __init__(self, repository: OrderRepository) -> None:
        """Initializes a new instance of the CheckoutUseCase class.

        Args:
            repository (OrderRepository): The repository instance for order persistence operations.
        """
        self.repository = repository

    def checkout(self, user_id: UUID, products: List[OrderProduct]) -> Order:
        """Creates a new order.

        Args:
            user_id (UUID): The ID of the user making the order.
            products (List[OrderProduct]): The list of products in the order.

        Returns:
            Order: The created order with its ID and other persistence details populated.
        """
        order = Order(user_id=user_id, products=products)
        return self.repository.create(order)

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

    def checkout(self, user_uuid: UUID, products: List[OrderProduct]) -> Order:
        """Creates a new order.

        Args:
            user_uuid (UUID): The uuid of the user making the order.
            products (List[OrderProduct]): The list of products in the order.

        Returns:
            Order: The created order with its uuid and other persistence details populated.
        """
        order = Order(user_uuid=user_uuid, products=products)
        return self.repository.create(order)

from dataclasses import dataclass
from typing import List
from uuid import UUID

from src.core.domain.entities import Order, OrderItem
from src.core.domain.exceptions import CustomerNotFoundError, ProductNotFoundError
from src.core.domain.repositories import CustomerRepository, OrderRepository
from src.core.domain.repositories.product_repository import ProductRepository
from src.core.domain.value_objects import CPF


@dataclass
class OrderItemDTO:
    """OrderItemDTO represents the data transfer object for an order item."""

    product_uuid: UUID
    quantity: int


class CheckoutUseCase:
    """CheckoutUseCase encapsulates the business logic for creating orders."""

    def __init__(
        self,
        order_repository: OrderRepository,
        customer_repository: CustomerRepository,
        product_repository: ProductRepository,
    ) -> None:
        """Initializes a new instance of the CheckoutUseCase class.

        Args:
            order_repository: The repository instance for order persistence operations.
            customer_repository: The repository instance for customer persistence operations.
            product_repository: The repository instance for product persistence operations.
        """
        self._order_repository = order_repository
        self._customer_repository = customer_repository
        self._product_repository = product_repository

    def checkout(self, customer_cpf: CPF, items: List[OrderItemDTO]) -> Order:
        """Creates a new order.

        Args:
            customer_cpf: The CPF of the customer.
            items: The list of items to be added to the order.

        Returns:
            Order: The created order with its uuid and other persistence details populated.
        """
        customer = self._customer_repository.get_by_cpf(customer_cpf)
        if not customer:
            raise CustomerNotFoundError(customer_cpf.number)

        products = self._product_repository.get_by_uuids({item.product_uuid for item in items})
        order_items = []
        for item_in in items:
            product = next((p for p in products if p.uuid == item_in.product_uuid), None)
            if not product:
                raise ProductNotFoundError(search_param=item_in.product_uuid.hex)

            order_items.append(
                OrderItem(product=product, quantity=item_in.quantity, unit_price=product.price)
            )

        order = Order(customer=customer, _items=order_items)

        return self._order_repository.create(order)


__all__ = ["CheckoutUseCase", "OrderItemDTO"]

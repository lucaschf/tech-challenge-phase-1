from typing import Iterable

from src.core.domain.repositories.order_repository import OrderRepository

from ..shared_dtos import CustomerSummaryResult, OrderItemResult, OrderResult


class ListOrdersUseCase:
    """ListOrdersUseCase encapsulates the business logic for retrieving orders."""

    def __init__(self, repository: OrderRepository) -> None:
        """Initializes a new instance of the ListOrdersUseCase class.

        Args:
            repository (OrderRepository): The repository instance for order persistence operations.
        """
        self.repository = repository

    def list_orders(self) -> Iterable[OrderResult]:
        """Retrieves all orders.

        Returns:
            An iterable of all orders.
        """
        orders = self.repository.list_all()
        return [
            OrderResult(
                uuid=order.uuid,
                status=order.status,
                total_value=order.total_value,
                created_at=order.created_at,
                updated_at=order.updated_at,
                customer=CustomerSummaryResult(
                    name=order.customer.name,
                    email=str(order.customer.email),
                    cpf=str(order.customer.cpf),
                ),
                items=[
                    OrderItemResult(
                        product_name=item.product.name,
                        quantity=item.quantity,
                        unit_price=item.unit_price,
                    )
                    for item in order.items
                ],
            )
            for order in orders
        ]


__all__ = ["ListOrdersUseCase"]

from typing import Iterable

from src.core.domain.repositories.order_repository import OrderRepository

from ..shared_dtos import CustomerSummaryResult, OrderItemResult, OrderResult


class ListOrdersByStatusUseCase:
    """Use case for listing orders by status order."""

    def __init__(self, repository: OrderRepository) -> None:
        """Initializes a new instance of the ListOrdersByStatusUseCase class.

        Args:
            repository (OrderRepository): The repository instance for order persistence operations.
        """
        self.repository = repository

    def list_orders_sorted_by_status(self) -> Iterable[OrderResult]:
        """Retrieves orders sorted by a custom status order: READY, PREPARING, RECEIVED and sorted py the creation date.

        Returns:
            List[Order]: List of orders sorted by custom status order and .
        """
        orders = self.repository.list_all()

        status_order = {"ready": 1, "preparing": 2, "received": 3}

        # Filter orders to include only those with statuses READY, PREPARING, RECEIVED
        filtered_orders = [order for order in orders if order.status in status_order]

        # Sort orders based on the defined order of statuses
        sorted_orders = sorted(
            filtered_orders, key=lambda order: (status_order[order.status], order.created_at)
        )

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
            for order in sorted_orders
        ]


__all__ = ["ListOrdersByStatusUseCase"]

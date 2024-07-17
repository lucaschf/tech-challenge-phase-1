from uuid import UUID

from src.core.domain.exceptions import OrderNotFoundError
from src.core.domain.repositories.order_repository import OrderRepository
from src.core.domain.value_objects.order_status import OrderStatus

from ..shared_dtos import CustomerSummaryResult, OrderItemResult, OrderResult


class UpdateOrderStatusUseCase:
    """UpdateOrderStatusUseCase encapsulates the business logic for updating order status."""

    def __init__(self, repository: OrderRepository) -> None:
        """Initializes a new instance of the UpdateOrderStatusUseCase class.

        Args:
            repository (OrderRepository): The repository instance for order persistence operations.
        """
        self.repository = repository

    def update_status(self, order_uuid: UUID, status: OrderStatus) -> OrderResult:
        """Updates the status of an existing order.

        Args:
            order_uuid: The uuid of the order to be updated.
            status: The new status for the order.

        Returns:
            Order: The updated order.
        """
        order = self.repository.get_by_uuid(order_uuid)

        if not order:
            raise OrderNotFoundError(order_uuid)

        order = self.repository.update_status(order_uuid, status)
        return OrderResult(
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


__all__ = ["UpdateOrderStatusUseCase"]

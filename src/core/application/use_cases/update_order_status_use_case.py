from uuid import UUID

from src.core.domain.entities.order import Order
from src.core.domain.repositories.order_repository import OrderRepository
from src.core.domain.value_objects.order_status import OrderStatus


class UpdateOrderStatusUseCase:
    """UpdateOrderStatusUseCase encapsulates the business logic for updating order status."""

    def __init__(self, repository: OrderRepository) -> None:
        """Initializes a new instance of the UpdateOrderStatusUseCase class.

        Args:
            repository (OrderRepository): The repository instance for order persistence operations.
        """
        self.repository = repository

    def update_status(self, order_uuid: UUID, status: OrderStatus) -> Order:
        """Updates the status of an existing order.

        Args:
            order_uuid (UUID): The uuid of the order to be updated.
            status (OrderStatus): The new status for the order.

        Returns:
            Order: The updated order.
        """
        return self.repository.update_status(order_uuid, status)

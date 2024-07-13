from typing import List
from uuid import UUID

from src.adapter.driver.api.schemas.order_schema import OrderIn, OrderOut, OrderStatusUpdate
from src.core.application.use_cases import (
    CheckoutUseCase,
    ListOrdersUseCase,
    UpdateOrderStatusUseCase,
)
from src.core.application.use_cases.checkout_use_case import OrderItemDTO
from src.core.domain.value_objects import CPF


class OrderController:
    """This class manages order-related actions using different use cases.

    The class acts as the intersection between the API and the business logic,
    handling HTTP requests related to order data.
    """

    def __init__(
        self,
        checkout_use_case: CheckoutUseCase,
        list_orders_use_case: ListOrdersUseCase,
        update_order_status_use_case: UpdateOrderStatusUseCase,
    ) -> None:
        self.checkout_use_case = checkout_use_case
        self.list_orders_use_case = list_orders_use_case
        self.update_order_status_use_case = update_order_status_use_case

    def checkout(self, order_in: OrderIn) -> OrderOut:
        """Registers a new order in the system from the provided order data."""
        order_items_dto = [
            OrderItemDTO(product_uuid=item.product_uuid, quantity=item.quantity)
            for item in order_in.items
        ]
        order = self.checkout_use_case.checkout(
            CPF(order_in.customer_cpf),
            order_items_dto,
        )
        return OrderOut.from_entity(order)

    def list_orders(self) -> List[OrderOut]:
        """Get a list of orders in the system."""
        orders = self.list_orders_use_case.list_orders()
        return [OrderOut.from_entity(order) for order in orders]

    def update_status(self, order_uuid: UUID, status_update: OrderStatusUpdate) -> OrderOut:
        """Update the status of an order in the system from the provided order ID and status."""
        order = self.update_order_status_use_case.update_status(order_uuid, status_update.status)
        return OrderOut.from_entity(order)


__all__ = ["OrderController"]

from typing import Iterable
from uuid import UUID

from src.core.use_cases import (
    CheckoutUseCase,
    ListOrdersUseCase,
    UpdateOrderStatusUseCase,
)

from ...core.use_cases.order import OrderResult
from ..presenters import Presenter
from ..schemas.order_schema import (
    OrderCreationOut,
    OrderIn,
    OrderOut,
    OrderStatusUpdateIn,
)


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
        order_created_presenter: Presenter[OrderCreationOut, OrderResult],
        order_details_presenter: Presenter[OrderOut, OrderResult],
    ) -> None:
        self._checkout_use_case = checkout_use_case
        self._list_orders_use_case = list_orders_use_case
        self._update_order_status_use_case = update_order_status_use_case
        self._order_created_presenter = order_created_presenter
        self._order_details_presenter = order_details_presenter

    def checkout(self, order_in: OrderIn) -> OrderCreationOut:
        """Registers a new order in the system from the provided order data."""
        order = self._checkout_use_case.checkout(order_in.to_checkout_request())
        return self._order_created_presenter.present(order)

    def list_orders(self) -> Iterable[OrderOut]:
        """Get a list of orders in the system."""
        orders = self._list_orders_use_case.list_orders()
        return self._order_details_presenter.present_many(orders)

    def update_status(self, order_uuid: UUID, status_update: OrderStatusUpdateIn) -> OrderOut:
        """Update the status of an order in the system from the provided order ID and status."""
        order = self._update_order_status_use_case.update_status(order_uuid, status_update.status)
        return self._order_details_presenter.present(order)


__all__ = ["OrderController"]

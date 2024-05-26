from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends

from src.adapter.driver.api.controllers.order_controller import OrderController
from src.adapter.driver.api.dependencies import injector
from src.adapter.driver.api.schemas.order_schema import OrderIn, OrderOut, OrderStatusUpdate

router = APIRouter(tags=["Order"])


@router.post("/checkout", response_model=OrderOut)
def checkout(
    order_in: OrderIn,
    controller: OrderController = Depends(lambda: injector.get(OrderController)),  # noqa: B008
) -> OrderOut:
    """Process a fake checkout by adding selected products to the order queue."""
    order = controller.checkout(order_in.products, order_in.user_id)
    return OrderOut.from_entity(order)


@router.get("/orders", response_model=List[OrderOut])
def list_orders(
    controller: OrderController = Depends(lambda: injector.get(OrderController)),  # noqa: B008
) -> List[OrderOut]:
    """List all orders."""
    orders = controller.list_orders()
    return [OrderOut.from_entity(order) for order in orders]


@router.put("/orders/{order_id}/status", response_model=OrderOut)
def update_order_status(
    order_id: UUID,
    status_update: OrderStatusUpdate,
    controller: OrderController = Depends(lambda: injector.get(OrderController)),  # noqa: B008
) -> OrderOut:
    """Update the status of an existing order."""
    order = controller.update_status(order_id, status_update.status)
    return OrderOut.from_entity(order)

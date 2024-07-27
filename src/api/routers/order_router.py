from http import HTTPStatus
from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends

from ..controllers.order_controller import OrderController
from ..dependencies import injector
from ..schemas.order_schema import (
    OrderCreationOut,
    OrderIn,
    OrderOut,
    OrderStatusUpdateIn,
)

router = APIRouter(tags=["Order"], prefix="/orders")


@router.post("/checkout", response_model=OrderCreationOut, status_code=HTTPStatus.CREATED)
def checkout(
    order_in: OrderIn,
    controller: OrderController = Depends(lambda: injector.get(OrderController)),  # noqa: B008
) -> OrderCreationOut:
    """Process a fake checkout by adding selected products to the order queue."""
    return controller.checkout(order_in)


@router.get("/", response_model=List[OrderOut])
def list_orders(
    controller: OrderController = Depends(lambda: injector.get(OrderController)),  # noqa: B008
) -> List[OrderOut]:
    """List all orders."""
    return controller.list_orders()


@router.get("/orders-sorted-by-status", response_model=List[OrderOut])
def list_orders_sorted_by_status(
    controller: OrderController = Depends(lambda: injector.get(OrderController)),  # noqa: B008
) -> List[OrderOut]:
    """List orders ordered by status."""
    return controller.list_orders_sorted_by_status()


@router.put("/{order_uuid}/status", response_model=OrderOut)
def update_order_status(
    order_uuid: UUID,
    status_update: OrderStatusUpdateIn,
    controller: OrderController = Depends(lambda: injector.get(OrderController)),  # noqa: B008
) -> OrderOut:
    """Update the status of an existing order."""
    return controller.update_status(order_uuid, status_update)

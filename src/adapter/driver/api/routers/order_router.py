from http import HTTPStatus

from fastapi import APIRouter, Depends, Response

from ..controllers.order_controller import OrderController
from ..dependencies import injector
from ..schemas import OrderCreationIn, OrderOut
from ..schemas.http_error import HttpErrorOut

router = APIRouter(tags=["Order"], prefix="/order")


@router.post(
    "/",
    status_code=HTTPStatus.CREATED,
    responses={400: {"model": HttpErrorOut}},
    description="Creates a new order in the system.",
)
def create_order(
    response: Response,
    inputs: OrderCreationIn,
    controller: OrderController = Depends(  # noqa: B008
        lambda: injector.get(OrderController)
    ),
) -> OrderOut:
    order = controller.create_order(inputs)
    response.headers["Location"] = f"{router.prefix}/{order.uuid}"
    return order


@router.get(
    "/",
    status_code=HTTPStatus.OK,
    responses={400: {"model": HttpErrorOut}},
    description="Get all orders in the system.",
)
def get_orders(
    controller: OrderController = Depends(  # noqa: B008
        lambda: injector.get(OrderController)
    ),
) -> list[OrderOut]:
    return controller.get_orders()


__all__ = ["router"]

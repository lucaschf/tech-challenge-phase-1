from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Depends

from src.api.controllers import PaymentConfirmationController
from src.api.dependencies import injector
from src.api.schemas import PaymentConfirmationIn

router = APIRouter(tags=["Payment Webhook"], prefix="/payment")


@router.post("/{payment_id}/result", status_code=HTTPStatus.NO_CONTENT)
def update_status(  # noqa: D103
    payment_id: UUID,
    data: PaymentConfirmationIn,
    controller: PaymentConfirmationController = Depends(  # noqa: B008
        lambda: injector.get(PaymentConfirmationController)
    ),
) -> None:
    return controller.update_payment_satus(payment_id, data)

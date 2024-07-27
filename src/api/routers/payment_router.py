from src.core.domain.repositories.payment_repository import PaymentRepository
from src.core.domain.entities.payment import Payment , PaymentStatus
from src.api.controllers.payment_controller import PaymentController
from uuid import UUID

from fastapi import APIRouter , Depends 
from ..dependencies import injector
from ..schemas.http_error import HttpErrorOut

router = APIRouter(tags=["Payment"], prefix="/payment")


@router.get(
        "/{payment}/status", 
        responses={404: {"model": HttpErrorOut}, 400: {"model": HttpErrorOut}},
        description="Retrieves a payment status from the system using the payment_uuid."
        "The payment_uuid is passed as a path "
        "parameter.",
)
def get_payment_status(
    order_uuid: UUID,
    controller: PaymentController = Depends(
        lambda: injector.get(PaymentController
    ),
)) -> PaymentStatus | None:
    return controller.get_payment_status(order_uuid)

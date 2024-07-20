from http import HTTPStatus

from fastapi import APIRouter

router = APIRouter(tags=["Payment"], prefix="/payment")


@router.post("/{payment_id}/result", status_code=HTTPStatus.NO_CONTENT)
async def request_payment():
    """Request payment from the user."""
    pass

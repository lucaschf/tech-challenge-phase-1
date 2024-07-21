from uuid import UUID

from src.api.schemas import PaymentConfirmationIn
from src.core.domain.entities.payment import PaymentStatus
from src.core.use_cases import PaymentConfirmationUseCase


class PaymentConfirmationController:
    """Dumb controller for updating payment status.

    It should be responsible for converting the incoming data and passing it to the use case.
    """

    def __init__(
        self,
        use_case: PaymentConfirmationUseCase,
    ) -> None:
        self._use_case = use_case

    def update_payment_satus(  # noqa: D102
        self, payment_id: UUID, data: PaymentConfirmationIn
    ) -> None:
        # Here we would need to convert the incoming data.
        self._use_case.execute(payment_id, PaymentStatus(data.status))


__all__ = ["PaymentConfirmationController"]

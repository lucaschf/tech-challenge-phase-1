from uuid import UUID

from src.core.domain.entities.payment import Payment, PaymentStatus
from src.core.domain.exceptions import PaymentNotFoundError
from src.core.domain.repositories import PaymentRepository
from src.core.domain.value_objects import OrderStatus

from .update_order_status_use_case import UpdateOrderStatusUseCase


class PaymentConfirmationUseCase:
    """Use-case for confirming payment status and updating order status accordingly."""

    def __init__(
        self,
        payment_repo: PaymentRepository,
        update_order_status_use_case: UpdateOrderStatusUseCase,
    ) -> None:
        self._payment_repo = payment_repo
        self._update_order_status_use_case = update_order_status_use_case

    def execute(self, payment_uuid: UUID, payment_status: PaymentStatus) -> Payment:
        """Executes the payment confirmation process.

        Args:
            payment_uuid: UUID of the payment to confirm.
            payment_status: New status of the payment.

        Returns:
            Updated payment entity.

        Raises:
             PaymentNotFoundError: If the payment does not exist.
        """
        payment = self._payment_repo.get_by_uuid(payment_uuid)
        if not payment:
            raise PaymentNotFoundError(search_params={"uuid": payment_uuid})

        payment.update_status(payment_status)
        self._payment_repo.update_status(payment.id, payment_status)

        if payment_status == PaymentStatus.APPROVED:
            self._update_order_status_use_case.update_status(
                payment.order.uuid, OrderStatus.RECEIVED
            )

        return self._payment_repo.get_by_uuid(payment_uuid)


__all__ = ["PaymentConfirmationUseCase"]

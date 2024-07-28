from uuid import UUID

from src.core.domain.exceptions import PaymentNotFoundError
from src.core.domain.repositories import PaymentRepository

from ..shared_dtos import PaymentResult


class GetPaymentStatusUseCase:
    """A use case for getting a payment status by their Order UUID."""

    def __init__(self, payment_repository: PaymentRepository) -> None:
        self.payment_repository = payment_repository

    def execute(self, order_uuid: UUID) -> PaymentResult:
        """Get a payment status by their Order UUID.

        Args:
            order_uuid: The order uuid.

        Returns:
            PaymentStatus: The payment status if found.

        Raises:
            PaymentStatusNotFoundError: If the customer is not found.
        """
        payment = self.payment_repository.get_payment_details(order_uuid)

        if not payment:
            raise PaymentNotFoundError(search_params={"order_uuid": order_uuid})

        return PaymentResult(payment.uuid, payment.status)


__all__ = ["GetPaymentStatusUseCase"]

from src.core.domain.entities import Order
from src.core.domain.repositories import PaymentRepository
from src.payment import IPaymentGateway


class PaymentProcessingUseCase:
    """Use-case for processing payments."""

    def __init__(
        self, payment_gateway: IPaymentGateway, payment_repository: PaymentRepository
    ) -> None:
        self._payment_gateway = payment_gateway
        self._payment_repository = payment_repository

    def process_payment(self, order: Order) -> Order:
        """Processes the payment for the given order."""
        payment = self._payment_gateway.process(order)
        self._payment_repository.add(payment)

        return order


__all__ = ["PaymentProcessingUseCase"]

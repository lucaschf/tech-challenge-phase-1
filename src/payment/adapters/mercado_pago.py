from src.core.domain.entities import Order, Payment
from src.core.domain.entities.payment import PaymentStatus

from ..payment_gateway import IPaymentGateway


class MercadoPagoGateway(IPaymentGateway):
    """A payment gateway implementation for MercadoPago."""

    def process(self, order: Order) -> Payment:
        """Processes a payment for the given order."""
        # Here we would call the MercadoPago API to create a payment
        return Payment(
            status=PaymentStatus.PENDING,
            order=order,
            details={
                "gateway": "MercadoPago",
            },
        )


__all__ = ["MercadoPagoGateway"]

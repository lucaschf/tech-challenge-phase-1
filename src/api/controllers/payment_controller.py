from src.core.use_cases.payment.find.get_payment_status_use_case import GetPaymentStatusUseCase
from src.core.domain.entities.payment import PaymentStatus
from uuid import UUID

class PaymentController:
    """This class manages payment-related actions using different use cases.

    The class acts as the intersection between the API and the business logic,
    handling HTTP requests related to order data."""


    def __init__(
            self,
            get_payment_status_use_case: GetPaymentStatusUseCase,
    ) -> None:
        self._get_payment_status_use_case = get_payment_status_use_case
    

    def get_payment_status(self, order_uuid: UUID) -> PaymentStatus:
        """Get the status of an payment in the system from the provided order ID."""
        return self._get_payment_status_use_case.execute(order_uuid).payment_status

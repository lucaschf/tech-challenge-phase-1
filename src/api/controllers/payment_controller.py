from uuid import UUID

from src.api.presenters import Presenter
from src.api.schemas import PaymentSummaryOut
from src.core.use_cases import GetPaymentStatusUseCase
from src.core.use_cases.payment.shared_dtos import PaymentResult


class PaymentController:
    """This class manages payment-related actions using different use cases.

    The class acts as the intersection between the API and the business logic,
    handling HTTP requests related to order data.
    """

    def __init__(
        self,
        get_payment_status_use_case: GetPaymentStatusUseCase,
        payment_summary_presenter: Presenter[PaymentSummaryOut, PaymentResult],
    ) -> None:
        self._get_payment_status_use_case = get_payment_status_use_case
        self._payment_summary_presenter = payment_summary_presenter

    def get_payment_status(self, order_uuid: UUID) -> PaymentSummaryOut:
        """Get the status of a payment in the system from the provided order ID."""
        payment = self._get_payment_status_use_case.execute(order_uuid)
        return self._payment_summary_presenter.present(payment)


__all__ = ["PaymentController"]

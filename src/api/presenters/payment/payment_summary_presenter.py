from src.core.use_cases.payment.shared_dtos import PaymentResult

from ...schemas import PaymentSummaryOut
from ..presenter import Presenter


class PaymentSummaryPresenter(Presenter[PaymentSummaryOut, PaymentResult]):
    """Presenter for the product details."""

    def present(self, data: PaymentResult) -> PaymentSummaryOut:
        """Converts the CustomerResult instance into a CustomerDetailsOut instance."""
        return PaymentSummaryOut(
            number=data.number,
            status=data.status,
        )


__all__ = ["PaymentSummaryPresenter"]

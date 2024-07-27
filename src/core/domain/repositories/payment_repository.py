from abc import ABC, abstractmethod
from uuid import UUID

from src.core.domain.entities import Payment
from src.core.domain.entities.payment import PaymentStatus


class PaymentRepository(ABC):
    """Repository for handling payment persistence."""

    @abstractmethod
    def get_by_uuid(self, uuid: UUID) -> Payment | None:
        """Get a payment by its UUID.

        Args:
            uuid: The payment's UUID.

        Returns:
            Payment: The payment data if found, None otherwise.
        """
    
    @abstractmethod
    def get_payment_status(self, order_uuid: UUID) -> PaymentStatus | None:
        """Get a payment status by Order UUID.
        
        Args:
            uuid: The order's UUID.
            
        Returns:
            Payment Status if found, None otherwise."""

    @abstractmethod
    def add(self, payment: Payment) -> Payment:
        """Add a new payment to the database.

        Args:
        payment: The payment data.

        Returns:
        Payment: The added payment data.
        """

    @abstractmethod
    def update_status(self, payment_id: int, status: PaymentStatus) -> Payment | None:
        """Update the status of an existing payment.

        Args:
            payment_id: The id of the payment to be updated.
            status: The new status for the payment.

        Returns:
            Payment: The updated payment data if found, None otherwise.
        """


__all__ = ["PaymentRepository"]

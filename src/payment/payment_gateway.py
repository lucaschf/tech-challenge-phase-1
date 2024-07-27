from abc import ABC, abstractmethod

from src.core.domain.entities import Order
from src.core.domain.entities.payment import Payment


class IPaymentGateway(ABC):
    """Interface for payment gateway implementations."""

    @abstractmethod
    def process(self, order: Order) -> Payment:
        """Processes a payment for the given order."""
        pass


__all__ = ["IPaymentGateway"]

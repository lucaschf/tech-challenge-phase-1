from dataclasses import dataclass
from uuid import UUID

from src.core.domain.entities.payment import PaymentStatus


@dataclass
class PaymentResult:
    """Data structure for holding data of a Payment status.

    Attributes:
    payment_status: Enum with Payment Status
    """

    number: UUID
    status: PaymentStatus


__all__ = ["PaymentResult"]

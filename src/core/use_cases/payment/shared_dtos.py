from dataclasses import dataclass

from src.core.domain.entities.payment import PaymentStatus

@dataclass
@dataclass
class PaymentResult:
    """Data structure for holding data of a Payment status
    
    Attributes:
        payment_status: Enum with Payment Status"""
    payment_status: PaymentStatus


__all__ = ["PaymentResult"]

from enum import StrEnum, auto


class PaymentMethod(StrEnum):
    """Represents the payment methods available in the system."""

    MERCADO_PAGO = auto()
    CASH = auto()


__all__ = ["PaymentMethod"]

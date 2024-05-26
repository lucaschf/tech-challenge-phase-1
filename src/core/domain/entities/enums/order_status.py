from enum import StrEnum, auto


class OrderStatus(StrEnum):
    """Order's status."""

    CREATED = auto()
    CONFIRMED = auto()
    IN_PREPARATION = auto()
    READY_FOR_DELIVERY = auto()
    PAID = auto()
    DELIVERED = auto()
    CANCELED = auto()


__all__ = ["OrderStatus"]

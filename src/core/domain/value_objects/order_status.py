from enum import StrEnum, auto
from typing import List


class OrderStatus(StrEnum):
    """An Enum that represents an Order Status."""

    PAYMENT_PENDING = auto()
    PROCESSING = auto()
    READY = auto()
    RECEIVED = auto()
    COMPLETED = auto()
    CANCELED = auto()

    @classmethod
    def values(cls) -> List["OrderStatus"]:
        """Return a list of OrderStatus values."""
        return [cls[member] for member in cls.__members__]


__all__ = ["OrderStatus"]

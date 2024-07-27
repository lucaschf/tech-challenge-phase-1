from typing import Iterable
from uuid import UUID

from src.core.domain.base import DomainError


class EmptyOrderError(DomainError):
    """Exception raised when an order is created without any items."""

    def __init__(self, message: str = "Order must contain at least one item.") -> None:
        super().__init__(message)


class OrderCreationFailedDueToMissingProductsError(DomainError):
    """Exception raised when an order cannot be created due to missing products."""

    def __init__(self, missing_product_uuids: Iterable[UUID]) -> None:
        self.missing_product_uuids = missing_product_uuids
        message = (
            f"Order creation failed due to missing products: "
            f"{', '.join([uuid.hex for uuid in missing_product_uuids])}"
        )
        super().__init__(message)


__all__ = ["EmptyOrderError", "OrderCreationFailedDueToMissingProductsError"]

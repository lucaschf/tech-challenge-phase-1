from dataclasses import dataclass
from uuid import UUID

from src.core.domain.base import AssertionConcern


@dataclass(kw_only=True)
class OrderProduct:
    """Represents a product within an order.

    Attributes:
    product_id: The UUID of the product.
    quantity: The quantity of the product.
    """

    product_id: UUID
    quantity: int

    def validate(self) -> None:
        """Validates the order product's attributes.

        This method checks if the product_id and quantity are valid.
        If any of these conditions are not met, a DomainError will be raised with a relevant message.

        Raises:
            DomainError: If any of the order product's attributes are invalid.
        """
        AssertionConcern.assert_argument_not_null(self.product_id, "Product ID is required")
        AssertionConcern.assert_argument_greater_than_zero(
            self.quantity, "Quantity must be greater than zero"
        )


__all__ = ["OrderProduct"]

from dataclasses import dataclass

from src.core.domain.base import AggregateRoot, AssertionConcern

from .product import Product


@dataclass(kw_only=True)
class OrderItem(AggregateRoot):
    """Represents a product within an order.

    Attributes:
    product_uuid: The UUID of the product.
    quantity: The quantity of the product.
    """

    product: Product
    quantity: int
    unit_price: float

    def validate(self) -> None:
        """Validates the order product's attributes.

        This method checks if the product_uuid and quantity are valid.
        If any of these conditions are not met, a DomainError will be raised with a
            relevant message.

        Raises:
            DomainError: If any of the order product's attributes are invalid.
        """
        AssertionConcern.assert_argument_not_null(self.product, "Product is required")
        AssertionConcern.assert_argument_greater_than_zero(
            self.quantity, "Quantity must be greater than zero"
        )
        AssertionConcern.assert_argument_greater_than_or_equal_to_zero(
            self.unit_price, "Unit price must be greater than or equal to zero"
        )


__all__ = ["OrderItem"]

from dataclasses import dataclass, field

from src.core.domain.base import AggregateRoot, AssertionConcern

from .customer import Customer
from .enums import OrderStatus, PaymentMethod
from .product import Product


@dataclass(kw_only=True)
class OrderItem(AggregateRoot):
    """Represents an order item in the system."""

    product: Product
    quantity: int
    price: float

    def validate(self) -> None:  # noqa: D102
        AssertionConcern.assert_argument_greater_than_zero(
            self.quantity, "Quantity must be greater than zero"
        )


@dataclass(kw_only=True)
class Order(AggregateRoot):
    """Represents an order in the system."""

    customer: Customer
    items: list[OrderItem]
    status: OrderStatus = field(default=OrderStatus.CREATED)
    payment_method: PaymentMethod = field(default=PaymentMethod.MERCADO_PAGO)
    total_price: float = field(init=False)

    def __post_init__(self) -> None:
        super().__post_init__()
        self.total_price = sum(item.price * item.quantity for item in self.items)
        AssertionConcern.assert_argument_greater_than_zero(
            self.total_price, "Total price must be greater than zero"
        )

    def validate(self) -> None:  # noqa: D102
        AssertionConcern.assert_argument_not_empty(self.items, "Order must have items")
        AssertionConcern.assert_argument_not_null(self.customer, "Order must have a customer")


__all__ = ["Order", "OrderItem"]

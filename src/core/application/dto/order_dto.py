from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from src.core.domain.entities.enums import OrderStatus, PaymentMethod

from .customer_dto import CustomerOutputDTO
from .product_dto import ProductOutputDTO


@dataclass
class OrderItemInputDTO:
    """Data Transfer Object for order item input.

    Attributes:
        product_uuid: The UUID of the product.
        quantity: The quantity of the product.
    """

    product_uuid: UUID
    quantity: int


@dataclass
class OrderItemOutputDTO:
    """Data Transfer Object for order item output.

    Attributes:
        product: The product output data transfer object.
        quantity: The quantity of the product.
        price: The price of the product.
    """

    product: ProductOutputDTO
    quantity: int
    price: float


@dataclass
class OrderInputDTO:
    """Data Transfer Object for order input.

    Attributes:
        customer_cpf: The CPF of the customer.
        items: The list of order item input data transfer objects.
        payment_method: The payment method. Optional.
    """

    customer_cpf: str
    items: list[OrderItemInputDTO]
    payment_method: PaymentMethod | None = None


@dataclass
class OrderDTO:
    """Data Transfer Object for order.

    Attributes:
        id: The ID of the order.
        uuid: The UUID of the order.
        customer: The customer output data transfer object.
        items: The list of order item output data transfer objects.
        status: The status of the order.
        payment_method: The payment method. Optional.
        total_price: The total price of the order.
        created_at: The creation date and time of the order.
        updated_at: The update date and time of the order. Optional.
    """

    id: int
    uuid: UUID
    customer: CustomerOutputDTO
    items: list[OrderItemOutputDTO]
    status: OrderStatus
    payment_method: PaymentMethod | None
    total_price: float
    created_at: datetime
    updated_at: datetime | None


@dataclass
class OrderOutputDTO:
    """Data Transfer Object for order output.

    Attributes:
        uuid: The UUID of the order.
        customer: The customer output data transfer object.
        items: The list of order item output data transfer objects.
        status: The status of the order.
        payment_method: The payment method. Optional.
        total_price: The total price of the order.
        created_at: The creation date and time of the order.
        updated_at: The update date and time of the order. Optional.
    """

    uuid: UUID
    customer: CustomerOutputDTO
    items: list[OrderItemOutputDTO]
    status: OrderStatus
    payment_method: PaymentMethod | None
    total_price: float
    created_at: datetime
    updated_at: datetime | None


__all__ = ["OrderDTO", "OrderInputDTO", "OrderItemInputDTO", "OrderItemOutputDTO", "OrderOutputDTO"]

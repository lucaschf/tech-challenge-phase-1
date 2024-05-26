from uuid import UUID

from pydantic import BaseModel, Field

from src.core.application.dto import OrderInputDTO, OrderItemInputDTO
from src.core.domain.entities.enums import OrderStatus, PaymentMethod

from ..types import CPFStr
from .customer_schema import CustomerOut


class OrderItemIn(BaseModel):
    """Pydantic model for an order item input.

    Attributes:
        product_uuid: The UUID of the product.
        quantity: The quantity of the product. Must be greater than 0.
    """

    product_uuid: UUID
    quantity: int = Field(gt=0)


class OrderCreationIn(BaseModel):
    """Pydantic model for order creation input.

    Attributes:
        customer_cpf: The CPF of the customer.
        items: The list of order item inputs. Must have at least one item.
        payment_method: The payment method.
    """

    customer_cpf: CPFStr
    items: list[OrderItemIn] = Field(minlength=1)
    payment_method: PaymentMethod

    def to_order_input_dto(self) -> OrderInputDTO:
        """Converts this model to an OrderInputDTO.

        Returns:
        An OrderInputDTO with the same data as this model.
        """
        return OrderInputDTO(
            customer_cpf=self.customer_cpf,
            items=[
                OrderItemInputDTO(product_uuid=item.product_uuid, quantity=item.quantity)
                for item in self.items
            ],
            payment_method=self.payment_method,
        )


class OrderItemOut(BaseModel):
    """Pydantic model for an order item output.

    Attributes:
        quantity: The quantity of the product.
        price: The price of the product.
    """

    quantity: int
    price: float


class OrderOut(BaseModel):
    """Pydantic model for an order output.

    Attributes:
        uuid: The UUID of the order.
        customer: The customer output model.
        items: The list of order item outputs.
        status: The status of the order.
        payment_method: The payment method. Optional.
        total_price: The total price of the order.
    """

    uuid: UUID
    customer: CustomerOut  # You might want to include a simplified customer representation
    items: list[OrderItemOut]
    status: OrderStatus
    payment_method: PaymentMethod | None
    total_price: float


__all__ = ["OrderCreationIn", "OrderItemIn", "OrderItemOut", "OrderOut"]

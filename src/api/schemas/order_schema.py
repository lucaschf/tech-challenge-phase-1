from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from src.core.domain.entities import Order
from src.core.domain.value_objects import OrderStatus
from src.core.use_cases.checkout_use_case import CheckoutItem, CheckoutOrder

from ..types import CPFStr
from .customer_schema import CustomerSummaryOut
from .order_item_schema import OrderItemIn, OrderItemOut


class OrderIn(BaseModel):
    """Schema for creating a new order."""

    customer_id: UUID = Field(description="The customer identifier")
    items: List[OrderItemIn] = Field(description="List of products in the order")

    model_config = ConfigDict(str_strip_whitespace=True)

    def to_checkout_request(self) -> CheckoutOrder:
        """Converts the OrderIn instance to a CheckoutRequest instance."""
        return CheckoutOrder(
            customer_id=self.customer_id,
            items=[
                CheckoutItem(product_id=item.product_id, quantity=item.quantity)
                for item in self.items
            ],
        )


class OrderCreationOut(BaseModel):
    """Schema for returning the result of creating an order."""

    number: UUID = Field(description="The order number")


class OrderOut(BaseModel):
    """Schema for returning an order."""

    uuid: UUID = Field(description="The order external uuid")
    customer: CustomerSummaryOut = Field(description="The customer")
    items: List[OrderItemOut] = Field(description="List of items in the order")
    status: OrderStatus = Field(description="The order status")
    created_at: datetime = Field(description="The order creation date")
    updated_at: datetime = Field(description="The order last update date")
    total_value: float = Field(description="The total value of the order")

    # TODO: Remove this method from here. Move this to presenter layer.
    @staticmethod
    def from_entity(entity: Order) -> "OrderOut":
        """Creates an OrderOut instance from an Order entity."""
        return OrderOut(
            uuid=entity.uuid,
            customer=CustomerSummaryOut(
                name=entity.customer.name,
                email=str(entity.customer.email),
                cpf=CPFStr(str(entity.customer.cpf)),
            ),
            items=[OrderItemOut.from_entity(item) for item in entity.items],
            status=entity.status,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
            total_value=entity.total_value,
        )

    model_config = ConfigDict(str_strip_whitespace=True, arbitrary_types_allowed=True)


class OrderStatusUpdateIn(BaseModel):
    """Schema for updating the status of an order."""

    status: OrderStatus = Field(description="The new status of the order")


__all__ = [
    "OrderCreationOut",
    "OrderIn",
    "OrderOut",
    "OrderStatusUpdateIn",
]

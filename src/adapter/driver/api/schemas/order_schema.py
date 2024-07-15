from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field

from src.adapter.driver.api.types import CPFStr
from src.core.application.use_cases.checkout_use_case import CheckoutItem, CheckoutOrder
from src.core.domain.entities import Order, OrderItem
from src.core.domain.value_objects import Category, OrderStatus


class _BaseOrderItem(BaseModel):
    quantity: int = Field(description="The quantity of the product", gt=0)


class OrderItemIn(_BaseOrderItem):
    """Schema for creating a new order product."""

    product_id: UUID = Field(description="The product id")


class OrderItemOut(_BaseOrderItem):
    """Schema for returning an order product."""

    product: "ItemProductOut" = Field(description="The product")
    uuid: UUID = Field(description="The order product uuid")
    unit_price: float = Field(description="The unit price of the product")

    class ItemProductOut(BaseModel):
        """Schema for returning a product within an order item."""

        name: str
        category: Category
        description: str
        images: List[str]

    @staticmethod
    def from_entity(entity: OrderItem) -> "OrderItemOut":
        """Creates an OrderProductOut instance from an OrderProduct entity."""
        return OrderItemOut(
            product=OrderItemOut.ItemProductOut(
                name=entity.product.name,
                category=entity.product.category,
                description=entity.product.description,
                images=entity.product.images,
            ),
            uuid=entity.uuid,
            quantity=entity.quantity,
            unit_price=entity.unit_price,
        )


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


class OrderCustomerOut(BaseModel):
    """Schema for returning a customer within an order."""

    name: str
    email: EmailStr
    cpf: CPFStr


class OrderOut(BaseModel):
    """Schema for returning an order."""

    uuid: UUID = Field(description="The order external uuid")
    customer: OrderCustomerOut = Field(description="The customer")
    items: List[OrderItemOut] = Field(description="List of items in the order")
    status: OrderStatus = Field(description="The order status")
    created_at: datetime = Field(description="The order creation date")
    updated_at: datetime = Field(description="The order last update date")
    total_value: float = Field(description="The total value of the order")

    @staticmethod
    def from_entity(entity: Order) -> "OrderOut":
        """Creates an OrderOut instance from an Order entity."""
        return OrderOut(
            uuid=entity.uuid,
            customer=OrderCustomerOut(
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


class OrderStatusUpdate(BaseModel):
    """Schema for updating the status of an order."""

    status: OrderStatus = Field(description="The new status of the order")

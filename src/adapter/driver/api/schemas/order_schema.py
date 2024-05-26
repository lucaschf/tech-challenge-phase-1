from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from src.core.domain.entities.order import Order as OrderEntity
from src.core.domain.entities.order import OrderProduct as OrderProductEntity
from src.core.domain.value_objects.order_status import OrderStatus


class _BaseOrderProduct(BaseModel):
    product_id: UUID = Field(description="The product ID")
    quantity: int = Field(description="The quantity of the product", gt=0)


class OrderProductIn(_BaseOrderProduct):
    """Schema for creating a new order product."""

    model_config = ConfigDict(str_strip_whitespace=True)


class OrderProductOut(_BaseOrderProduct):
    """Schema for returning an order product."""

    @staticmethod
    def from_entity(entity: OrderProductEntity) -> "OrderProductOut":
        """Creates an OrderProductOut instance from an OrderProduct entity."""
        return OrderProductOut(
            product_id=entity.product_id,
            quantity=entity.quantity,
        )


class OrderIn(BaseModel):
    """Schema for creating a new order."""

    user_id: UUID = Field(description="The user ID")
    products: List[OrderProductIn] = Field(description="List of products in the order")

    model_config = ConfigDict(str_strip_whitespace=True, arbitrary_types_allowed=True)


class OrderOut(OrderIn):
    """Schema for returning an order."""

    id: UUID = Field(description="The order external id")
    status: OrderStatus = Field(description="The order status")
    created_at: datetime = Field(description="The order creation date")
    updated_at: datetime = Field(description="The order last update date")

    @staticmethod
    def from_entity(entity: OrderEntity) -> "OrderOut":
        """Creates an OrderOut instance from an Order entity."""
        return OrderOut(
            id=entity.id,
            user_id=entity.user_id,
            products=[OrderProductOut.from_entity(product) for product in entity.products],
            status=entity.status,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )


class OrderStatusUpdate(BaseModel):
    """Schema for updating the status of an order."""

    status: OrderStatus = Field(description="The new status of the order")

    model_config = ConfigDict(str_strip_whitespace=True, arbitrary_types_allowed=True)

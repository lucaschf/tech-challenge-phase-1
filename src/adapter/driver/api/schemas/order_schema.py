from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from src.core.domain.entities.order import Order as OrderEntity
from src.core.domain.entities.order import OrderProduct as OrderProductEntity


class _BaseOrderProduct(BaseModel):
    product_uuid: UUID = Field(description="The product uuid")
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
            product_uuid=entity.product_uuid,
            quantity=entity.quantity,
        )


class OrderIn(BaseModel):
    """Schema for creating a new order."""

    user_uuid: UUID = Field(description="The user uuid")
    products: List[OrderProductIn] = Field(description="List of products in the order")

    model_config = ConfigDict(str_strip_whitespace=True, arbitrary_types_allowed=True)


class OrderOut(BaseModel):
    """Schema for returning an order."""

    uuid: UUID = Field(description="The order external uuid")
    user_uuid: UUID = Field(description="The user uuid")
    products: List[OrderProductOut] = Field(description="List of products in the order")
    status: str = Field(description="The order status")  # Altere para string
    created_at: datetime = Field(description="The order creation date")
    updated_at: datetime = Field(description="The order last update date")

    @staticmethod
    def from_entity(entity: OrderEntity) -> "OrderOut":
        """Creates an OrderOut instance from an Order entity."""
        return OrderOut(
            uuid=entity.uuid,
            user_uuid=entity.user_uuid,
            products=[OrderProductOut.from_entity(product) for product in entity.products],
            status=str(entity.status),  # Passe a string do status
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

    model_config = ConfigDict(str_strip_whitespace=True, arbitrary_types_allowed=True)


class OrderStatusUpdate(BaseModel):
    """Schema for updating the status of an order."""

    status: str = Field(description="The new status of the order")  # Altere para string

    model_config = ConfigDict(str_strip_whitespace=True, arbitrary_types_allowed=True)

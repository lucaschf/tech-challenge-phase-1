from typing import List
from uuid import UUID

from pydantic import BaseModel, Field

from src.core.domain.entities import OrderItem
from src.core.domain.value_objects import Category


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

    # TODO: Remove this method from here. Move this to presenter layer.
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


__all__ = [
    "OrderItemIn",
    "OrderItemOut",
]

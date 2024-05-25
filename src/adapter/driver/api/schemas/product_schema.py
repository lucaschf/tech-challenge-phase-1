from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from src.adapter.driver.api.types.category_str import CategoryStr
from src.core.domain.entities.product import Product
from src.core.domain.value_objects.category import Category


class _BaseProduct(BaseModel):
    name: str = Field(description="The product name", min_length=1, max_length=100)
    category: CategoryStr = Field(description="The product category")
    price: float = Field(description="The product price")
    description: str = Field(description="The product description", max_length=255)
    images: List[str] = Field(description="List of image URLs for the product")


class ProductCreationIn(_BaseProduct):
    """Schema for creating a new product."""

    model_config = ConfigDict(str_strip_whitespace=True)


class ProductOut(ProductCreationIn):
    """Schema for returning a product."""

    uuid: UUID = Field(description="The product external id")
    created_at: datetime = Field(description="The product creation date")
    updated_at: datetime = Field(description="The product last update date")

    @staticmethod
    def from_entity(entity: Product) -> "ProductOut":
        """Creates a ProductOut instance from a Product entity."""
        return ProductOut(
            name=entity.name,
            category=CategoryStr(
                entity.category.category
                if isinstance(entity.category, Category)
                else entity.category
            ),
            price=entity.price,
            description=entity.description,
            images=list(entity.images),
            uuid=entity.uuid,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

    __all__ = [
        "ProductCreationIn",
        "ProductOut",
    ]

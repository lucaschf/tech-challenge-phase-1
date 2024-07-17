from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from src.core.domain.entities.product import Product
from src.core.domain.value_objects import Category
from src.core.use_cases.product import ProductCreation


class _BaseProduct(BaseModel):
    name: str = Field(description="The product name", min_length=1, max_length=100)
    category: Category = Field(description="The product category")
    price: float = Field(description="The product price", gt=0)
    description: str = Field(description="The product description", max_length=255, min_length=10)
    images: List[str] = Field(
        description="List of image URLs for the product", min_length=1, max_length=50
    )


class ProductCreationIn(_BaseProduct):
    """Schema for creating a new product."""

    model_config = ConfigDict(str_strip_whitespace=True)

    def to_product_creation_dto(self) -> ProductCreation:
        """Converts the schema to a ProductCreation instance."""
        return ProductCreation(
            name=self.name,
            category=self.category,
            price=self.price,
            description=self.description,
            images=self.images,
        )


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
            category=entity.category,
            price=entity.price,
            description=entity.description,
            images=entity.images,
            uuid=entity.uuid,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )


__all__ = [
    "ProductCreationIn",
    "ProductOut",
]

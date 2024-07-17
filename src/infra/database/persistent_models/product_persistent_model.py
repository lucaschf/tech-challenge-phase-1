from typing import List

from sqlalchemy import ARRAY, Column, Float, String
from sqlalchemy import Enum as SaEnum
from sqlalchemy.orm import Mapped

from src.core.domain.entities import Product
from src.core.domain.value_objects import Category

from .persistent_model import PersistentModel


class ProductPersistentModel(PersistentModel):
    """Represents a product in the system."""

    __tablename__ = "products"

    name: Mapped[str] = Column(String(100), nullable=False, unique=True)
    category: Mapped[Category] = Column(SaEnum(Category), nullable=False)
    price: Mapped[float] = Column(Float, nullable=False)
    description: Mapped[str] = Column(String(255), nullable=False)
    images: Mapped[List[str]] = Column(ARRAY(String), nullable=False)

    def to_entity(self) -> Product:
        """Converts the persistent model to a domain entity."""
        return Product(
            _id=self.id,
            name=self.name,
            category=self.category,
            price=self.price,
            description=self.description,
            images=self.images,
            uuid=self.uuid,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )


__all__ = ["ProductPersistentModel"]

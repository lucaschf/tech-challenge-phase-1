from typing import List

from sqlalchemy import ARRAY, Column, Float, String
from sqlalchemy.orm import Mapped

from .persistent_model import PersistentModel


class ProductPersistentModel(PersistentModel):
    """Represents a product in the system."""

    __tablename__ = "products"

    name: Mapped[str] = Column(String(100), nullable=False)
    category: Mapped[str] = Column(String(100), nullable=False)
    price: Mapped[float] = Column(Float, nullable=False)
    description: Mapped[str] = Column(String(255), nullable=True)
    images: Mapped[List[str]] = Column(ARRAY(String), nullable=True)


__all__ = ["ProductPersistentModel"]

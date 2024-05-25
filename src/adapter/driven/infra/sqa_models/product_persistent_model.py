from typing import List

from sqlalchemy import Column, Float, String
from sqlalchemy.orm import Mapped

from .persistent_model import PersistentModel


class ProductPersistentModel(PersistentModel):
    """Represents a product in the system."""

    __tablename__ = "products"

    name: Mapped[str] = Column(String(100), nullable=False)
    category: Mapped[str] = Column(String(100), nullable=False)
    price: Mapped[float] = Column(Float, nullable=False)
    description: Mapped[str] = Column(String(255), nullable=True)
    images: Mapped[List[str]] = Column(String, nullable=True)

    def __init__(
        self, name: str, category: str, price: float, description: str, images: List[str]
    ) -> None:
        self.name = name
        self.category = category
        self.price = price
        self.description = description
        self.images = images
        super().__init__()


__all__ = ["ProductPersistentModel"]

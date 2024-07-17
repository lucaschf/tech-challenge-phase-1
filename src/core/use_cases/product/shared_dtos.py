from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from src.core.domain.value_objects import Category


@dataclass
class ProductResult:
    """Data structure for holding product data."""

    name: str
    category: Category
    price: float
    description: str
    images: list[str]
    uuid: UUID
    created_at: datetime
    updated_at: datetime


__all__ = ["ProductResult"]

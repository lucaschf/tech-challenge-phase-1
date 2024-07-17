from dataclasses import dataclass
from typing import List

from src.core.domain.value_objects import Category


@dataclass
class ProductUpdate:
    """Data structure for holding product creation data."""

    name: str
    category: Category
    price: float
    description: str
    images: List[str]


__all__ = ["ProductUpdate"]

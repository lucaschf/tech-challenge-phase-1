from enum import StrEnum, auto
from typing import List


class Category(StrEnum):
    """An Enum that represents a Product Category."""

    LANCHE = auto()
    ACOMPANHAMENTO = auto()
    BEBIDA = auto()
    SOBREMESA = auto()

    @classmethod
    def values(cls) -> List["Category"]:
        """Return a list of Category values."""
        return [cls[member] for member in cls.__members__]


__all__ = ["Category"]

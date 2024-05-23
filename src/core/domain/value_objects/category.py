from typing import ClassVar

from src.core.domain.base import ValueObject
from src.core.domain.exceptions import InvalidCategoryError


class Category(ValueObject):
    """A Value Object that represents a Product Category.

    The category must be one of the predefined categories: Lanche, Acompanhamento, Bebida, Sobremesa.

    Attributes:
        _category: The category of the product.
    """

    ALLOWED_CATEGORIES: ClassVar[set[str]] = {"Lanche", "Acompanhamento", "Bebida", "Sobremesa"}

    def __init__(self, category: str) -> None:
        """Initializes a Category object after validating the input category.

        Args:
            category (str): The category to be validated and stored.

        Raises:
            InvalidCategoryError: If the input category is invalid.
        """
        if not self._is_valid(category):
            raise InvalidCategoryError(category=category)

        self._category = category

    def _get_equality_components(self) -> tuple[str]:
        """Provides the components that define the value of this Category object.

        Returns:
            Tuple[str]: A tuple containing the category.
        """
        return (self.category,)

    @property
    def category(self) -> str:
        """Gets the category.

        Returns:
            str: The category.
        """
        return self._category

    @classmethod
    def _is_valid(cls, category: str) -> bool:
        """Validates if the input category is one of the allowed categories.

        Args:
            category (str): The category to be validated.

        Returns:
            bool: True if the category is valid, False otherwise.
        """
        return category in cls.ALLOWED_CATEGORIES

    def __str__(self) -> str:
        """Returns the category as a string."""
        return self.category


__all__ = ["Category"]

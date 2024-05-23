from datetime import datetime
from uuid import UUID

from src.core.domain.base import AggregateRoot, AssertionConcern
from src.core.domain.value_objects.category import Category


class Product(AggregateRoot):
    """Represents a product in the system.

    Attributes:
    name: The product's name.
    category: The product's category.
    price: The product's price.
    description: The product's description.
    images: The product's images.
    """

    def __init__(
        self,
        name: str,
        category: Category,
        price: float,
        description: str,
        images: list[str],
        _id: int | None = None,
        uuid: UUID | None = None,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
    ) -> None:
        """Initializes a new Product instance."""
        self.name = name
        self.category = category
        self.price = price
        self.description = description
        self.images = images

        super().__init__(_id, uuid, created_at, updated_at)
        self.validate()

    def validate(self) -> None:
        """Validates the product's attributes.

        This method checks if the product's name, category, price, and description are not null or empty.
        If any of these conditions are not met, a DomainError will be raised with a relevant message.

        Raises:
            DomainError: If any of the product's attributes are null or empty.
        """
        AssertionConcern.assert_argument_not_null(self.name, "Name is required")
        AssertionConcern.assert_argument_not_empty(self.name, "Name is required")
        AssertionConcern.assert_argument_not_null(self.category, "Category is required")
        AssertionConcern.assert_argument_not_null(self.price, "Price is required")
        AssertionConcern.assert_argument_not_null(self.description, "Description is required")
        AssertionConcern.assert_argument_not_empty(self.description, "Description is required")
        AssertionConcern.assert_argument_not_null(self.images, "Images are required")
        AssertionConcern.assert_argument_not_empty(self.images, "Images are required")


__all__ = ["Product"]

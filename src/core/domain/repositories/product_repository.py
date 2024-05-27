from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from src.core.domain.entities.product import Product


class ProductRepository(ABC):
    """ProductRepository is an abstract base class that defines the contract for product persistence operations.

    This class outlines the methods that any concrete implementation of a product repository must provide.
    """

    @abstractmethod
    def create(self, product: Product) -> Product:
        """Persists a new product in the repository.

        Args:
            product (Product): The product to be created.

        Returns:
            Product: The created product with its ID and other persistence details populated.
        """
        pass

    @abstractmethod
    def update(self, product_uuid: UUID, product: Product) -> Product:
        """Updates an existing product in the repository.

        Args:
            product_uuid (UUID): The ID of the product to be updated.
            product (Product): The product data to update.

        Returns:
            Product: The updated product.
        """
        pass

    @abstractmethod
    def delete(self, product_uuid: UUID) -> None:
        """Deletes a product from the repository.

        Args:
            product_uuid (UUID): The ID of the product to be deleted.

        Returns:
            None
        """
        pass

    @abstractmethod
    def get_by_category(self, category: str) -> List[Product]:
        """Retrieves all products in a given category.

        Args:
            category (str): The category to filter products by.

        Returns:
            List[Product]: A list of products in the specified category.
        """
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Product | None:
        """Retrieves a product by its name.

        Args:
            name (str): The name of the product to retrieve.

        Returns:
            Product: The product with the specified name.
        """

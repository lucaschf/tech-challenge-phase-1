from typing import List
from uuid import UUID

from src.core.domain.entities.product import Product
from src.core.domain.repositories.product_repository import ProductRepository


class ProductUseCase:
    """ProductUseCase encapsulates the business logic for managing products.

    This class provides methods for creating, updating, deleting, and retrieving products by category.
    """

    def __init__(self, repository: ProductRepository) -> None:
        """Initializes a new instance of the ProductUseCase class.

        Args:
            repository (ProductRepository): The repository instance for product persistence operations.
        """
        self.repository = repository

    def delete_product(self, product_uuid: UUID) -> None:
        """Deletes a product.

        Args:
            product_uuid (int): The ID of the product to be deleted.

        Returns:
            None
        """
        self.repository.delete(product_uuid)

    def get_products_by_category(self, category: str) -> List[Product]:
        """Retrieves products by category.

        Args:
            category (str): The category to filter products by.

        Returns:
            List[Product]: A list of products in the specified category.
        """
        return self.repository.get_by_category(category)

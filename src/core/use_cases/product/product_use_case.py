from typing import List

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

    def get_products_by_category(self, category: str) -> List[Product]:
        """Retrieves products by category.

        Args:
            category (str): The category to filter products by.

        Returns:
            List[Product]: A list of products in the specified category.
        """
        return self.repository.get_by_category(category)

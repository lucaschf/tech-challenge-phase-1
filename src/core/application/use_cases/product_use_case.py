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

    def create_product(self, product: Product) -> Product:
        """Creates a new product.

        Args:
            product (Product): The product to be created.

        Returns:
            Product: The created product with its ID and other persistence details populated.
        """
        return self.repository.create(product)

    def update_product(self, product_id: int, product: Product) -> Product:
        """Updates an existing product.

        Args:
            product_id (int): The ID of the product to be updated.
            product (Product): The product data to update.

        Returns:
            Product: The updated product.
        """
        return self.repository.update(product_id, product)

    def delete_product(self, product_id: int) -> None:
        """Deletes a product.

        Args:
            product_id (int): The ID of the product to be deleted.

        Returns:
            None
        """
        self.repository.delete(product_id)

    def get_products_by_category(self, category: str) -> List[Product]:
        """Retrieves products by category.

        Args:
            category (str): The category to filter products by.

        Returns:
            List[Product]: A list of products in the specified category.
        """
        return self.repository.get_by_category(category)

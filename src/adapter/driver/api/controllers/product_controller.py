from typing import List

from src.core.application.use_cases.product_use_case import ProductUseCase
from src.core.domain.entities.product import Product


class ProductController:
    """ProductController handles HTTP requests for product-related operations.

    This class interacts with the ProductUseCase to process the business logic.
    """

    def __init__(self, use_case: ProductUseCase) -> None:
        """Initializes the ProductController with a given use case.

        Args:
            use_case (ProductUseCase): The use case to handle product operations.
        """
        self.use_case = use_case

    async def create_product(self, product: Product) -> Product:
        """Handles the creation of a new product.

        Args:
            product (Product): The product to be created.

        Returns:
            Product: The created product.
        """
        return await self.use_case.create_product(product)

    async def update_product(self, product_id: int, product: Product) -> Product:
        """Handles the update of an existing product.

        Args:
            product_id (int): The ID of the product to be updated.
            product (Product): The updated product data.

        Returns:
            Product: The updated product.
        """
        return await self.use_case.update_product(product_id, product)

    async def delete_product(self, product_id: int) -> None:
        """Handles the deletion of a product.

        Args:
            product_id (int): The ID of the product to be deleted.

        Returns:
            None
        """
        await self.use_case.delete_product(product_id)

    async def get_products_by_category(self, category: str) -> List[Product]:
        """Retrieves products by category.

        Args:
            category (str): The category to filter products by.

        Returns:
            List[Product]: A list of products in the specified category.
        """
        return await self.use_case.get_products_by_category(category)

from typing import Iterable

from src.core.domain.repositories import ProductRepository
from src.core.domain.value_objects import Category

from ..shared_dtos import ProductResult


class GetProductsByCategoryUseCase:
    """A use case for retrieving products by category."""

    def __init__(self, product_repository: ProductRepository) -> None:
        """Initializes the use case with a product repository.

        Args:
            product_repository (ProductRepository): The repository for accessing product data.
        """
        self._product_repository = product_repository

    def execute(self, category: Category) -> Iterable[ProductResult]:
        """Executes the use case to get products by category.

        Args:
            category (Category): The category to filter products by.

        Returns:
            An iterable of `ProductResult` instances representing the products.
        """
        products = self._product_repository.get_by_category(category)

        return [
            ProductResult(
                uuid=product.uuid,
                name=product.name,
                category=product.category,
                price=product.price,
                description=product.description,
                images=product.images,
                created_at=product.created_at,
                updated_at=product.updated_at,
            )
            for product in products
        ]


__all__ = ["GetProductsByCategoryUseCase"]

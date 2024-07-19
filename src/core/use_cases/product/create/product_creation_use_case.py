from src.core.domain.base import DomainError
from src.core.domain.entities.product import Product
from src.core.domain.repositories import ProductRepository

from ..shared_dtos import ProductResult
from .product_creation_dto import ProductCreation


class ProductCreationUseCase:
    """A use case for creating a product within a system."""

    def __init__(self, repository: ProductRepository) -> None:
        """Initializes the use case with a specific product repository.

        Parameters:
            repository: An instance of ProductRepository used for product data interactions.
        """
        self.repository = repository

    def execute(self, product_data: ProductCreation) -> ProductResult:
        """Creates a new product if a product with the same name does not already exist.

        Parameters:
            product_data: The product to be created.

        Returns:
            Product: The created product instance.

        Raises:
            DomainError: If a product with the same name already exists.
        """
        if self.repository.get_by_name(product_data.name):
            raise DomainError(message="Product already exists")

        product = Product(
            name=product_data.name,
            category=product_data.category,
            price=product_data.price,
            description=product_data.description or "No description",
            images=product_data.images or ["https://via.placeholder.com/150"],
        )

        product = self.repository.create(product)

        return ProductResult(
            name=product.name,
            category=product.category,
            price=product.price,
            description=product.description,
            images=product.images,
            created_at=product.created_at,
            updated_at=product.updated_at,
            uuid=product.uuid,
        )


__all__ = ["ProductCreationUseCase"]

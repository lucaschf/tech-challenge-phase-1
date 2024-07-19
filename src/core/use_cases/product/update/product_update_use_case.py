from uuid import UUID

from src.core.domain.base import DomainError
from src.core.domain.entities import Product
from src.core.domain.repositories import ProductRepository

from ..shared_dtos import ProductResult
from .product_update_dto import ProductUpdate


class ProductUpdateUseCase:
    """A use case for updating a product within the system."""

    def __init__(self, product_repository: ProductRepository) -> None:
        """Initializes the use case with a specific product repository.

        Parameters:
            product_repository: An instance of ProductRepository used for product data interactions.
        """
        self._product_repository = product_repository

    def execute(self, product_uuid: UUID, product: ProductUpdate) -> ProductResult:
        """Executes the product update use case.

        Parameters:
            product_uuid: The UUID of the product to update.
            product: An instance of ProductUpdate containing the new product data.

        Returns:
            ProductResult: The updated product instance.

        Raises:
            DomainError: If a product with the same name already exists,
                and it's not the product being updated.
        """
        db_product = self._product_repository.get_by_name(product.name)

        if db_product and db_product.uuid != product_uuid:
            raise DomainError(message="Product already exists")

        db_product = self._product_repository.update(
            product_uuid,
            Product(
                name=product.name,
                category=product.category,
                price=product.price,
                description=product.description,
                images=product.images,
            ),
        )

        if not db_product:
            raise DomainError(message="Product not found")

        return ProductResult(
            uuid=db_product.uuid,
            name=db_product.name,
            category=db_product.category,
            price=db_product.price,
            description=db_product.description,
            images=db_product.images,
            created_at=db_product.created_at,
            updated_at=db_product.updated_at,
        )


__all__ = ["ProductUpdateUseCase"]

from uuid import UUID

from src.core.domain.exceptions import ProductNotFoundError
from src.core.domain.repositories import ProductRepository


class ProductDeleteUseCase:
    """A use case for deleting a product within the system."""

    def __init__(self, product_repository: ProductRepository) -> None:
        """Initializes the use case with a specific product repository.

        Parameters:
            product_repository: An instance of ProductRepository used for product data interactions.
        """
        self._product_repository = product_repository

    def execute(self, product_uuid: UUID) -> None:
        """Executes the product deletion use case.

        Parameters:
            product_uuid (UUID): The UUID of the product to delete.
        """
        if not self._product_repository.get_by_uuid(product_uuid):
            raise ProductNotFoundError(search_param=str(product_uuid))

        self._product_repository.delete(product_uuid)


__all__ = ["ProductDeleteUseCase"]

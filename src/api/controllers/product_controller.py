from typing import List
from uuid import UUID

from src.core.use_cases import ProductCreationUseCase, ProductUseCase

from ...core.use_cases.product import ProductUpdateUseCase
from ..presenters.product import DetailedProductPresenter
from ..schemas import ProductCreationIn, ProductOut
from ..schemas.product_schema import ProductUpdateIn


class ProductController:
    """This class manages product-related actions using ProductUseCase.

    The class acts as the intersection between the API and the business logic,
    handling HTTP requests related to product data.
    """

    def __init__(
        self,
        use_case: ProductUseCase,
        product_creation_use_case: ProductCreationUseCase,
        product_update_use_case: ProductUpdateUseCase,
    ) -> None:
        self.use_case = use_case
        self._product_creation_use_case = product_creation_use_case
        self._product_update_use_case = product_update_use_case

    def create_product(self, product_in: ProductCreationIn) -> ProductOut:
        """Registers a new product in the system from the provided product data."""
        created_product = self._product_creation_use_case.execute(
            product_in.to_product_creation_dto()
        )
        return DetailedProductPresenter().present(created_product)

    def update_product(self, product_uuid: UUID, product_in: ProductUpdateIn) -> ProductOut:
        """Update a product in the system from the provided product data and id."""
        updated_product = self._product_update_use_case.execute(
            product_uuid, product_in.to_product_update_dto()
        )
        return DetailedProductPresenter().present(updated_product)

    def delete_product(self, product_uuid: UUID) -> None:
        """Delete a product in the system from the provided product id."""
        self.use_case.delete_product(product_uuid)

    def get_products_by_category(self, category: str) -> List[ProductOut]:
        """Get a list of products in the system from the provided product category."""
        products = self.use_case.get_products_by_category(category)
        return [ProductOut.from_entity(product) for product in products]


__all__ = ["ProductController"]

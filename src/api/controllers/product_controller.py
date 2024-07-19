from typing import Iterable
from uuid import UUID

from src.core.use_cases import ProductCreationUseCase

from ...core.domain.value_objects import Category
from ...core.use_cases.product import (
    GetProductsByCategoryUseCase,
    ProductResult,
    ProductUpdateUseCase,
)
from ...core.use_cases.product.delete import ProductDeleteUseCase
from ..presenters import Presenter
from ..schemas import ProductCreationIn, ProductOut
from ..schemas.product_schema import ProductUpdateIn


class ProductController:
    """This class manages product-related actions using ProductUseCase.

    The class acts as the intersection between the API and the business logic,
    handling HTTP requests related to product data.
    """

    def __init__(
        self,
        product_creation_use_case: ProductCreationUseCase,
        product_update_use_case: ProductUpdateUseCase,
        product_delete_use_case: ProductDeleteUseCase,
        get_products_by_category_use_case: GetProductsByCategoryUseCase,
        product_details_presenter: Presenter[ProductOut, ProductResult],
    ) -> None:
        self._product_creation_use_case = product_creation_use_case
        self._product_update_use_case = product_update_use_case
        self._product_delete_use_case = product_delete_use_case
        self._get_products_by_category_use_case = get_products_by_category_use_case
        self._product_details_presenter = product_details_presenter

    def create_product(self, product_in: ProductCreationIn) -> ProductOut:
        """Registers a new product in the system from the provided product data."""
        created_product = self._product_creation_use_case.execute(
            product_in.to_product_creation_dto()
        )
        return self._product_details_presenter.present(created_product)

    def update_product(self, product_uuid: UUID, product_in: ProductUpdateIn) -> ProductOut:
        """Update a product in the system from the provided product data and id."""
        updated_product = self._product_update_use_case.execute(
            product_uuid, product_in.to_product_update_dto()
        )
        return self._product_details_presenter.present(updated_product)

    def delete_product(self, product_uuid: UUID) -> None:
        """Delete a product in the system from the provided product uuid."""
        self._product_delete_use_case.execute(product_uuid)

    def get_products_by_category(self, category: Category) -> Iterable[ProductOut]:
        """Get a list of products in the system from the provided product category."""
        products = self._get_products_by_category_use_case.execute(category)
        return self._product_details_presenter.present_many(products)


__all__ = ["ProductController"]

from typing import List

from src.adapter.driver.api.schemas.product_schema import ProductCreationIn, ProductOut
from src.core.application.use_cases.product_use_case import ProductUseCase
from src.core.domain.entities.product import Product


class ProductController:
    """This class manages product-related actions using ProductUseCase.

    The class acts as the intersection between the API and the business logic,
    handling HTTP requests related to product data.
    """

    def __init__(self, use_case: ProductUseCase) -> None:
        self.use_case = use_case

    def create_product(self, product_in: ProductCreationIn) -> ProductOut:
        """Registers a new product in the system from the provided product data."""
        product = Product(
            name=product_in.name,
            category=product_in.category,
            price=product_in.price,
            description=product_in.description,
            images=product_in.images,
        )
        created_product = self.use_case.create_product(product)
        return ProductOut.from_entity(created_product)

    def update_product(self, product_id: int, product_in: ProductCreationIn) -> ProductOut:
        """Update a product in the system from the provided product data and id."""
        product = Product(
            name=product_in.name,
            category=product_in.category,
            price=product_in.price,
            description=product_in.description,
            images=product_in.images,
        )
        updated_product = self.use_case.update_product(product_id, product)
        return ProductOut.from_entity(updated_product)

    def delete_product(self, product_id: int) -> None:
        """Delete a product in the system from the provided product id."""
        self.use_case.delete_product(product_id)

    def get_products_by_category(self, category: str) -> List[ProductOut]:
        """Get a list of products in the system from the provided product category."""
        products = self.use_case.get_products_by_category(category)
        return [ProductOut.from_entity(product) for product in products]

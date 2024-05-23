from typing import List

from fastapi import APIRouter, Depends

from src.adapter.driver.api.controllers.product_controller import ProductController
from src.adapter.driver.api.dependencies import get_product_controller
from src.core.domain.entities.product import Product

router = APIRouter()


@router.post("/products", response_model=Product)
async def create_product(
    product: Product,
    controller: ProductController = Depends(get_product_controller),  # noqa: B008
) -> Product:
    """Creates a new product.

    Args:
        product (Product): The product to be created.
        controller (ProductController): The controller to handle the request.

    Returns:
        Product: The created product.
    """
    return await controller.create_product(product)


@router.put("/products/{product_id}", response_model=Product)
async def update_product(
    product_id: int,
    product: Product,
    controller: ProductController = Depends(get_product_controller),  # noqa: B008
) -> Product:
    """Updates an existing product.

    Args:
        product_id (int): The ID of the product to be updated.
        product (Product): The updated product data.
        controller (ProductController): The controller to handle the request.

    Returns:
        Product: The updated product.
    """
    return await controller.update_product(product_id, product)


@router.delete("/products/{product_id}")
async def delete_product(
    product_id: int,
    controller: ProductController = Depends(get_product_controller),  # noqa: B008
) -> None:
    """Deletes a product.

    Args:
        product_id (int): The ID of the product to be deleted.
        controller (ProductController): The controller to handle the request.

    Returns:
        None
    """
    await controller.delete_product(product_id)
    return {"detail": "Product deleted"}


@router.get("/products", response_model=List[Product])
async def get_products_by_category(
    category: str,
    controller: ProductController = Depends(get_product_controller),  # noqa: B008
) -> List[Product]:
    """Retrieves products by category.

    Args:
        category (str): The category to filter products by.
        controller (ProductController): The controller to handle the request.

    Returns:
        List[Product]: A list of products in the specified category.
    """
    return await controller.get_products_by_category(category)

from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, Response, status

from src.adapter.driver.api.controllers.product_controller import ProductController
from src.adapter.driver.api.dependencies import get_product_controller

from ..schemas.product_schema import ProductCreationIn, ProductOut

router = APIRouter(tags=["Product"])


@router.post("/products", response_model=ProductOut, status_code=status.HTTP_201_CREATED)
def create_product(
    product: ProductCreationIn,
    controller: ProductController = Depends(get_product_controller),  # noqa: B008
) -> ProductOut:
    created_product = controller.create_product(product)
    return ProductOut.from_entity(created_product)


@router.put("/products/{product_id}", response_model=ProductOut)
def update_product(
    product_id: UUID,
    product: ProductCreationIn,
    controller: ProductController = Depends(get_product_controller),  # noqa: B008
) -> ProductOut:
    updated_product = controller.update_product(product_id, product)
    return ProductOut.from_entity(updated_product)


@router.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(
    product_id: UUID,
    controller: ProductController = Depends(get_product_controller),  # noqa: B008
) -> None:
    controller.delete_product(product_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/products", response_model=List[ProductOut])
def get_products_by_category(
    category: str,
    controller: ProductController = Depends(get_product_controller),  # noqa: B008
) -> List[ProductOut]:
    products = controller.get_products_by_category(category)
    return [ProductOut.from_entity(product) for product in products]


__all__ = ["router"]

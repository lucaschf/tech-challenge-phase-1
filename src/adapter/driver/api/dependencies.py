from fastapi import Depends
from sqlalchemy.orm import Session

from src.adapter.driven.infra.config import get_db_session
from src.adapter.driven.infra.repositories.product_repository_impl import (
    SQLAlchemyProductRepository,
)
from src.core.application.use_cases.product_use_case import ProductUseCase

from .controllers import ProductController


def get_product_controller(
    db_session: Session = Depends(get_db_session),  # noqa: B008
) -> ProductController:
    """Gets the product controller with all depencies."""
    product_repository = SQLAlchemyProductRepository(db_session)
    product_use_case = ProductUseCase(product_repository)
    return ProductController(product_use_case)

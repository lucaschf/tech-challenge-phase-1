from src.api.schemas import ProductOut
from src.core.use_cases.product import ProductResult

from ..presenter import Presenter


class ProductDetailsPresenter(Presenter[ProductOut, ProductResult]):
    """Presenter for the product details."""

    def present(self, data: ProductResult) -> ProductOut:
        """Converts the CustomerResult instance into a CustomerDetailsOut instance."""
        return ProductOut(
            uuid=data.uuid,
            name=data.name,
            category=data.category,
            price=data.price,
            description=data.description,
            images=data.images,
            created_at=data.created_at,
            updated_at=data.updated_at,
        )


__all__ = ["ProductDetailsPresenter"]

from .customer_router import router as customer_router
from .order_router import router as order_router
from .product_router import router as product_router

__all__ = ["customer_router", "order_router", "product_router"]

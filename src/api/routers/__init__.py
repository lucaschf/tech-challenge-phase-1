from .customer_router import router as customer_router
from .order_router import router as order_router
from .payment_router import router as payment_router
from .product_router import router as product_router

__all__ = ["customer_router", "order_router", "payment_router", "product_router"]

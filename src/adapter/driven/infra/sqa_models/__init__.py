"""This package contains SQLAlchemy models for the System.

These models are used to interact with the database using SQLAlchemy,
an SQL toolkit and Object-Relational Mapping (ORM) system for Python.

They provide a high-level API for SQL operations, abstracting the underlying database system.
"""

from .customer_persistent_model import CustomerPersistentModel
from .order_persistent_model import OrderPersistentModel
from .order_product_persistent_model import OrderProductPersistentModel
from .persistent_model import PersistentModel
from .product_persistent_model import ProductPersistentModel

__all__ = [
    "CustomerPersistentModel",
    "OrderPersistentModel",
    "OrderProductPersistentModel",
    "PersistentModel",
    "ProductPersistentModel",
]

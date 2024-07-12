"""This module defines the Value Objects used within the domain.

Value Objects are immutable entities characterized by their attributes or state, rather than
their identity.
They encapsulate a set of attributes and related behavior
that form a conceptual whole within the domain model.

This module provides a declaration of such objects,
promoting code consistency and domain integrity.
"""

from src.core.domain.base import ValueObject

from .category import Category
from .cpf import CPF
from .email import Email
from .order_status import OrderStatus

__all__ = [
    "CPF",
    "Category",
    "Email",
    "OrderStatus",
    "ValueObject",
]

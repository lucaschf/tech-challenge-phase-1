"""Provides a set of domain-specific exceptions.

These exceptions are triggered when certain domain rules or invariants are violated.
The module includes DomainError, which serves as the base class for all exceptions specific to
the domain.

This approach ensures that domain-specific issues are encapsulated within their own unique
exception types, enhancing error handling and debugging processes.
"""

from src.core.domain.base import DomainError

from .cpf_error import InvalidCpfError
from .customer_error import CustomerNotFoundError
from .email_error import InvalidEmailError
from .not_found_error import NotFoundError

__all__ = [
    "CustomerNotFoundError",
    "DomainError",
    "InvalidCpfError",
    "InvalidEmailError",
    "NotFoundError",
]

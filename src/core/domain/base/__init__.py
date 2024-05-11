"""Contains core classes that define the fundamental structures of the domain model.

It includes `ValueObject`, `AggregateRoot`, `DomainError` and `AssertionConcern`.
It provides essential building blocks for defining domain entities,
value objects, erros, and more.
"""

from .aggregate_root import AggregateRoot
from .assertion_concern import AssertionConcern
from .domain_error import DomainError
from .value_object import ValueObject

__all__ = [
    "AggregateRoot",
    "AssertionConcern",
    "DomainError",
    "ValueObject",
]

"""Provides interfaces for managing domain entities.

Following the Repository Design Pattern, these interfaces serve as an abstraction layer between
the domain model and the data mapping layers.

They offer methods for creating, reading, updating, and deleting domain entities, ensuring a
clean separation of concerns and enhancing the maintainability of the codebase.
"""

from .customer_repository import CustomerRepository

__all__ = ["CustomerRepository"]

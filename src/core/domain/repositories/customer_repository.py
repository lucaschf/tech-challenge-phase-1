from abc import ABC, abstractmethod
from uuid import UUID

from src.core.domain.entities.customer import Customer
from src.core.domain.value_objects import CPF, Email


class CustomerRepository(ABC):
    """Repository for handling customer persistence."""

    @abstractmethod
    def exists(self, cpf: CPF | None, email: Email | None) -> bool:
        """Check if a customer already exists in the database either by cpf, email or both.

        Args:
            cpf: The customer's CPF.
            email: The customer's email.

        Returns:
            bool: True if the customer exists, False otherwise.
        """

    @abstractmethod
    def get_by_cpf(self, cpf: CPF) -> Customer | None:
        """Get a customer by their CPF.

        Args:
            cpf: The customer's CPF.

        Returns:
            Customer: The customer data if found, None otherwise.
        """

    @abstractmethod
    def get_by_uuid(self, uuid: UUID) -> Customer | None:
        """Get a customer by their UUID.

        Args:
            uuid: The customer's UUID.

        Returns:
            Customer: The customer data if found, None otherwise.
        """

    @abstractmethod
    def add(self, customer: Customer) -> Customer:
        """Add a new customer to the database.

        Args:
           customer: The customer data.

        Returns:
           Customer: The added customer data.
        """


__all__ = ["CustomerRepository"]

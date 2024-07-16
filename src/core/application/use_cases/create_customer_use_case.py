from dataclasses import dataclass

from src.core.domain.base import DomainError
from src.core.domain.entities import Customer
from src.core.domain.repositories import CustomerRepository
from src.core.domain.value_objects import CPF, Email


@dataclass
class CustomerData:
    name: str
    cpf: CPF
    email: Email


class CreateCustomerUseCase:
    """A use case for creating a new customer."""

    def __init__(self, customer_repository: CustomerRepository) -> None:
        self.customer_repository = customer_repository

    def execute(self, customer_data: CustomerData) -> Customer:
        """Creates a new customer using the provided data and adds it to the repository.

        Args:
            customer_data: The data for creating the new customer.

        Returns:
            Customer: The newly created customer.

        Raises:
            DomainError: If the customer already exists.
        """
        customer = Customer(
            name=customer_data.name, cpf=customer_data.cpf, email=customer_data.email
        )
        if self.customer_repository.exists(customer.cpf, customer.email):
            raise DomainError(message="Customer already exists")

        return self.customer_repository.add(customer)


__all__ = ["CreateCustomerUseCase"]

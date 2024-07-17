from src.core.domain.base import DomainError
from src.core.domain.entities import Customer
from src.core.domain.repositories import CustomerRepository

from ..shared_dtos import CustomerResult
from .create_customer_dto import CustomerCreationData


class CreateCustomerUseCase:
    """A use case for creating a new customer."""

    def __init__(self, customer_repository: CustomerRepository) -> None:
        self.customer_repository = customer_repository

    def execute(self, customer_data: CustomerCreationData) -> CustomerResult:
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

        db_customer = self.customer_repository.add(customer)
        return CustomerResult(
            name=db_customer.name,
            cpf=db_customer.cpf,
            email=db_customer.email,
            created_at=db_customer.created_at,
            updated_at=db_customer.updated_at,
            uuid=db_customer.uuid,
        )


__all__ = ["CreateCustomerUseCase"]

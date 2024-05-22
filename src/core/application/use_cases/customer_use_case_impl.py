from src.core.application.use_cases.customer_use_case import CustomerUseCase
from src.core.domain.base import DomainError
from src.core.domain.entities import Customer
from src.core.domain.repositories import CustomerRepository
from src.core.domain.value_objects import CPF, Email


class CustomerUseCaseImpl(CustomerUseCase):
    """Implementation of the customer use case.

    Attributes:
        customer_repository (CustomerRepository): The repository for customer operations.
    """

    def __init__(self, customer_repository: CustomerRepository) -> None:
        self.customer_repository = customer_repository

    def create_customer(self, name: str, cpf: str, email: str) -> Customer:
        """Create a new customer.

        Args:
            name: The customer's name.
            cpf: The customer's CPF.
            email: The customer's email.

        Returns:
            Customer: The created customer data.

        Raises:
            DomainError: If the customer already exists.
        """
        customer: Customer = Customer(name=name, cpf=CPF(cpf), email=Email(email))
        if self.customer_repository.exists(customer.cpf, customer.email):
            raise DomainError(message="Customer already exists")
        return self.customer_repository.add(customer)

    def get_by_cpf(self, cpf: str) -> Customer:
        """Get a customer by their CPF.

        Args:
            cpf: The customer's CPF.

        Returns:
            Customer: The customer data if found.
        """
        return self.customer_repository.get_by_cpf(CPF(cpf))


__all__ = ["CustomerUseCaseImpl"]

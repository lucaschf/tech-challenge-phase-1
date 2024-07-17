from src.core.domain.exceptions import CustomerNotFoundError
from src.core.domain.repositories import CustomerRepository
from src.core.domain.value_objects import CPF

from ..shared_dtos import CustomerResult


class GetCustomerByCpfUseCase:
    """A use case for getting a customer by their CPF."""

    def __init__(self, customer_repository: CustomerRepository) -> None:
        self.customer_repository = customer_repository

    def execute(self, cpf: str) -> CustomerResult:
        """Get a customer by their CPF.

        Args:
            cpf: The customer's CPF.

        Returns:
            Customer: The customer data if found.

        Raises:
            CustomerNotFoundError: If the customer is not found.
        """
        customer = self.customer_repository.get_by_cpf(CPF(cpf))

        if not customer:
            raise CustomerNotFoundError(search_params={"cpf": cpf})

        return CustomerResult(
            name=customer.name,
            cpf=customer.cpf,
            email=customer.email,
            created_at=customer.created_at,
            updated_at=customer.updated_at,
            uuid=customer.uuid,
        )


__all__ = ["GetCustomerByCpfUseCase"]

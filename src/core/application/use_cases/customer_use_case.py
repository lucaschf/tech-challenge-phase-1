from abc import ABC, abstractmethod

from src.core.domain.entities.customer import Customer
from src.core.domain.value_objects import CPF, Email


class CustomerUseCase(ABC):
    """Abstract base class for handling customer related operations.

     This acts as a base for all the use cases
    involving customers within the system.
    """

    @abstractmethod
    def create_customer(self, name: str, cpf: CPF, email: Email) -> Customer:
        """Abstract method representing the creation of a new customer in the system.

        Args:
            name: A string representing the customer's name.
            cpf: A string representing the unique CPF (Cadastro de Pessoas Físicas) of the customer.
            email: A string representing the email address of the customer.

        Returns:
            Customer: A Customer object with the newly created customer's data.
        """
        pass

    @abstractmethod
    def get_by_cpf(self, cpf: str) -> Customer | None:
        """Abstract method representing the procedure to fetch customer details given a CPF.

        Args:
            cpf: A string representing the unique CPF (Cadastro de Pessoas Físicas) of the customer.
                 CPF is a unique identifier for individuals in a country.

        Returns:
            Customer: A Customer object containing the customer data if a customer with the given
             CPF exists. In case no such customer exists, returns None.
        """
        pass


__all__ = ["CustomerUseCase"]

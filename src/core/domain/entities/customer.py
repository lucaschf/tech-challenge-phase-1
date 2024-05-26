from dataclasses import dataclass, field

from src.core.domain.base import AggregateRoot, AssertionConcern
from src.core.domain.value_objects import CPF, Email


@dataclass(kw_only=True)
class Customer(AggregateRoot):
    """Represents a customer in the system.

    Attributes:
    name: The customer's name.
    cpf: The customer's CPF.
    email: The customer's email.
    """

    name: str = field()
    cpf: CPF = field()
    email: Email = field()

    def validate(self) -> None:
        """Validates the customer's attributes.

        This method checks if the customer's name, CPF, and email are not null or empty.
        If any of these conditions are not met, a DomainError will be raised
        with a relevant message.

        Raises:
           DomainError: If any of the customer's attributes are null or empty.
        """
        AssertionConcern.assert_argument_not_null(self.name, "Name is required")
        AssertionConcern.assert_argument_not_empty(self.name, "Name is required")
        AssertionConcern.assert_argument_not_null(self.cpf, "CPF is required")
        AssertionConcern.assert_argument_not_null(self.email, "Email is required")


__all__ = ["Customer"]

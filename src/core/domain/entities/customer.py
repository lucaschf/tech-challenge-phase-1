from datetime import datetime
from uuid import UUID

from src.core.domain.base import AggregateRoot, AssertionConcern
from src.core.domain.value_objects import CPF, Email


class Customer(AggregateRoot):
    """Represents a customer in the system.

    Attributes:
    name: The customer's name.
    cpf: The customer's CPF.
    email: The customer's email.
    """

    def __init__(
        self,
        name: str,
        cpf: CPF,
        email: Email,
        _id: int | None = None,
        uuid: UUID | None = None,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
    ) -> None:
        """Initializes a new Customer instance."""
        self.name = name
        self.cpf = cpf
        self.email = email
        super().__init__(_id, uuid, created_at, updated_at)

    def validate(self) -> None:
        """Validates the customer's attributes.

        This method checks if the customer's name, CPF, and email are not null or empty.
        If any of these conditions are not met, an AssertionError will be raised
         with a relevant message.

        Raises:
            DomainError: If any of the customer's attributes are null or empty.
        """
        AssertionConcern.assert_argument_not_null(self.name, "Name is required")
        AssertionConcern.assert_argument_not_empty(self.name, "Name is required")
        AssertionConcern.assert_argument_not_null(self.cpf, "CPF is required")
        AssertionConcern.assert_argument_not_null(self.email, "Email is required")

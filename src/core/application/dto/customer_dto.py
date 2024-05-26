from dataclasses import dataclass
from uuid import UUID


@dataclass
class CustomerInputDTO:
    """Data Transfer Object for customer input.

    Attributes:
        name: The name of the customer.
        cpf: The CPF of the customer.
        email: The email of the customer.
    """

    name: str
    cpf: str
    email: str


@dataclass
class CustomerOutputDTO:
    """Data Transfer Object for customer output.

    Attributes:
        uuid: The ID of the customer.
        name: The name of the customer.
        cpf: The CPF of the customer.
        email: The email of the customer.
    """

    uuid: UUID
    name: str
    cpf: str
    email: str


__all__ = ["CustomerInputDTO", "CustomerOutputDTO"]

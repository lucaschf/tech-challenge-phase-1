from dataclasses import dataclass

from src.core.domain.value_objects import CPF, Email


@dataclass
class CustomerCreationData:
    """Data structure for holding customer creation data.

    Attributes:
        name: The name of the customer.
        cpf: The CPF (Cadastro de Pessoas Físicas) of the customer.
        email: The email address of the customer.
    """

    name: str
    cpf: CPF
    email: Email


__all__ = [
    "CustomerCreationData",
]

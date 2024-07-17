from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from src.core.domain.value_objects import CPF, Email


@dataclass
class CustomerResult:
    """Data structure for holding data of a customer.

    Attributes:
        name: The name of the customer.
        cpf: The CPF of the customer.
        email: The email address of the customer.
        uuid: The unique identifier of the customer.
        created_at: The timestamp when the customer was created.
        updated_at: The timestamp when the customer data was last updated.
    """

    name: str
    cpf: CPF
    email: Email
    uuid: UUID
    created_at: datetime
    updated_at: datetime


__all__ = ["CustomerResult"]

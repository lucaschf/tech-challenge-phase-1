from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field

from src.adapter.driver.api.types import CPFStr
from src.core.domain.entities.customer import Customer


class _BaseCustomer(BaseModel):
    name: str = Field(description="The customer full name", min_length=3, max_length=100)
    email: EmailStr = Field(description="The customer email address")
    cpf: CPFStr = Field(description="The customer CPF number")


class CustomerCreationIn(_BaseCustomer):
    """Schema for creating a new customer."""

    model_config = ConfigDict(str_strip_whitespace=True)


class CustomerOut(_BaseCustomer):
    """Schema for returning a customer."""

    uuid: UUID = Field(description="The customer external id")
    created_at: datetime = Field(description="The customer creation date")
    updated_at: datetime = Field(description="The customer last update date")

    @staticmethod
    def from_entity(entity: Customer) -> "CustomerOut":
        """Creates a CustomerOut instance from a Customer entity."""
        return CustomerOut(
            name=entity.name,
            cpf=CPFStr(str(entity.cpf)),
            email=str(entity.email),
            uuid=entity.uuid,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )


__all__ = [
    "CustomerCreationIn",
    "CustomerOut",
]

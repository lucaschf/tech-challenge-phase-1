from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field

from src.core.domain.value_objects import CPF, Email
from src.core.use_cases.customer.create import CustomerCreationData

from ..types import CPFStr


class BaseCustomer(BaseModel):
    """Base schema for customer data."""

    name: str = Field(description="The customer full name", min_length=3, max_length=100)
    email: EmailStr = Field(description="The customer email address")
    cpf: CPFStr = Field(description="The customer CPF number")


class CustomerSummaryOut(BaseCustomer):
    """Schema for returning a simplified customer."""

    pass


class CustomerCreationIn(BaseCustomer):
    """Schema for creating a new customer."""

    def to_customer_creation_data(self) -> CustomerCreationData:
        """Converts the schema into a CustomerData instance."""
        return CustomerCreationData(
            name=self.name,
            cpf=CPF(self.cpf),
            email=Email(self.email),
        )

    model_config = ConfigDict(str_strip_whitespace=True)


class CustomerDetailsOut(CustomerSummaryOut):
    """Schema for returning a customer."""

    uuid: UUID = Field(description="The customer external id")
    created_at: datetime = Field(description="The customer creation date")
    updated_at: datetime = Field(description="The customer last update date")


__all__ = [
    "CustomerCreationIn",
    "CustomerDetailsOut",
    "CustomerSummaryOut",
]

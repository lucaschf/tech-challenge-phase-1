from sqlalchemy import CheckConstraint, Column, String
from sqlalchemy.orm import Mapped

from src.core.domain.entities import Customer
from src.core.domain.value_objects import CPF, Email

from .persistent_model import PersistentModel


class CustomerPersistentModel(PersistentModel):
    """This class represents a customer table in the system."""

    __tablename__ = "customers"

    name: Mapped[str] = Column(String)
    cpf: Mapped[str] = Column(String(11), unique=True)
    email: Mapped[str] = Column(String(120), unique=True)

    def to_entity(self) -> Customer:
        """Converts the persistent model to a Customer entity."""
        return Customer(
            _id=self.id,
            uuid=self.uuid,
            name=self.name,
            cpf=CPF(self.cpf),
            email=Email(self.email),
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    __table_args__ = (CheckConstraint("char_length(cpf) = 11", name="cons_cpf_length"),)


__all__ = ["CustomerPersistentModel"]

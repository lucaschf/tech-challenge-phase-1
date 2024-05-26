from sqlalchemy import CheckConstraint, Column, String
from sqlalchemy.orm import Mapped, relationship

from .persistent_model import PersistentModel


class CustomerPersistentModel(PersistentModel):
    """This class represents a customer table in the system."""

    __tablename__ = "customers"

    name: Mapped[str] = Column(String)
    cpf: Mapped[str] = Column(String(11), unique=True)
    email: Mapped[str] = Column(String(120), unique=True)

    orders = relationship("OrderPersistentModel", back_populates="customer")
    __table_args__ = (CheckConstraint("char_length(cpf) = 11", name="cons_cpf_length"),)


__all__ = ["CustomerPersistentModel"]

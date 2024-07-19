from uuid import UUID

from sqlalchemy import exists, or_, select
from sqlalchemy.orm import Session

from src.core.domain.entities.customer import Customer
from src.core.domain.repositories import CustomerRepository
from src.core.domain.value_objects import CPF, Email

from ..persistent_models import CustomerPersistentModel


class SQlAlchemyCustomerRepository(CustomerRepository):
    """Repository for handling customer-related database operations.

    Attributes:
        _session (Session): The database session.
    """

    def __init__(self, session: Session) -> None:
        self._session = session

    def exists(self, cpf: CPF | None, email: Email | None) -> bool:
        """Check if a customer already exists in the database either by cpf, email or both.

        Args:
           cpf: The customer's CPF.
           email: The customer's email.

        Returns:
           bool: True if the customer exists, False otherwise.
        """
        if not cpf and not email:  # Should not happen
            return False

        conditions = []
        if cpf:
            conditions.append(CustomerPersistentModel.cpf == cpf.number)
        if email:
            conditions.append(CustomerPersistentModel.email == email.address)

        stmt = select(exists().where(or_(*conditions)))
        return self._session.execute(stmt).scalar()

    def add(self, customer: Customer) -> Customer:
        """Add a new customer to the database.

        Args:
            customer (Customer): The customer data.

        Returns:
            Customer: The added customer data.
        """
        db_customer = CustomerPersistentModel(
            name=customer.name,
            cpf=customer.cpf.number,
            email=customer.email.address,
            uuid=customer.uuid,
            created_at=customer.created_at,
            updated_at=customer.updated_at,
        )

        self._session.add(db_customer)
        self._session.commit()
        self._session.refresh(db_customer)

        return db_customer.to_entity()

    def get_by_cpf(self, cpf: CPF) -> Customer | None:
        """Get a customer by their CPF.

        Args:
            cpf (CPF): The customer's CPF.

        Returns:
            Customer: The customer data if found, None otherwise.
        """
        customer: CustomerPersistentModel | None = (
            self._session.query(CustomerPersistentModel).filter_by(cpf=cpf.number).first()
        )

        return customer.to_entity() if customer else None

    def get_by_uuid(self, uuid: UUID) -> Customer | None:
        """Get a customer by their UUID.

        Args:
            uuid (UUID): The customer's UUID.

        Returns:
            Customer: The customer data if found, None otherwise.
        """
        customer: CustomerPersistentModel | None = (
            self._session.query(CustomerPersistentModel).filter_by(uuid=uuid).first()
        )

        return customer.to_entity() if customer else None


__all__ = ["SQlAlchemyCustomerRepository"]

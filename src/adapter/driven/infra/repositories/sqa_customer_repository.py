from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from src.adapter.driven.infra.sqa_models import CustomerPersistentModel
from src.core.domain.entities.customer import Customer
from src.core.domain.repositories import CustomerRepository
from src.core.domain.value_objects import CPF, Email


class SQACustomerRepository(CustomerRepository):
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

        Raises:
           DomainError: If both CPF and email are not provided.
        """
        query = select(CustomerPersistentModel).where(
            or_(
                CustomerPersistentModel.cpf == cpf.number,
                CustomerPersistentModel.email == email.address,
            )
        )
        return self._session.execute(query).scalar() is not None

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

        customer.id = db_customer.id
        customer.created_at = db_customer.created_at
        customer.updated_at = db_customer.updated_at
        customer.uuid = db_customer.uuid

        return customer

    def get_by_cpf(self, cpf: CPF) -> Customer | None:
        """Get a customer by their CPF.

        Args:
            cpf (CPF): The customer's CPF.

        Returns:
            Customer: The customer data if found, None otherwise.
        """
        query = select(CustomerPersistentModel).where(CustomerPersistentModel.cpf == cpf.number)
        customer: CustomerPersistentModel | None = self._session.execute(query).scalar()

        if customer is None:
            return None

        return Customer(
            name=customer.name,
            cpf=CPF(customer.cpf),
            email=Email(customer.email),
            _id=customer.id,
            uuid=customer.uuid,
            created_at=customer.created_at,
            updated_at=customer.updated_at,
        )


__all__ = ["SQACustomerRepository"]

from datetime import datetime
from uuid import UUID

import pytest

from src.core.domain.entities import Customer
from src.core.domain.exceptions import DomainError
from src.core.domain.value_objects import CPF, Email
from tests.factories import CPFProvider


def test_customer_creation_successful() -> None:
    """Test successful customer creation."""
    name = "John Doe"
    cpf = CPF(CPFProvider.generate_cpf_number())
    email = Email("john.doe@example.com")

    customer = Customer(name=name, cpf=cpf, email=email)

    assert customer.name == name
    assert customer.cpf == cpf
    assert customer.email == email


def test_customer_creation_with_id_uuid_timestamps() -> None:
    """Test customer creation with optional parameters."""
    name = "Jane Smith"
    cpf = CPF(CPFProvider.generate_cpf_number())
    email = Email("jane.smith@example.com")
    _id = 1
    uuid = UUID("12345678-1234-5678-1234-567812345678")
    created_at = datetime.now()
    updated_at = datetime.now()

    customer = Customer(
        name=name,
        cpf=cpf,
        email=email,
        _id=_id,
        uuid=uuid,
        created_at=created_at,
        updated_at=updated_at,
    )

    assert customer._id == _id
    assert customer.uuid == uuid
    assert customer.created_at == created_at
    assert customer.updated_at == updated_at


@pytest.mark.parametrize("name", [None, "", "    "])
def test_customer_creation_with_missing_name(name: str | None) -> None:
    cpf_str = CPFProvider.generate_cpf_number()

    with pytest.raises(DomainError) as exec_info:
        Customer(name=name, cpf=CPF(cpf_str), email=Email("john.doe@example.com"))

    assert exec_info.value.message == "Name is required"


def test_customer_creation_with_missing_cpf() -> None:
    with pytest.raises(DomainError) as exec_info:
        Customer(
            name="John Doe",
            cpf=None,  # type: ignore
            email=Email("john.doe@example.com"),
        )

    assert exec_info.value.message == "CPF is required"


def test_customer_creation_with_missing_email() -> None:
    with pytest.raises(DomainError) as exec_info:
        Customer(
            name="John Doe",
            cpf=CPF(CPFProvider.generate_cpf_number()),
            email=None,  # type: ignore
        )

    assert exec_info.value.message == "Email is required"

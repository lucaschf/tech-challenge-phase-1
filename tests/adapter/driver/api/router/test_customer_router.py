from unittest.mock import ANY

import pytest
from fastapi.testclient import TestClient

from src.adapter.driver.api.schemas import CustomerCreationIn
from tests.factories import CPFProvider
from tests.factories.adapter.driver.api.schemas import CustomerCreationInFactory


def test_create_customer_should_create(client: TestClient) -> None:
    customer_data: CustomerCreationIn = CustomerCreationInFactory()

    response = client.post("/api/customer", json=customer_data.model_dump())

    assert response.status_code == 201

    assert response.headers["location"] == f"/customer/{customer_data.cpf}"
    assert response.json() == {
        "name": customer_data.name,
        "email": customer_data.email,
        "cpf": customer_data.cpf,
        "uuid": ANY,
        "created_at": ANY,
        "updated_at": ANY,
    }


def test_create_customer_should_raise_error_if_customer_already_exists(client: TestClient) -> None:
    customer_data: CustomerCreationIn = CustomerCreationInFactory()

    client.post("/api/customer", json=customer_data.model_dump())
    response = client.post("/api/customer", json=customer_data.model_dump())

    assert response.status_code == 400
    assert response.json() == {"detail": "Customer already exists"}


def test_get_customer_should_return_customer(client: TestClient) -> None:
    customer_data: CustomerCreationIn = CustomerCreationInFactory()
    client.post("/api/customer", json=customer_data.model_dump())

    response = client.get(f"/api/customer/{customer_data.cpf}")

    assert response.status_code == 200
    assert response.json() == {
        "name": customer_data.name,
        "email": customer_data.email,
        "cpf": customer_data.cpf,
        "uuid": ANY,
        "created_at": ANY,
        "updated_at": ANY,
    }


def test_get_customer_should_return_404_if_not_found(client: TestClient) -> None:
    cpf = CPFProvider.generate_cpf_number()
    response = client.get(f"/api/customer/{cpf}")

    assert response.status_code == 404
    assert response.json() == {"detail": f"Customer with CPF '{cpf}' not found."}


def test_create_customer_should_create_with_valid_location_header(client: TestClient) -> None:
    customer_data: CustomerCreationIn = CustomerCreationInFactory()

    response = client.post("/api/customer", json=customer_data.model_dump())
    assert response.status_code == 201
    assert response.headers["location"] == f"/customer/{customer_data.cpf}"

    get_response = client.get(f"/api{response.headers['location']}")
    assert get_response.status_code == 200
    assert get_response.json() == {
        "name": customer_data.name,
        "email": customer_data.email,
        "cpf": customer_data.cpf,
        "uuid": ANY,
        "created_at": ANY,
        "updated_at": ANY,
    }


@pytest.mark.parametrize("cpf", ["12345678901", "12345", ["a" * 11]])
def test_get_customer_should_return_422_if_invalid_cpf_informed(
    client: TestClient,
    cpf: str | None,
) -> None:
    response = client.get(f"/api/customer/{cpf}")

    assert response.status_code == 422

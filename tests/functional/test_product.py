import pytest
from fastapi.testclient import TestClient

from src.adapter.driver.api.schemas.product_schema import ProductCreationIn
from tests.factories.adapter.driver.api.schemas import ProductCreationInFactory


@pytest.mark.parametrize(
    "replace_key, replace_value",
    [("name", ""), ("category", ""), ("price", -1), ("description", ""), ("images", [])],
)
def test_product_creation_returns_error_if_any_invalid_field_informed(
    replace_key: str, replace_value: str | int | float | list[str], client: TestClient
) -> None:
    product_data: ProductCreationIn = ProductCreationInFactory()
    input_data = product_data.model_dump()

    input_data[replace_key] = replace_value
    response = client.post("/api/products", json=input_data)

    assert response.status_code == 422


def test_create_product(client: TestClient) -> None:
    product_data: ProductCreationIn = ProductCreationInFactory()

    response = client.post("/api/products", json=product_data.model_dump())

    assert response.status_code == 201
    assert response.json()["name"] == product_data.name


def test_update_product(client: TestClient) -> None:
    # First, create a product to update
    product_data: ProductCreationIn = ProductCreationInFactory()

    create_response = client.post("/api/products", json=product_data.model_dump())
    product_uuid = create_response.json()["uuid"]

    updated_product_data: ProductCreationIn = ProductCreationInFactory()
    update_response = client.put(
        f"/api/products/{product_uuid}", json=updated_product_data.model_dump()
    )

    assert update_response.status_code == 200
    assert update_response.json()["name"] == updated_product_data.name


def test_delete_product(client: TestClient) -> None:
    # First, create a product to delete
    product_data: ProductCreationIn = ProductCreationInFactory()
    create_response = client.post("/api/products", json=product_data.model_dump())
    product_id = create_response.json()["uuid"]

    delete_response = client.delete(f"/api/products/{product_id}")

    assert delete_response.status_code == 204


def test_get_products_by_category(client: TestClient) -> None:
    product_data: ProductCreationIn = ProductCreationInFactory()
    client.post("/api/products", json=product_data.model_dump())
    response = client.get("/api/products", params={"category": product_data.category})

    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()[0]["category"] == product_data.category

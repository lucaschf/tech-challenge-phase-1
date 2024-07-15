from unittest.mock import ANY

from fastapi.testclient import TestClient

from src.adapter.driver.api.schemas.order_schema import OrderIn
from tests.factories.adapter.driver.api.schemas.order_schema_factory import (
    OrderInFactory,
    OrderItemInFactory,
)


def test_checkout(
    client: TestClient,
    create_customer_in_db,  # noqa: ANN001
    create_products_in_db,  # noqa: ANN001
) -> None:
    customer = create_customer_in_db
    products = create_products_in_db

    order_products = [OrderItemInFactory(product_id=product.uuid) for product in products]
    order_data: OrderIn = OrderInFactory(customer_id=customer.uuid, items=order_products)

    response = client.post("/api/orders/checkout", json=order_data.model_dump(mode="json"))

    assert response.status_code == 201
    assert response.json() == {"number": ANY}


def test_list_orders(
    client: TestClient,
    create_customer_in_db,  # noqa: ANN001
    create_products_in_db,  # noqa: ANN001
) -> None:
    customer = create_customer_in_db
    products = create_products_in_db

    order_products = [OrderItemInFactory(product_id=product.uuid) for product in products]
    order_data: OrderIn = OrderInFactory(customer_id=customer.uuid, items=order_products)

    client.post("/api/orders/checkout", json=order_data.model_dump(mode="json"))

    response = client.get("/api/orders")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_update_order_status(
    client: TestClient,
    create_customer_in_db,  # noqa: ANN001
    create_products_in_db,  # noqa: ANN001
) -> None:
    customer = create_customer_in_db
    products = create_products_in_db

    order_products = [OrderItemInFactory(product_id=product.uuid) for product in products]
    order_data: OrderIn = OrderInFactory(customer_id=customer.uuid, items=order_products)

    create_response = client.post("/api/orders/checkout", json=order_data.model_dump(mode="json"))
    order_uuid = create_response.json()["number"]

    update_response = client.put(f"/api/orders/{order_uuid}/status", json={"status": "completed"})

    assert update_response.status_code == 200
    assert update_response.json()["status"] == "completed"

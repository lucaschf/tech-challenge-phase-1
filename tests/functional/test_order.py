from fastapi.testclient import TestClient

from src.adapter.driver.api.schemas.order_schema import OrderIn
from tests.factories.adapter.driver.api.schemas.order_schema_factory import (
    OrderInFactory,
    OrderProductInFactory,
)


def test_checkout(client: TestClient, create_customer_in_db, create_products_in_db) -> None:  # noqa: ANN001
    customer = create_customer_in_db
    products = create_products_in_db

    order_products = [OrderProductInFactory(product_uuid=product.uuid) for product in products]
    order_data = OrderInFactory(user_uuid=customer.uuid, products=order_products)
    order_data: OrderIn = OrderInFactory(user_uuid=customer.uuid, products=order_products)
    response = client.post("/api/orders/checkout", json=order_data.model_dump(mode="json"))
    assert response.status_code == 200
    assert response.json()["user_uuid"] == str(order_data.user_uuid)
    assert response.json()["status"] == "pending"


def test_list_orders(client: TestClient, create_customer_in_db, create_products_in_db) -> None:  # noqa: ANN001
    customer = create_customer_in_db
    products = create_products_in_db

    order_products = [OrderProductInFactory(product_uuid=product.uuid) for product in products]
    order_data = OrderInFactory(user_uuid=customer.uuid, products=order_products)
    order_data: OrderIn = OrderInFactory(user_uuid=customer.uuid, products=order_products)

    client.post("/api/orders/checkout", json=order_data.model_dump(mode="json"))

    response = client.get("/api/orders")

    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()[0]["user_uuid"] == str(order_data.user_uuid)


def test_update_order_status(
    client: TestClient,
    create_customer_in_db,  # noqa: ANN001
    create_products_in_db,  # noqa: ANN001
) -> None:
    customer = create_customer_in_db
    products = create_products_in_db

    order_products = [OrderProductInFactory(product_uuid=product.uuid) for product in products]
    order_data = OrderInFactory(user_uuid=customer.uuid, products=order_products)
    order_data: OrderIn = OrderInFactory(user_uuid=customer.uuid, products=order_products)

    create_response = client.post("/api/orders/checkout", json=order_data.model_dump(mode="json"))
    order_uuid = create_response.json()["uuid"]

    update_response = client.put(f"/api/orders/{order_uuid}/status", json={"status": "completed"})

    assert update_response.status_code == 200
    assert update_response.json()["status"] == "completed"

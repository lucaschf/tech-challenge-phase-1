from fastapi.testclient import TestClient

from src.adapter.driver.api.schemas.order_schema import OrderIn
from tests.factories.adapter.driver.api.schemas import OrderInFactory


def test_checkout(client: TestClient) -> None:
    order_data: OrderIn = OrderInFactory()

    response = client.post("/api/orders/checkout", json=order_data.model_dump(mode="json"))

    assert response.status_code == 201
    assert response.json()["user_id"] == str(order_data.user_id)
    assert response.json()["products"] == order_data.products
    assert response.json()["status"] == "pending"


def test_list_orders(client: TestClient) -> None:
    order_data: OrderIn = OrderInFactory()
    client.post("/api/orders/checkout", json=order_data.model_dump(mode="json"))

    response = client.get("/api/orders")

    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()[0]["user_id"] == str(order_data.user_id)
    assert response.json()[0]["products"] == order_data.products


def test_update_order_status(client: TestClient) -> None:
    order_data: OrderIn = OrderInFactory()
    create_response = client.post("/api/orders/checkout", json=order_data.model_dump(mode="json"))
    order_id = create_response.json()["id"]

    update_response = client.put(f"/orders/{order_id}/status", json={"status": "completed"})

    assert update_response.status_code == 200
    assert update_response.json()["status"] == "completed"

from fastapi.testclient import TestClient


def test_create_product(client: TestClient) -> None:
    product_data = {
        "name": "Sandwich",
        "category": "Lanche",
        "price": 5.99,
        "description": "A delicious sandwich",
        "images": ["http://example.com/sandwich.jpg"],
    }
    response = client.post("/api/products", json=product_data)
    assert response.status_code == 201
    assert response.json()["name"] == product_data["name"]


def test_update_product(client: TestClient) -> None:
    # First, create a product to update
    product_data = {
        "name": "Sandwich",
        "category": "Lanche",
        "price": 5.99,
        "description": "A delicious sandwich",
        "images": ["http://example.com/sandwich.jpg"],
    }
    create_response = client.post("/api/products", json=product_data)
    product_uuid = create_response.json()["uuid"]

    updated_product_data = {
        "name": "Updated Sandwich",
        "category": "Lanche",
        "price": 6.99,
        "description": "An updated delicious sandwich",
        "images": ["http://example.com/updated_sandwich.jpg"],
    }
    update_response = client.put(f"/api/products/{product_uuid}", json=updated_product_data)

    assert update_response.status_code == 200
    assert update_response.json()["name"] == updated_product_data["name"]


def test_delete_product(client: TestClient) -> None:
    # First, create a product to delete
    product_data = {
        "name": "Sandwich",
        "category": "Lanche",
        "price": 5.99,
        "description": "A delicious sandwich",
        "images": ["http://example.com/sandwich.jpg"],
    }
    create_response = client.post("/api/products", json=product_data)
    product_id = create_response.json()["uuid"]

    delete_response = client.delete(f"/api/products/{product_id}")
    assert delete_response.status_code == 204


def test_get_products_by_category(client: TestClient) -> None:
    product_data = {
        "name": "Sandwich",
        "category": "Lanche",
        "price": 5.99,
        "description": "A delicious sandwich",
        "images": ["http://example.com/sandwich.jpg"],
    }
    client.post("/api/products", json=product_data)
    response = client.get("/api/products", params={"category": "Lanche"})
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()[0]["category"] == "Lanche"

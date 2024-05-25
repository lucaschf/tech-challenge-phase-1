from fastapi.testclient import TestClient
from httpx import Client


def test_create_product(client: TestClient) -> None:
    product_data = {
        "name": "Sandwich",
        "category": "Lanche",
        "price": 5.99,
        "description": "A delicious sandwich",
        "images": ["http://example.com/sandwich.jpg"],
    }
    with Client(app=client.app, base_url="http://test") as ac:
        response = ac.post("/api/products", json=product_data)
    assert response.status_code == 200
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
    with Client(app=client.app, base_url="http://test") as ac:
        create_response = ac.post("/api/products", json=product_data)
        product_id = create_response.json()["id"]

    # Update the product
    updated_product_data = {
        "name": "Updated Sandwich",
        "category": "Lanche",
        "price": 6.99,
        "description": "An updated delicious sandwich",
        "images": ["http://example.com/updated_sandwich.jpg"],
    }
    with Client(app=client.app, base_url="http://test") as ac:
        update_response = ac.put(f"/api/products/{product_id}", json=updated_product_data)
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
    with Client(app=client.app, base_url="http://test") as ac:
        create_response = ac.post("/api/products", json=product_data)
        product_id = create_response.json()["id"]

    # Delete the product
    with Client(app=client.app, base_url="http://test") as ac:
        delete_response = ac.delete(f"/api/products/{product_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["detail"] == "Product deleted"


def test_get_products_by_category(client: TestClient) -> None:
    product_data = {
        "name": "Sandwich",
        "category": "Lanche",
        "price": 5.99,
        "description": "A delicious sandwich",
        "images": ["http://example.com/sandwich.jpg"],
    }
    with Client(app=client.app, base_url="http://test") as ac:
        # Create a product to ensure there is data
        ac.post("/api/products", json=product_data)
        # Retrieve products by category
        response = ac.get("/api/products", params={"category": "Lanche"})
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()[0]["category"] == "Lanche"

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_product(client: TestClient) -> None:
    product_data = {
        "name": "Sandwich",
        "category": "Lanche",
        "price": 5.99,
        "description": "A delicious sandwich",
        "images": ["http://example.com/sandwich.jpg"],
    }
    async with AsyncClient(app=client.app, base_url="http://test") as ac:
        response = await ac.post("/api/products", json=product_data)
    assert response.status_code == 200
    assert response.json()["name"] == product_data["name"]


@pytest.mark.asyncio
async def test_update_product(client: TestClient) -> None:
    # First, create a product to update
    product_data = {
        "name": "Sandwich",
        "category": "Lanche",
        "price": 5.99,
        "description": "A delicious sandwich",
        "images": ["http://example.com/sandwich.jpg"],
    }
    async with AsyncClient(app=client.app, base_url="http://test") as ac:
        create_response = await ac.post("/api/products", json=product_data)
        product_id = create_response.json()["id"]

    # Update the product
    updated_product_data = {
        "name": "Updated Sandwich",
        "category": "Lanche",
        "price": 6.99,
        "description": "An updated delicious sandwich",
        "images": ["http://example.com/updated_sandwich.jpg"],
    }
    async with AsyncClient(app=client.app, base_url="http://test") as ac:
        update_response = await ac.put(f"/api/products/{product_id}", json=updated_product_data)
    assert update_response.status_code == 200
    assert update_response.json()["name"] == updated_product_data["name"]


@pytest.mark.asyncio
async def test_delete_product(client: TestClient) -> None:
    # First, create a product to delete
    product_data = {
        "name": "Sandwich",
        "category": "Lanche",
        "price": 5.99,
        "description": "A delicious sandwich",
        "images": ["http://example.com/sandwich.jpg"],
    }
    async with AsyncClient(app=client.app, base_url="http://test") as ac:
        create_response = await ac.post("/api/products", json=product_data)
        product_id = create_response.json()["id"]

    # Delete the product
    async with AsyncClient(app=client.app, base_url="http://test") as ac:
        delete_response = await ac.delete(f"/api/products/{product_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["detail"] == "Product deleted"


@pytest.mark.asyncio
async def test_get_products_by_category(client: TestClient) -> None:
    product_data = {
        "name": "Sandwich",
        "category": "Lanche",
        "price": 5.99,
        "description": "A delicious sandwich",
        "images": ["http://example.com/sandwich.jpg"],
    }
    async with AsyncClient(app=client.app, base_url="http://test") as ac:
        # Create a product to ensure there is data
        await ac.post("/api/products", json=product_data)
        # Retrieve products by category
        response = await ac.get("/api/products", params={"category": "Lanche"})
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()[0]["category"] == "Lanche"

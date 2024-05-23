from typing import List

from sqlalchemy import delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.core.domain.entities.product import Product
from src.core.domain.repositories.product_repository import ProductRepository


class SQLAlchemyProductRepository(ProductRepository):
    """Implementation of the ProductRepository using SQLAlchemy.

    This repository uses an asynchronous SQLAlchemy session to perform CRUD operations on products.
    """

    def __init__(self, session: AsyncSession) -> None:
        """Initializes the SQLAlchemyProductRepository with a given session.

        Args:
            session (AsyncSession): The SQLAlchemy session to use for database operations.
        """
        self.session = session

    async def create(self, product: Product) -> Product:
        """Creates a new product in the repository.

        Args:
            product (Product): The product to be created.

        Returns:
            Product: The created product with its ID and other persistence details populated.
        """
        async with self.session() as session:
            session.add(product)
            await session.commit()
            return product

    async def update(self, product_id: int, product: Product) -> Product:
        """Updates an existing product in the repository.

        Args:
            product_id (int): The ID of the product to be updated.
            product (Product): The product data to update.

        Returns:
            Product: The updated product.
        """
        async with self.session() as session:
            await session.execute(update(Product).where(Product.id == product_id).values(product))
            await session.commit()
            return product

    async def delete(self, product_id: int) -> None:
        """Deletes a product from the repository.

        Args:
            product_id (int): The ID of the product to be deleted.

        Returns:
            None
        """
        async with self.session() as session:
            await session.execute(delete(Product).where(Product.id == product_id))
            await session.commit()

    async def get_by_category(self, category: str) -> List[Product]:
        """Retrieves all products in a given category.

        Args:
            category (str): The category to filter products by.

        Returns:
            List[Product]: A list of products in the specified category.
        """
        async with self.session() as session:
            result = await session.execute(select(Product).where(Product.category == category))
            return result.scalars().all()

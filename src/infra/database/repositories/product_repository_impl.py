from typing import List, Set
from uuid import UUID

from sqlalchemy import delete, update
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from sqlalchemy.sql.operators import eq

from src.core.domain.entities import Product
from src.core.domain.repositories.product_repository import ProductRepository
from src.core.domain.value_objects import Category

from ..persistent_models.product_persistent_model import ProductPersistentModel


class SQLAlchemyProductRepository(ProductRepository):
    """Implementation of the ProductRepository using SQLAlchemy.

    This repository uses an SQLAlchemy session to perform CRUD operations on products.
    """

    def __init__(self, session: Session) -> None:
        """Initializes the SQLAlchemyProductRepository with a given session.

        Args:
            session (Session): The SQLAlchemy session to use for database operations.
        """
        self._session = session

    def create(self, product: Product) -> Product:
        """Creates a new product in the repository.

        Args:
            product (Product): The product to be created.

        Returns:
            Product: The created product with its ID and other persistence details populated.
        """
        db_product = ProductPersistentModel(
            name=product.name,
            category=product.category,
            price=product.price,
            description=product.description,
            images=product.images,
        )
        with self._session as session:
            session.add(db_product)
            session.commit()
            product._id = db_product.id
            product.created_at = db_product.created_at
            product.updated_at = db_product.updated_at
            product.uuid = db_product.uuid
            return product

    def update(self, product_uuid: UUID, product: Product) -> Product:
        """Updates an existing product in the repository.

        Args:
            product_uuid (uuid): The ID of the product to be updated.
            product (Product): The product data to update.

        Returns:
            Product: The updated product.
        """
        product_dict = {
            "name": product.name,
            "category": product.category
            if isinstance(product.category, str)
            else product.category.category,
            "price": product.price,
            "description": product.description,
            "images": product.images,
        }
        with self._session as session:
            session.execute(
                update(ProductPersistentModel)
                .where(ProductPersistentModel.uuid == product_uuid)
                .values(product_dict)
            )
            session.commit()
            updated_product = session.execute(
                select(ProductPersistentModel).where(ProductPersistentModel.uuid == product_uuid)
            ).scalar_one()

        return Product(
            _id=updated_product.id,
            uuid=updated_product.uuid,
            name=updated_product.name,
            category=Category(updated_product.category),
            price=updated_product.price,
            description=updated_product.description,
            images=updated_product.images,
            created_at=updated_product.created_at,
            updated_at=updated_product.updated_at,
        )

    def delete(self, product_uuid: UUID) -> None:
        """Deletes a product from the repository.

        Args:
            product_uuid (uuid): The ID of the product to be deleted.

        Returns:
            None
        """
        with self._session as session:
            session.execute(
                delete(ProductPersistentModel).where(ProductPersistentModel.uuid == product_uuid)
            )
            session.commit()

    def get_by_category(self, category: str) -> List[Product]:
        """Retrieves all products in a given category.

        Args:
            category (str): The category to filter products by.

        Returns:
            List[Product]: A list of products in the specified category.
        """
        with self._session as session:
            result = session.execute(
                select(ProductPersistentModel).where(ProductPersistentModel.category == category)
            )
            return result.scalars().all()

    def get_by_name(self, name: str) -> Product | None:
        """Retrieves a product by its name.

        Args:
            name (str): The name of the product to retrieve.

        Returns:
            Product: The product with the specified name.
        """
        result = (
            self._session.query(ProductPersistentModel)
            .filter(ProductPersistentModel.name.ilike(name))
            .first()
        )

        if result is None:
            return None

        return Product(
            _id=result.id,
            uuid=result.uuid,
            name=result.name,
            category=Category(result.category),
            price=result.price,
            description=result.description,
            images=result.images,
            created_at=result.created_at,
            updated_at=result.updated_at,
        )

    def get_by_uuids(self, product_uuids: Set[UUID]) -> List[Product]:
        """Retrieves a list of products by their UUIDs.

        Args:
            product_uuids: The UUIDs of the products to retrieve.

        Returns:
            List[Product]: A list of products with the specified UUIDs.
        """
        result = (
            self._session.execute(
                select(ProductPersistentModel).where(ProductPersistentModel.uuid.in_(product_uuids))
            )
            .scalars()
            .all()
        )

        return [p.to_entity() for p in result]

    def get_by_uuid(self, product_uuid: UUID) -> Product | None:
        """Retrieves a product by its UUID.

        Args:
            product_uuid (UUID): The UUID of the product to retrieve.

        Returns:
            Product: The product with the specified UUID.
        """
        result: ProductPersistentModel | None = (
            self._session.query(ProductPersistentModel)
            .filter(eq(ProductPersistentModel.uuid, product_uuid))
            .first()
        )

        if result is None:
            return None

        return result.to_entity()


__all__ = ["SQLAlchemyProductRepository"]

from typing import Iterable, Set
from uuid import UUID

from sqlalchemy import delete
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

        self._session.add(db_product)
        self._session.commit()
        self._session.refresh(db_product)

        return db_product.to_entity()

    def update(self, product_uuid: UUID, product: Product) -> Product | None:
        """Updates an existing product in the repository.

        Args:
            product_uuid: The ID of the product to be updated.
            product: The product data to update.

        Returns:
            The updated product, None if no product meets the criteria.
        """
        db_product: ProductPersistentModel | None = (
            self._session.query(ProductPersistentModel).filter_by(uuid=product_uuid).first()
        )

        if db_product is None:
            return None

        db_product.name = product.name
        db_product.category = product.category
        db_product.price = product.price
        db_product.description = product.description
        db_product.images = product.images

        self._session.commit()
        self._session.refresh(db_product)
        return db_product.to_entity()

    def delete(self, product_uuid: UUID) -> None:
        """Deletes a product from the repository.

        Args:
            product_uuid (uuid): The ID of the product to be deleted.

        Returns:
            None
        """
        self._session.execute(
            delete(ProductPersistentModel).where(eq(ProductPersistentModel.uuid, product_uuid))
        )
        self._session.commit()

    def get_by_category(self, category: Category) -> Iterable[Product]:
        """Retrieves all products in a given category.

        Args:
            category (str): The category to filter products by.

        Returns:
            List[Product]: A list of products in the specified category.
        """
        result = (
            self._session.query(ProductPersistentModel)
            .filter(eq(ProductPersistentModel.category, category))
            .all()
        )

        return [p.to_entity() for p in result]

    def get_by_name(self, name: str) -> Product | None:
        """Retrieves a product by its name.

        Args:
            name (str): The name of the product to retrieve.

        Returns:
            Product: The product with the specified name.
        """
        result: ProductPersistentModel | None = (
            self._session.query(ProductPersistentModel)
            .filter(ProductPersistentModel.name.ilike(name))
            .first()
        )

        if result is None:
            return None

        return result.to_entity()

    def get_by_uuids(self, product_uuids: Set[UUID]) -> Iterable[Product]:
        """Retrieves products by their UUIDs.

        Args:
            product_uuids: The UUIDs of the products to retrieve.

        Returns:
            An iterable collection of products.
        """
        result = (
            self._session.query(ProductPersistentModel)
            .filter(ProductPersistentModel.uuid.in_(product_uuids))
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

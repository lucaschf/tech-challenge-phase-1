import pytest
from fastapi.testclient import TestClient
from sqlalchemy import MetaData, delete

from src.api import app
from src.core.domain.entities import Customer, Product
from src.infra.database.config.database import Session, engine, get_db_session
from src.infra.database.repositories import (
    SQlAlchemyCustomerRepository,
    SQLAlchemyProductRepository,
)
from tests.factories.core.domain.entities.customer_factory import CustomerFactory
from tests.factories.core.domain.entities.product_factory import ProductFactory


@pytest.fixture
def client():  # noqa: ANN201
    with TestClient(app) as c:
        yield c


@pytest.fixture
def db_session() -> Session:
    session = next(get_db_session())
    metadata = MetaData()
    metadata.reflect(bind=engine)
    for table in reversed(metadata.sorted_tables):
        if table.name != "alembic_version":
            session.execute(delete(table))
    session.commit()

    yield session
    session.close()


@pytest.fixture
def create_customer_in_db(db_session: Session):  # noqa: ANN201
    customer_data = CustomerFactory()
    customer_repo = SQlAlchemyCustomerRepository(db_session)
    customer = customer_repo.add(
        Customer(name=customer_data.name, email=customer_data.email, cpf=customer_data.cpf)
    )
    db_session.commit()
    return customer


@pytest.fixture
def create_products_in_db(db_session: Session, num_products: int = 2):  # noqa: ANN201
    product_repo = SQLAlchemyProductRepository(db_session)
    products = []
    for _ in range(num_products):
        product_data = ProductFactory()
        product = product_repo.create(
            Product(
                name=product_data.name,
                category=product_data.category,
                price=product_data.price,
                description=product_data.description,
                images=product_data.images,
            )
        )
        products.append(product)
    db_session.commit()
    return products

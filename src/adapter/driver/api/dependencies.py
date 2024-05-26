from fastapi import Depends
from injector import Injector, Module, provider
from sqlalchemy.orm import Session

from src.adapter.driven.infra.config.database import get_db_session
from src.adapter.driven.infra.repositories import SQACustomerRepository
from src.adapter.driven.infra.repositories.product_repository_impl import (
    SQLAlchemyProductRepository,
)
from src.adapter.driver.api.controllers import CustomerController
from src.core.application.use_cases import CustomerUseCase, CustomerUseCaseImpl
from src.core.application.use_cases.product_use_case import ProductUseCase
from src.core.domain.repositories import CustomerRepository
from src.core.domain.repositories.product_repository import ProductRepository

from .controllers import ProductController


class AppModule(Module):
    """AppModule is a class that provides the dependencies for the application.

    It uses the provider decorator from the injector package to specify how to provide each
     dependency.
    """

    @provider
    def provide_session(self) -> Session:
        """Provides an SQLAlchemy session using the get_db_session function."""
        return next(get_db_session())

    @provider
    def provide_customer_repository(
        self,
        session: Session = Depends(),  # noqa: B008
    ) -> CustomerRepository:
        """Provides a CustomerRepository instance.

        It depends on an SQLAlchemy session, which is injected by FastAPI's "Depends" mechanism.
        """
        return SQACustomerRepository(session)

    @provider
    def provide_customer_use_case(
        self,
        customer_repository: CustomerRepository = Depends(),  # noqa: B008
    ) -> CustomerUseCase:
        """Provides a CustomerUseCase instance.

        It depends on a CustomerRepository, which is injected by FastAPI's "Depends" mechanism.
        """
        return CustomerUseCaseImpl(customer_repository)

    @provider
    def provide_customer_controller(
        self,
        customer_use_case: CustomerUseCase = Depends(),  # noqa: B008
    ) -> CustomerController:
        """Provides a CustomerController instance.

        It depends on a CustomerUseCase, which is injected by FastAPI's "Depends" mechanism.
        """
        return CustomerController(customer_use_case)

    @provider
    def provide_product_repository(
        self,
        session: Session = Depends(),  # noqa: B008
    ) -> ProductRepository:
        """Provides a ProductRepository instance.

        It depends on an SQLAlchemy session, which is injected by FastAPI's "Depends" mechanism.
        """
        return SQLAlchemyProductRepository(session)

    @provider
    def provide_product_use_case(
        self,
        product_repository: ProductRepository = Depends(),  # noqa: B008
    ) -> ProductUseCase:
        """Provides a ProductUseCase instance.

        It depends on a ProductRepository, which is injected by FastAPI's "Depends" mechanism.
        """
        return ProductUseCase(product_repository)

    @provider
    def provide_product_controller(
        self,
        product_use_case: ProductUseCase = Depends(),  # noqa: B008
    ) -> ProductController:
        """Provides a ProductController instance.

        It depends on a ProductUseCase, which is injected by FastAPI's "Depends" mechanism.
        """
        return ProductController(product_use_case)


def configure_injector(binder) -> None:  # noqa: ANN001
    """Configures the injector by installing the AppModule."""
    binder.install(AppModule())


# Create an instance of Injector with the configure_injector function.
injector = Injector([configure_injector])

__all__ = ["injector"]

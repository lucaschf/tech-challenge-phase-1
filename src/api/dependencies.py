from fastapi import Depends
from injector import Injector, Module, provider
from sqlalchemy.orm import Session

from src.api.controllers import CustomerController, OrderController
from src.core.domain.repositories import CustomerRepository, OrderRepository, ProductRepository
from src.core.use_cases import (
    CheckoutUseCase,
    CreateCustomerUseCase,
    GetCustomerByCpfUseCase,
    ListOrdersUseCase,
    ProductCreationUseCase,
    ProductUseCase,
    UpdateOrderStatusUseCase,
)
from src.infra.database.config import get_db_session
from src.infra.database.repositories import (
    SQlAlchemyCustomerRepository,
    SQLAlchemyOrderRepository,
    SQLAlchemyProductRepository,
)

from ..core.use_cases.product import ProductUpdateUseCase
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
        return SQlAlchemyCustomerRepository(session)

    @provider
    def provide_create_customer_use_case(
        self,
        customer_repository: CustomerRepository = Depends(),  # noqa: B008
    ) -> CreateCustomerUseCase:
        """Provides a CreateCustomerUseCase instance.

        It depends on a CustomerRepository, which is injected by FastAPI's "Depends" mechanism.
        """
        return CreateCustomerUseCase(customer_repository)

    @provider
    def provide_get_customer_by_cpf_use_case(
        self,
        customer_repository: CustomerRepository = Depends(),  # noqa: B008
    ) -> GetCustomerByCpfUseCase:
        """Provides a GetCustomerByCpfUseCase instance.

        It depends on a CustomerRepository, which is injected by FastAPI's "Depends" mechanism.
        """
        return GetCustomerByCpfUseCase(customer_repository)

    @provider
    def provide_customer_controller(
        self,
        create_customer_use_case: CreateCustomerUseCase = Depends(),  # noqa: B008
        get_customer_by_cpf_use_case: GetCustomerByCpfUseCase = Depends(),  # noqa: B008
    ) -> CustomerController:
        """Provides a CustomerController instance.

        It depends on a CustomerUseCase, which is injected by FastAPI's "Depends" mechanism.
        """
        return CustomerController(create_customer_use_case, get_customer_by_cpf_use_case)

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
    def provide_product_creation_use_case(
        self,
        product_repository: ProductRepository = Depends(),  # noqa: B008
    ) -> ProductCreationUseCase:
        """Provides a ProductCreationUseCase instance.

        It depends on a ProductRepository, which is injected by FastAPI's "Depends" mechanism.
        """
        return ProductCreationUseCase(product_repository)

    @provider
    def provide_product_update_use_case(
        self,
        product_repository: ProductRepository = Depends(),  # noqa: B008
    ) -> ProductUpdateUseCase:
        """Provides a ProductUpdateUseCase instance.

        It depends on a ProductRepository, which is injected by FastAPI's "Depends" mechanism.
        """
        return ProductUpdateUseCase(product_repository)

    @provider
    def provide_product_controller(
        self,
        product_use_case: ProductUseCase = Depends(),  # noqa: B008
        product_creation_use_case: ProductCreationUseCase = Depends(),  # noqa: B008
        product_update_use_case: ProductUpdateUseCase = Depends(),  # noqa: B008
    ) -> ProductController:
        """Provides a ProductController instance.

        It depends on a ProductUseCase, which is injected by FastAPI's "Depends" mechanism.
        """
        return ProductController(
            product_use_case, product_creation_use_case, product_update_use_case
        )

    @provider
    def provide_order_repository(
        self,
        session: Session = Depends(),  # noqa: B008
    ) -> OrderRepository:
        return SQLAlchemyOrderRepository(session)

    @provider
    def provide_checkout_use_case(
        self,
        order_repository: OrderRepository = Depends(),  # noqa: B008
        customer_repository: CustomerRepository = Depends(),  # noqa: B008
        product_repository: ProductRepository = Depends(),  # noqa: B008
    ) -> CheckoutUseCase:
        """Provides a CheckoutUseCase instance."""
        return CheckoutUseCase(
            order_repository,
            customer_repository,
            product_repository,
        )

    @provider
    def provide_list_orders_use_case(
        self,
        order_repository: OrderRepository = Depends(),  # noqa: B008
    ) -> ListOrdersUseCase:
        """Provides a ListOrdersUseCase instance."""
        return ListOrdersUseCase(order_repository)

    @provider
    def provide_update_order_status_use_case(
        self,
        order_repository: OrderRepository = Depends(),  # noqa: B008
    ) -> UpdateOrderStatusUseCase:
        """Provides an UpdateOrderStatusUseCase instance."""
        return UpdateOrderStatusUseCase(order_repository)

    @provider
    def provide_order_controller(
        self,
        checkout_use_case: CheckoutUseCase = Depends(),  # noqa: B008
        list_orders_use_case: ListOrdersUseCase = Depends(),  # noqa: B008
        update_order_status_use_case: UpdateOrderStatusUseCase = Depends(),  # noqa: B008
    ) -> OrderController:
        """Provides an OrderController instance."""
        return OrderController(
            checkout_use_case, list_orders_use_case, update_order_status_use_case
        )


def configure_injector(binder) -> None:  # noqa: ANN001
    """Configures the injector by installing the AppModule."""
    binder.install(AppModule())


# Create an instance of Injector with the configure_injector function.
injector = Injector([configure_injector])

__all__ = ["injector"]

from fastapi import Depends
from injector import Injector, Module, provider
from sqlalchemy.orm import Session

from src.api.controllers import (
    CustomerController,
    OrderController,
    PaymentConfirmationController,
    PaymentController,
)
from src.core.domain.repositories import (
    CustomerRepository,
    OrderRepository,
    PaymentRepository,
    ProductRepository,
)
from src.core.use_cases import (
    CheckoutUseCase,
    CreateCustomerUseCase,
    CustomerResult,
    GetCustomerByCpfUseCase,
    GetPaymentStatusUseCase,
    GetProductsByCategoryUseCase,
    ListOrdersByStatusUseCase,
    ListOrdersUseCase,
    OrderResult,
    PaymentConfirmationUseCase,
    PaymentProcessingUseCase,
    ProductCreationUseCase,
    ProductDeleteUseCase,
    ProductResult,
    ProductUpdateUseCase,
    UpdateOrderStatusUseCase,
)
from src.infra.database.config import get_db_session
from src.infra.database.repositories import (
    SQlAlchemyCustomerRepository,
    SQLAlchemyOrderRepository,
    SQLAlchemyPaymentRepository,
    SQLAlchemyProductRepository,
)

from ..payment import IPaymentGateway, MercadoPagoGateway
from .controllers import ProductController
from .presenters import (
    CustomerDetailsPresenter,
    OrderCreatedPresenter,
    OrderDetailsPresenter,
    Presenter,
    ProductDetailsPresenter,
)
from .schemas import CustomerDetailsOut, OrderCreationOut, OrderOut, ProductOut


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
        customer_details_presenter: CustomerDetailsPresenter = Depends(),  # noqa: B008
    ) -> CustomerController:
        """Provides a CustomerController instance.

        It depends on a CustomerUseCase, which is injected by FastAPI's "Depends" mechanism.
        """
        return CustomerController(
            create_customer_use_case, get_customer_by_cpf_use_case, customer_details_presenter
        )

    @provider
    def provide_customer_details_presenter(self) -> Presenter[CustomerDetailsOut, CustomerResult]:
        return CustomerDetailsPresenter()

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
    def provide_product_delete_use_case(
        self,
        product_repository: ProductRepository = Depends(),  # noqa: B008
    ) -> ProductDeleteUseCase:
        """Provides a ProductDeleteUseCase instance.

        It depends on a ProductRepository, which is injected by FastAPI's "Depends" mechanism.
        """
        return ProductDeleteUseCase(product_repository)

    @provider
    def provide_get_products_by_category_use_case(
        self,
        product_repository: ProductRepository = Depends(),  # noqa: B008
    ) -> GetProductsByCategoryUseCase:
        """Provides a GetProductsByCategoryUseCase instance.

        It depends on a ProductRepository, which is injected by FastAPI's "Depends" mechanism.
        """
        return GetProductsByCategoryUseCase(product_repository)

    @provider
    def provide_product_details_presenter(self) -> Presenter[ProductOut, ProductResult]:
        return ProductDetailsPresenter()

    @provider
    def provide_product_controller(
        self,
        get_products_by_category_use_case: GetProductsByCategoryUseCase = Depends(),  # noqa: B008
        product_creation_use_case: ProductCreationUseCase = Depends(),  # noqa: B008
        product_update_use_case: ProductUpdateUseCase = Depends(),  # noqa: B008
        product_delete_use_case: ProductDeleteUseCase = Depends(),  # noqa: B008
        product_details_presenter: Presenter[ProductOut, ProductResult] = Depends(),  # noqa: B008
    ) -> ProductController:
        """Provides a ProductController instance.

        It depends on a ProductUseCase, which is injected by FastAPI's "Depends" mechanism.
        """
        return ProductController(
            product_creation_use_case,
            product_update_use_case,
            product_delete_use_case,
            get_products_by_category_use_case,
            product_details_presenter,
        )

    @provider
    def provide_order_repository(
        self,
        session: Session = Depends(),  # noqa: B008
    ) -> OrderRepository:
        return SQLAlchemyOrderRepository(session)

    @provider
    def provide_payment_repository(
        self,
        session: Session = Depends(),  # noqa: B008
    ) -> PaymentRepository:
        return SQLAlchemyPaymentRepository(session)

    @provider
    def provide_payment_gateway(self) -> IPaymentGateway:
        return MercadoPagoGateway()

    @provider
    def provide_payment_use_case(
        self,
        payment_gateway: IPaymentGateway = Depends(),  # noqa: B008
        payment_repository: PaymentRepository = Depends(),  # noqa: B008
    ) -> PaymentProcessingUseCase:
        return PaymentProcessingUseCase(payment_gateway, payment_repository)

    @provider
    def provide_checkout_use_case(
        self,
        order_repository: OrderRepository = Depends(),  # noqa: B008
        customer_repository: CustomerRepository = Depends(),  # noqa: B008
        product_repository: ProductRepository = Depends(),  # noqa: B008
        payment_use_case: PaymentProcessingUseCase = Depends(),  # noqa: B008
    ) -> CheckoutUseCase:
        """Provides a CheckoutUseCase instance."""
        return CheckoutUseCase(
            order_repository,
            customer_repository,
            product_repository,
            payment_use_case,
        )

    @provider
    def provide_list_orders_use_case(
        self,
        order_repository: OrderRepository = Depends(),  # noqa: B008
    ) -> ListOrdersUseCase:
        """Provides a ListOrdersUseCase instance."""
        return ListOrdersUseCase(order_repository)

    @provider
    def provide_list_orders_sorted_by_status_use_case(
        self,
        order_repository: OrderRepository = Depends(),  # noqa: B008
    ) -> ListOrdersByStatusUseCase:
        """Provides a ListOrdersByStatusUseCase instance."""
        return ListOrdersByStatusUseCase(order_repository)

    @provider
    def provide_update_order_status_use_case(
        self,
        order_repository: OrderRepository = Depends(),  # noqa: B008
    ) -> UpdateOrderStatusUseCase:
        """Provides an UpdateOrderStatusUseCase instance."""
        return UpdateOrderStatusUseCase(order_repository)

    @provider
    def provide_order_created_presenter(self) -> Presenter[OrderCreationOut, OrderResult]:
        """Provides an OrderCreatedPresenter instance."""
        return OrderCreatedPresenter()

    @provider
    def provide_order_details_presenter(self) -> Presenter[OrderOut, OrderResult]:
        """Provides an OrderDetailsPresenter instance."""
        return OrderDetailsPresenter()

    @provider
    def provide_order_controller(
        self,
        checkout_use_case: CheckoutUseCase = Depends(),  # noqa: B008
        list_orders_use_case: ListOrdersUseCase = Depends(),  # noqa: B008
        update_order_status_use_case: UpdateOrderStatusUseCase = Depends(),  # noqa: B008
        order_created_presenter: Presenter[OrderCreationOut, OrderResult] = Depends(),  # noqa: B008
        order_details_presenter: Presenter[OrderOut, OrderResult] = Depends(),  # noqa: B008
        list_orders_sorted_by_status_use_case: ListOrdersByStatusUseCase = Depends(),  # noqa: B008
    ) -> OrderController:
        """Provides an OrderController instance."""
        return OrderController(
            checkout_use_case,
            list_orders_use_case,
            update_order_status_use_case,
            order_created_presenter,
            order_details_presenter,
            list_orders_sorted_by_status_use_case,
        )

    @provider
    def provide_payment_confirmation_use_case(
        self,
        payment_repository: PaymentRepository = Depends(),  # noqa: B008
        update_order_status_use_case: UpdateOrderStatusUseCase = Depends(),  # noqa: B008
    ) -> PaymentConfirmationUseCase:
        return PaymentConfirmationUseCase(payment_repository, update_order_status_use_case)

    @provider
    def provide_payment_confirmation_controller(
        self,
        payment_confirmation_use_case: PaymentConfirmationUseCase = Depends(),  # noqa: B008
    ) -> PaymentConfirmationController:
        return PaymentConfirmationController(payment_confirmation_use_case)

    @provider
    def provide_payment_controller(
        self,
        get_payment_status_use_case: GetPaymentStatusUseCase = Depends(),  # noqa: B008
    ) -> PaymentController:
        return PaymentController(get_payment_status_use_case)

    @provider
    def provide_get_payment_status_use_case(
        self,
        payment_repository: PaymentRepository = Depends(),  # noqa: B008
    ) -> GetPaymentStatusUseCase:
        return GetPaymentStatusUseCase(payment_repository)


def configure_injector(binder) -> None:  # noqa: ANN001
    """Configures the injector by installing the AppModule."""
    binder.install(AppModule())


# Create an instance of Injector with the configure_injector function.
injector = Injector([configure_injector])

__all__ = ["injector"]

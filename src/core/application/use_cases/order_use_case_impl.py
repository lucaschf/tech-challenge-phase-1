from src.core.application.dto import OrderInputDTO
from src.core.application.use_cases.order_use_case import OrderUseCase
from src.core.domain.entities import Product
from src.core.domain.entities.order import Order, OrderItem
from src.core.domain.exceptions import CustomerNotFoundError, ProductNotFoundError
from src.core.domain.repositories import CustomerRepository, OrderRepository, ProductRepository
from src.core.domain.value_objects import CPF


class OrderUseCaseImpl(OrderUseCase):
    """Implementation of the OrderUseCase interface."""

    def __init__(
        self,
        order_repository: OrderRepository,
        product_repository: ProductRepository,
        customer_repository: CustomerRepository,
    ) -> None:
        self._order_repository = order_repository
        self._product_repository = product_repository
        self._customer_repository = customer_repository

    def create_order(self, order_data: OrderInputDTO) -> Order:
        """Create a new order in the system.

        Args:
            order_data: The order data.

        Returns:
            Order: An Order object representing the newly created order.
        """
        cpf = CPF(order_data.customer_cpf)
        customer = self._customer_repository.get_by_cpf(cpf)

        if not customer:
            raise CustomerNotFoundError(cpf=order_data.customer_cpf.number)

        order_items = []

        for item in order_data.items:
            product: Product = self._product_repository.get_by_uuid(item.product_uuid)
            if not product:
                raise ProductNotFoundError(uuid=item.product_uuid)
            order_items.append(
                OrderItem(product=product, quantity=item.quantity, price=product.price)
            )

        order = Order(
            customer=customer, items=order_items, payment_method=order_data.payment_method
        )

        return self._order_repository.add(order)

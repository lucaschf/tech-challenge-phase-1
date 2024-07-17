from typing import Iterable
from uuid import UUID

from src.core.domain.entities import Customer, Order, OrderItem, Product
from src.core.domain.exceptions import (
    CustomerNotFoundError,
    EmptyOrderError,
    OrderCreationFailedDueToMissingProductsError,
)
from src.core.domain.repositories import CustomerRepository, OrderRepository, ProductRepository

from .checkout_dto import (
    CheckoutItem,
    CheckoutOrder,
    CheckoutResult,
)


class CheckoutUseCase:
    """CheckoutUseCase encapsulates the business logic for creating orders."""

    def __init__(
        self,
        order_repository: OrderRepository,
        customer_repository: CustomerRepository,
        product_repository: ProductRepository,
    ) -> None:
        """Initializes a new instance of the CheckoutUseCase class.

        Args:
            order_repository: The repository instance for order persistence operations.
            customer_repository: The repository instance for customer persistence operations.
            product_repository: The repository instance for product persistence operations.
        """
        self._order_repository = order_repository
        self._customer_repository = customer_repository
        self._product_repository = product_repository

    def checkout(self, request: CheckoutOrder) -> CheckoutResult:
        """Creates a new order in the system.

        Args:
            request: The checkout request data.

        Returns:
            CheckoutResponse: The response containing the order number.

        Raises:
            EmptyOrderError: If the order has no items.
            OrderCreationFailedDueToMissingProductsError: If any product is not found.
            CustomerNotFoundError: If the customer is not found.
        """
        self._validate_items(request.items)
        customer = self._get_customer(request.customer_id)
        product_map = self._get_products(request.items)

        order_items = self._create_order_items(request.items, product_map)
        order = Order(_customer=customer, _items=list(order_items))
        created_order = self._order_repository.create(order)

        return CheckoutResult(number=created_order.uuid)

    @staticmethod
    def _validate_items(items: Iterable[CheckoutItem]) -> None:
        if not items:
            raise EmptyOrderError()

    def _get_products(self, items: Iterable[CheckoutItem]) -> dict[UUID, Product]:
        """Gets the products for the order items.

        Args:
            items: The order items containing the product identifiers.

        Returns:
            A dictionary containing the product UUIDs as keys and the products as values.

        Raises:
            OrderCreationFailedDueToMissingProductsError: If any product is not found.
        """
        product_uuids = {item.product_id for item in items}
        products = self._product_repository.get_by_uuids(product_uuids)
        product_map = {product.uuid: product for product in products}
        missing_products = product_uuids - product_map.keys()

        if missing_products:
            raise OrderCreationFailedDueToMissingProductsError(missing_products)

        return product_map

    def _get_customer(self, customer_id: UUID) -> Customer:
        """Gets a customer by CPF.

        Args:
            customer_id: The customer's external identifier.

        Returns:
            Customer: The customer entity if found.

        Raises:
            CustomerNotFoundError: If the customer is not found.
        """
        customer = self._customer_repository.get_by_uuid(customer_id)
        if not customer:
            raise CustomerNotFoundError(search_params={"uuid": customer_id})

        return customer

    @staticmethod
    def _create_order_items(
        items: Iterable[CheckoutItem], product_map: dict[UUID, Product]
    ) -> Iterable[OrderItem]:
        return [
            OrderItem(
                product=product_map[item.product_id],
                unit_price=product_map[item.product_id].price,
                quantity=item.quantity,
            )
            for item in items
        ]


__all__ = ["CheckoutUseCase"]

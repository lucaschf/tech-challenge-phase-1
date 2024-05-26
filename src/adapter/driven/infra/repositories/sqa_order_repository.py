from sqlalchemy.orm import Session

from src.adapter.driven.infra.sqa_models import OrderItemPersistentModel, OrderPersistentModel
from src.core.domain.entities.order import Order, OrderItem
from src.core.domain.repositories import OrderRepository


class SQAOrderRepository(OrderRepository):
    """Repository for handling orders persistence."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def add(self, order: Order) -> Order:
        """Add a new order to the database.

        Args:
            order: The order data.

        Returns:
            Order: The added order data.
        """
        db_order = OrderPersistentModel(
            customer_id=order.customer.id,
            payment_method=order.payment_method.value,
            status=order.status.value,
            total_price=order.total_price,
            items=[
                OrderItemPersistentModel(
                    product_id=item.product.id, quantity=item.quantity, price=item.price
                )
                for item in order.items
            ],
        )

        self._session.add(db_order)
        self._session.commit()

        return db_order

    def get_all(self) -> list[Order]:
        """Get all orders in the database.

        Returns:
            list[Order]: A list of Order objects.
        """
        return [
            Order(
                _id=db_order.id,
                uuid=db_order.uuid,
                customer=db_order.customer,
                items=[
                    OrderItem(
                        product=item.product,
                        quantity=item.quantity,
                        price=item.price,
                    )
                    for item in db_order.items
                ],
                payment_method=db_order.payment_method,
                status=db_order.status,
            )
            for db_order in self._session.query(OrderPersistentModel).all()
        ]


__all__ = ["OrderRepository"]

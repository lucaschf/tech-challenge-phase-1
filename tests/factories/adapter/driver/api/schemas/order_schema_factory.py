from uuid import uuid4

import factory

from src.adapter.driver.api.schemas.order_schema import OrderIn, OrderItemIn


class OrderItemInFactory(factory.Factory):  # noqa: D101
    product_id = factory.LazyFunction(uuid4)
    quantity = factory.Faker("random_int", min=1, max=5)

    class Meta:  # noqa: D106
        model = OrderItemIn


class OrderInFactory(factory.Factory):  # noqa: D101
    user_uuid = factory.LazyFunction(uuid4)
    products = factory.List([factory.SubFactory(OrderItemInFactory) for _ in range(2)])

    class Meta:  # noqa: D106
        model = OrderIn


__all__ = ["OrderInFactory", "OrderItemInFactory"]

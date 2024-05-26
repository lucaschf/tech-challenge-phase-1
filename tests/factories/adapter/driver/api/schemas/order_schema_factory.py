from uuid import uuid4

import factory

from src.adapter.driver.api.schemas.order_schema import OrderIn, OrderProductIn


class OrderProductInFactory(factory.Factory):  # noqa: D101
    product_id = factory.LazyFunction(uuid4)
    quantity = factory.Faker("random_int", min=1, max=5)

    class Meta:  # noqa: D106
        model = OrderProductIn


class OrderInFactory(factory.Factory):  # noqa: D101
    class Meta:  # noqa: D106
        model = OrderIn

    user_id = factory.LazyFunction(uuid4)
    products = OrderProductInFactory.create_batch(2)

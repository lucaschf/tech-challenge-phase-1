from uuid import uuid4

import factory

from src.adapter.driver.api.schemas.order_schema import OrderIn


class OrderInFactory(factory.Factory):  # noqa: D101
    class Meta:  # noqa: D106
        model = OrderIn

    user_id = factory.LazyFunction(uuid4)
    products = factory.List(["product1", "product2"])

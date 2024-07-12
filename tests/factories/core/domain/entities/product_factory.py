import factory

from src.core.domain.entities import Product
from src.core.domain.value_objects import Category


class ProductFactory(factory.Factory):
    """Product Factory."""

    name = factory.Faker("name")
    price = factory.Faker("pydecimal", left_digits=5, right_digits=2, positive=True)
    description = factory.Faker("sentence")
    images = factory.List([factory.Faker("url") for _ in range(5)])

    category = factory.Faker("random_element", elements=Category.values())

    class Meta:  # noqa: D106
        model = Product


__all__ = ["ProductFactory"]

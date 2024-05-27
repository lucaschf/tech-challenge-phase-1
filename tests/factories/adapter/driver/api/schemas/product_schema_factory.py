import factory

from src.adapter.driver.api.schemas.product_schema import ProductCreationIn
from src.core.domain.value_objects.category import Category


class ProductCreationInFactory(factory.Factory):  # noqa: D101
    name = factory.Faker("name")
    price = factory.Faker("pydecimal", left_digits=5, right_digits=2, positive=True)
    description = factory.Faker("sentence")
    images = factory.List([factory.Faker("url") for _ in range(5)])
    category = factory.Faker("random_element", elements=Category.ALLOWED_CATEGORIES)

    class Meta:  # noqa: D106
        model = ProductCreationIn


__all__ = ["ProductCreationInFactory"]

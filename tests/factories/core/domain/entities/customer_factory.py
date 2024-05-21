import factory

from src.core.domain.entities import Customer


class CustomerFactory(factory.Factory):
    """Customer Factory."""

    name = factory.Faker("name")
    email = factory.Faker("email")
    cpf = factory.Faker("cpf_number")

    class Meta:  # noqa: D106
        model = Customer


__all__ = ["CustomerFactory"]

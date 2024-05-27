import factory

from src.adapter.driver.api.schemas import CustomerCreationIn


class CustomerCreationInFactory(factory.Factory):  # noqa: D101
    name = factory.Faker("name")
    email = factory.Faker("email")
    cpf = factory.Faker("cpf_number")

    class Meta:  # noqa: D106
        model = CustomerCreationIn


__all__ = ["CustomerCreationInFactory"]

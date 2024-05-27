import random

import factory
from faker import Faker

from src.core.domain.entities import Customer
from src.core.domain.value_objects import CPF, Email

fake = Faker()


def generate_cpf() -> CPF:
    # Função para gerar um CPF válido
    cpf = [random.randint(0, 9) for _ in range(9)]  # noqa: S311
    for _ in range(2):
        val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11  # noqa: C419
        cpf.append(11 - val if val > 1 else 0)
    return CPF("".join(map(str, cpf)))


class CustomerFactory(factory.Factory):
    """Customer Factory."""

    name = factory.LazyFunction(fake.name)
    email = factory.LazyFunction(lambda: Email(fake.email()))
    cpf = factory.LazyFunction(generate_cpf)

    class Meta:  # noqa: D106
        model = Customer


__all__ = ["CustomerFactory"]

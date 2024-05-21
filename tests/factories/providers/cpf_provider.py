import random

from faker.providers import BaseProvider


class CPFProvider(BaseProvider):
    """A Brazilian CRM numbers provider."""

    # noinspection PyMethodMayBeStatic
    def cpf_number(self) -> str:
        """Return a random cro number."""
        return self.generate_cpf_number()

    @staticmethod
    def generate_cpf_number() -> str:
        """Generate a valid CPF number."""
        cpf = [random.randint(0, 9) for _ in range(9)]  # noqa: S311

        soma = sum(cpf[i] * (10 - i) for i in range(9))
        resto = soma % 11
        digito1 = 0 if resto < 2 else 11 - resto
        cpf.append(digito1)

        soma = sum(cpf[i] * (11 - i) for i in range(10))
        resto = soma % 11
        digito2 = 0 if resto < 2 else 11 - resto
        cpf.append(digito2)

        return "".join(str(d) for d in cpf)


__all__ = ["CPFProvider"]

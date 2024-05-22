import re

from src.core.domain.base import ValueObject
from src.core.domain.exceptions import InvalidCpfError


class CPF(ValueObject):
    """A Value Object that represents a Brazilian CPF (Cadastro de Pessoas Físicas).

    CPF is a unique number that identifies a taxpaying resident in Brazil. This class
    validates the CPF number using the official Brazilian algorithm.

    Attributes:
        _number: The CPF number.
    """

    def __init__(self, cpf: str) -> None:
        """Initializes a CPF object after validating the input CPF number.

        Args:
            cpf (str): The CPF number to be validated and stored.

        Raises:
            InvalidCpfError: If the input CPF number is invalid.
        """
        if not self._is_valid(cpf):
            raise InvalidCpfError(cpf=cpf)

        self._number = self._clean_cpf(cpf)

    def _get_equality_components(self) -> tuple[str]:
        """Provides the components that define the value of this CPF object.

        Returns:
            Tuple[str]: A tuple containing the CPF number.
        """
        return (self.number,)

    @property
    def number(self) -> str:
        """Gets the CPF number.

        Returns:
            str: The CPF number.
        """
        return self._number

    @classmethod
    def _is_valid(cls, cpf: str) -> bool:
        """Validates the input CPF number using the official Brazilian algorithm.

        Args:
            cpf (str): The CPF number to be validated.

        Returns:
            bool: True if the CPF number is valid, False otherwise.
        """
        if not re.match(r"(\d{3}\.\d{3}\.\d{3}-\d{2}|\d{11})", cpf):
            return False

        cpf = cls._clean_cpf(cpf)

        # Checks if all digits are the same
        if cpf == cpf[0] * 11:
            return False

        checksum = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digit1 = 11 - (checksum % 11)
        digit1 = 0 if digit1 > 9 else digit1

        # Calculates the second check digit
        checksum = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digit2 = 11 - (checksum % 11)
        digit2 = 0 if digit2 > 9 else digit2

        return cpf.endswith(f"{digit1}{digit2}")

    @staticmethod
    def _clean_cpf(cpf: str) -> str:
        """Removes non-digit characters from the CPF number.

        Args:
            cpf (str): The CPF number to be cleaned.

        Returns:
            str: The cleaned CPF number.
        """
        return re.sub(r"\D", "", cpf)

    def __str__(self) -> str:
        """Returns the clean CPF number."""
        return self.number


__all__ = ["CPF"]

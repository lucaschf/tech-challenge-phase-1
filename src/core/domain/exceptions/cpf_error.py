from typing import Optional

from src.core.domain.base import DomainError


class InvalidCpfError(DomainError):
    """Exception raised when a CPF is invalid."""

    def __init__(self, cpf: Optional[object]) -> None:
        """Initializes the exception with a default message."""
        self._cpf = cpf
        super().__init__(message="Invalid CPF.")

    @property
    def cpf(self) -> Optional[object]:
        """Gets the invalid CPF."""
        return self._cpf


__all__ = ["InvalidCpfError"]

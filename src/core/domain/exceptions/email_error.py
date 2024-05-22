from typing import Optional

from src.core.domain.base import DomainError


class InvalidEmailError(DomainError):
    """Exception raised when an email is invalid."""

    def __init__(self, email_address: Optional[object]) -> None:
        """Initializes the exception with a default message."""
        self._email_address = email_address
        super().__init__(message="Invalid email.")

    @property
    def email_address(self) -> Optional[object]:
        """Gets the invalid email address."""
        return self._email_address


__all__ = ["InvalidEmailError"]

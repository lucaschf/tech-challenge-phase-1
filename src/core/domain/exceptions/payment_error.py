from types import MappingProxyType
from typing import Any

from src.core.domain.exceptions import NotFoundError


class PaymentNotFoundError(NotFoundError):
    """Raised when a payment is not found."""

    def __init__(
        self,
        search_params: dict[str, Any],
        message: str | None = None,
        inner_error: Exception | None = None,
    ) -> None:
        """Constructs a new exception.

        Args:
            search_params: The search parameters that were used to search.
            message: A custom message to include in the exception.
            inner_error: An underlying exception that caused this exception.
        """
        default_message = "Payment not found."
        super().__init__(message or default_message, inner_error)
        self._search_params = MappingProxyType(search_params)

    @property
    def search_params(self) -> dict[str, Any]:
        """The search parameters that were used to search."""
        return dict(self._search_params)


__all__ = ["PaymentNotFoundError"]

from types import MappingProxyType
from typing import Any

from .not_found_error import NotFoundError


class CustomerNotFoundError(NotFoundError):
    """Raised when a customer with the given CPF is not found."""

    def __init__(
        self,
        search_params: dict[str, Any],
        message: str | None = None,
        inner_error: Exception | None = None,
    ) -> None:
        """Constructs a new CustomerNotFound exception.

        Args:
            search_params:
             The search parameters that were used to search for the customer.
            message: A custom message to include in the exception.
            inner_error: An underlying exception that caused this exception.
        """
        default_message = "Customer not found."
        super().__init__(message or default_message, inner_error)
        self._search_params = MappingProxyType(search_params)

    @property
    def search_params(self) -> dict[str, Any]:
        """The search parameters that were used to search for the customer."""
        return dict(self._search_params)


__all__ = ["CustomerNotFoundError"]

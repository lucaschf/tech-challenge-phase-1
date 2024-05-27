from uuid import UUID

from .not_found_error import NotFoundError


class OrderNotFoundError(NotFoundError):
    """Raised when a order with the given uuid is not found."""

    def __init__(
        self, uuid: str | UUID, message: str | None = None, inner_error: Exception | None = None
    ) -> None:
        """Constructs a new OrderNotFoundError exception.

        Args:
            uuid: The uuid of the order that was not found.
            message: A custom message to include in the exception.
            inner_error: An underlying exception that caused this exception.
        """
        default_message = f"Order with uuid '{uuid}' not found."
        super().__init__(message or default_message, inner_error)
        self.uuid = uuid


__all__ = ["OrderNotFoundError"]

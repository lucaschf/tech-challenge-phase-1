from typing import ClassVar

from src.core.domain.base import ValueObject
from src.core.domain.exceptions.order_status_error import InvalidOrderStatusError


class OrderStatus(ValueObject):
    """A Value Object that represents an Order Status.

    The status must be one of the predefined statuses: pending, completed, cancelled.

    Attributes:
        _status: The current status of the order.
    """

    ALLOWED_STATUSES: ClassVar[set[str]] = {"pending", "completed", "cancelled"}

    def __init__(self, status: str) -> None:
        """Initializes an OrderStatus object after validating the input status.

        Args:
            status (str): The status to be validated and stored.

        Raises:
            InvalidOrderStatusError: If the input status is invalid.
        """
        if not self._is_valid(status):
            raise InvalidOrderStatusError(status=status)

        self._status = status

    def _get_equality_components(self) -> tuple[str]:
        """Provides the components that define the value of this OrderStatus object.

        Returns:
            Tuple[str]: A tuple containing the status.
        """
        return (self.status,)

    @property
    def status(self) -> str:
        """Gets the status.

        Returns:
            str: The status.
        """
        return self._status

    @classmethod
    def _is_valid(cls, status: str) -> bool:
        """Validates if the input status is one of the allowed statuses.

        Args:
            status (str): The status to be validated.

        Returns:
            bool: True if the status is valid, False otherwise.
        """
        return status in cls.ALLOWED_STATUSES

    def __str__(self) -> str:
        """Returns the status as a string."""
        return self.status


__all__ = ["OrderStatus"]

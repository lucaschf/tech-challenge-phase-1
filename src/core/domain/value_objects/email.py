import re

from src.core.domain.base import ValueObject
from src.core.domain.exceptions import InvalidEmailError


class Email(ValueObject):
    """A Value Object that represents an Email.

    This class validates the email using a simple regular expression.

    Attributes:
        _address: The email address.
    """

    def __init__(self, email_address: str) -> None:
        """Initializes an Email object after validating the input email.

        Args:
            email_address (str): The email to be validated and stored.

        Raises:
            InvalidEmailError: If the input email is invalid.
        """
        if not self._is_valid(email_address):
            raise InvalidEmailError(email_address)

        self._address = email_address

    def _get_equality_components(self) -> tuple[str]:
        """Provides the components that define the value of this Email object.

        Returns:
            Tuple[str]: A tuple containing the email address.
        """
        return (self.address,)

    @property
    def address(self) -> str:
        """Gets the email address.

        Returns:
            str: The email address.
        """
        return self._address

    @staticmethod
    def _is_valid(email: str) -> bool:
        """Validates the input email using a simple regular expression.

        Args:
            email (str): The email to be validated.

        Returns:
            bool: True if the email is valid, False otherwise.
        """
        return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

    def __str__(self) -> str:
        """Returns the email address as a string."""
        return self.address


__all__ = ["Email"]

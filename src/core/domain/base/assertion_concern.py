from typing import Any, Union

from .domain_error import DomainError


class AssertionConcern:
    """A class for domain-specific validation assertions."""

    @staticmethod
    def _assert(condition: bool, message: str) -> None:
        """A generic assert method that raises a DomainError if the condition is False.

        Args:
            condition: The condition to be validated.
            message: The error message to raise if the validation fails.

        Raises:
            DomainError: If the condition is False.
        """
        if not condition:
            raise DomainError(message)

    @classmethod
    def assert_argument_in_set(
        cls: "AssertionConcern", string_value: str, valid_set: set, message: str
    ) -> None:
        """Asserts that a string value is within a specified set.

        Args:
            string_value: The string value to be validated.
            valid_set: The set of valid values.
            message: The error message to raise if the validation fails.

        Raises:
            DomainError: If the string value is not in the valid set.
        """
        if string_value not in valid_set:
            cls._assert(False, message)

    @classmethod
    def assert_argument_length(
        cls: "AssertionConcern",
        string_value: str,
        maximum: int,
        message: str,
    ) -> None:
        """Asserts that the trimmed length of a string does not exceed the maximum.

        Args:
            string_value: The string to be validated.
            maximum: The maximum allowed length.
            message: The error message to raise if the validation fails.

        Raises:
            DomainError: If the string's trimmed length exceeds the maximum.
        """
        length = len(string_value.strip())
        cls._assert(length <= maximum, message)

    @classmethod
    def assert_argument_length_range(
        cls: "AssertionConcern",
        string_value: str,
        minimum: int,
        maximum: int,
        message: str,
    ) -> None:
        """Asserts that the trimmed length of a string is within a specified range.

        Args:
            string_value: The string to be validated.
            minimum: The minimum allowed length.
            maximum: The maximum allowed length.
            message: The error message to raise if the validation fails.

        Raises:
            DomainError: If the string's trimmed length is not within the range.
        """
        length = len(string_value.strip())
        cls._assert(minimum <= length <= maximum, message)

    @classmethod
    def assert_argument_not_empty(
        cls: "AssertionConcern",
        value: Union[str, list, tuple],
        message: str,
    ) -> None:
        """Asserts that a string or a list/tuple is not null or empty after trimming if it's a string.

        Args:
            value: The value to be validated.
            message: The error message to raise if the validation fails.

        Raises:
            DomainError: If the value is null or empty.
        """
        if isinstance(value, str):
            cls._assert(bool(value and value.strip()), message)
        elif isinstance(value, (list, tuple)):
            cls._assert(bool(value), message)
        else:
            cls._assert(False, "assert_argument_not_empty only supports str, list, and tuple")

    @classmethod
    def assert_argument_not_null(
        cls: "AssertionConcern",
        obj: Any,  # noqa: ANN401
        message: str,
    ) -> None:
        """Asserts that an object is not None.

        Args:
            obj: Any: The object to be validated.
            message: The error message to raise if the validation fails.

        Raises:
            DomainError: If the object is None.
        """
        cls._assert(obj is not None, message)

    @classmethod
    def assert_argument_greater_than_zero(
        cls: "AssertionConcern",
        value: Union[int, float],
        message: str,
    ) -> None:
        """Asserts that a numeric value is strictly greater than zero.

        Args:
            value: The numeric value to be validated.
            message: The error message to raise if the validation fails.

        Raises:
            DomainError: If the value is less than or equal to zero.
            TypeError: If the value is not numeric (int or float).
        """
        cls.assert_argument_not_null(value, message)
        cls._assert(value > 0, message)


__all__ = ["AssertionConcern"]

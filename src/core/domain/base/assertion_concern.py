from typing import Iterable

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
        iterable_value: Iterable,
        message: str,
    ) -> None:
        """Asserts iterable is not None, empty, or has only False-like values or whitespace strings.

        Args:
            iterable_value: The iterable to be validated.
            message: The error message to raise if the validation fails.

        Raises:
            DomainError: If the iterable is None, empty, contains only False-like values,
             or is a whitespace string.
        """
        try:
            is_valid = any(iterable_value) and (
                not isinstance(iterable_value, str) or iterable_value.strip()
            )
        except TypeError:  # Handle case where iterable_value is not iterable
            is_valid = False

        cls._assert(is_valid, message)

    @classmethod
    def assert_argument_not_null(
        cls: "AssertionConcern",
        obj: object | None,
        message: str,
    ) -> None:
        """Asserts that an object is not None.

        Args:
            obj: The object to be validated.
            message: The error message to raise if the validation fails.

        Raises:
            DomainError: If the object is None.
        """
        cls._assert(obj is not None, message)


__all__ = ["AssertionConcern"]

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
        string_value: str,
        message: str,
    ) -> None:
        """Asserts that a string is not null or empty after trimming.

        Args:
            string_value: The string to be validated.
            message: The error message to raise if the validation fails.

        Raises:
            DomainError: If the string is null or empty after trimming.
        """
        cls._assert(bool(string_value and string_value.strip()), message)

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

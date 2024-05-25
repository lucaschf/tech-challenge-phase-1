from .not_found_error import NotFoundError


class CustomerNotFoundError(NotFoundError):
    """Raised when a customer with the given CPF is not found."""

    def __init__(
        self, cpf: str, message: str | None = None, inner_error: Exception | None = None
    ) -> None:
        """Constructs a new CustomerNotFound exception.

        Args:
            cpf: The CPF of the customer that was not found.
            message: A custom message to include in the exception.
            inner_error: An underlying exception that caused this exception.
        """
        default_message = f"Customer with CPF '{cpf}' not found."
        super().__init__(message or default_message, inner_error)
        self.cpf = cpf


__all__ = ["CustomerNotFoundError"]

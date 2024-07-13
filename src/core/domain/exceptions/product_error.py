from .not_found_error import NotFoundError


class ProductNotFoundError(NotFoundError):
    """Raised when a product is not found."""

    def __init__(
        self, search_param: str, message: str | None = None, inner_error: Exception | None = None
    ) -> None:
        """Constructs a new CustomerNotFound exception.

        Args:
            search_param: The search parameter that was used to search for the product.
            message: A custom message to include in the exception.
            inner_error: An underlying exception that caused this exception.
        """
        default_message = "Product not found."
        super().__init__(message or default_message, inner_error)
        self.search_param = search_param


__all__ = ["ProductNotFoundError"]

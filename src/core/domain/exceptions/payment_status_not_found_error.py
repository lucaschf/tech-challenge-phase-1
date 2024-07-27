from src.core.domain.base import DomainError


class PaymentStatusNotFoundError(DomainError):
    """Exception raised for invalid payment status.

    Attributes:
        search_params -- input params which caused the error
    message -- explanation of the error
    """

    def __init__(self, search_params: dict, message: str = "Payment status not found") -> None:
        super().__init__(message)
        self.search_params = search_params


__all__ = ["PaymentStatusNotFoundError"]

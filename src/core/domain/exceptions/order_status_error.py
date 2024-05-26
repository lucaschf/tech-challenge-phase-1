from src.core.domain.base import DomainError


class InvalidOrderStatusError(DomainError):
    """Exception raised for invalid order status.

    Attributes:
        status -- input status which caused the error
        message -- explanation of the error
    """

    def __init__(self, status: str, message: str = "Invalid order status") -> None:
        super().__init__(message)
        self.status = status

    def __str__(self) -> str:
        return f"{self.status} -> {self.message}"


__all__ = ["InvalidOrderStatusError"]

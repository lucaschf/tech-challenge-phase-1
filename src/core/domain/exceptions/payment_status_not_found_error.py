from src.core.domain.base import DomainError

class PaymentStatusNotFoundError(DomainError):
    """uashdfuahsdufhsfuhdf"""
    def __init__(self, status: str, message: str = "Payment status not found") -> None:
        super().__init__(message)
        self.status = status

    def __str__(self) -> str:
        return f"{self.status} -> {self.message}"


__all__ = ["PaymentStatusNotFoundError"]

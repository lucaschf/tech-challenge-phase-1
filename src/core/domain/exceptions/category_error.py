from src.core.domain.base import DomainError


class InvalidCategoryError(DomainError):
    """Exception raised for invalid product category.

    Attributes:
        category -- input category which caused the error
        message -- explanation of the error
    """

    def __init__(self, category: str, message: str = "Invalid category") -> None:
        super().__init__(message)
        self.category = category

    def __str__(self) -> str:
        return f"{self.category} -> {self.message}"


__all__ = ["InvalidCategoryError"]

class InvalidCategoryError(Exception):
    """Exception raised for invalid product category.

    Attributes:
        category -- input category which caused the error
        message -- explanation of the error
    """

    def __init__(self, category: str, message: str = "Invalid category") -> None:
        self.category = category
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"{self.category} -> {self.message}"


__all__ = ["InvalidCategoryError"]

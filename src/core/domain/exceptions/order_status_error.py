class InvalidOrderStatusError(Exception):
    """Exception raised for invalid order status.

    Attributes:
        status -- input status which caused the error
        message -- explanation of the error
    """

    def __init__(self, status: str, message: str = "Invalid order status") -> None:
        self.status = status
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"{self.status} -> {self.message}"


__all__ = ["InvalidOrderStatusError"]

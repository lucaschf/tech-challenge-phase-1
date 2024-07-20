from src.core.domain.base import DomainError


class InvalidStatusTransitionError(DomainError):
    """Raised when an invalid transition is attempted on a status."""

    def __init__(self, status: str, new_status: str) -> None:
        super().__init__(f"Invalid status transition from {status} to {new_status}")
        self.status = status
        self.new_status = new_status


__all__ = ["InvalidStatusTransitionError"]

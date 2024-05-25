from ..base import DomainError


class NotFoundError(DomainError):
    """Base class for errors where an entity is not found."""


__all__ = ["NotFoundError"]

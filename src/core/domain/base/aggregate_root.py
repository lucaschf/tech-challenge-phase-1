from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID


@dataclass(kw_only=True)
class AggregateRoot(ABC):
    """Base class for aggregate roots."""

    _id: int | None = field(default=None)
    uuid: UUID | None = field(default=None)
    created_at: datetime | None = field(default=None)
    updated_at: datetime | None = field(default=None)

    @abstractmethod
    def validate(self) -> None:
        """Validate the aggregate root.

        Raises:
           DomainError: If the validation fails.
        """
        pass

    def __post_init__(self) -> None:
        self.validate()

    @property
    def id(self) -> int | None:
        """The aggregate root's ID."""
        return self._id


__all__ = ["AggregateRoot"]

from abc import ABC, abstractmethod
from datetime import datetime
from uuid import UUID


class AggregateRoot(ABC):  # noqa: B024
    """Base class for aggregate roots."""

    def __init__(
        self,
        _id: int | None = None,
        uuid: UUID | None = None,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
    ) -> None:
        self.id = _id
        """The aggregate root ID."""

        self.uuid = uuid
        """The aggregate root UUID used in external systems."""

        self.created_at = created_at
        """The aggregate root creation date and time."""

        self.updated_at = updated_at
        """The aggregate root last update date and time."""

        self.validate()

    @abstractmethod
    def validate(self) -> None:
        """Validate the aggregate root.

        Raises:
           DomainError: If the validation fails.
        """
        pass


__all__ = ["AggregateRoot"]

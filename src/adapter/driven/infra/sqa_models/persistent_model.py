import uuid
from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, DateTime, Integer, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped


class PersistentModel(DeclarativeBase):
    """A base model class for all persistent models in the application.

    This class provides common fields and configurations for all persistent models.
    It inherits from the `Base` class, which is assumed to be a SQLAlchemy declarative base.

    Attributes:
    - id: An auto-incrementing integer primary key.
    - external_id: A UUID field with a default value generated using `uuid4`.
    - created_at: A DateTime field with the current timestamp when an instance is created.
    - updated_at: A DateTime field with the current timestamp when an instance is updated.
    """

    __abstract__ = True

    id: Mapped[int] = Column(Integer, primary_key=True)
    """An auto-incrementing integer primary key."""

    external_id: Mapped[uuid.UUID] = Column(
        UUID(as_uuid=True), default=uuid4, unique=True, index=True
    )
    """A UUID field with a default value generated using `uuid4`."""

    created_at: Mapped[datetime] = Column(DateTime(timezone=True), server_default=func.now())
    """A DateTime field with the current timestamp when an instance is created."""

    updated_at: Mapped[datetime] = Column(DateTime(timezone=True), onupdate=func.now())
    """A DateTime field with the current timestamp when an instance is updated."""


__all__ = ["PersistentModel"]

from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import Column, DateTime, Integer, func
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import DeclarativeBase, Mapped


class PersistentModel(DeclarativeBase):
    """A base model class for all persistent models in the application.

    This class provides common fields and configurations for all persistent models.
    It inherits from the `Base` class, which is assumed to be a SQLAlchemy declarative base.

    Attributes:
    - id: An auto-incrementing integer primary key.
    - uuid: A UUID field with a default value generated using `uuid4`.
    - created_at: A DateTime field with the current timestamp when an instance is created.
    - updated_at: A DateTime field with the current timestamp when an instance is updated.
    """

    __abstract__ = True

    id: Mapped[int] = Column(Integer, primary_key=True)
    """An auto-incrementing integer primary key."""

    uuid: Mapped[UUID] = Column(
        PG_UUID(as_uuid=True), default=uuid4, unique=True, index=True, nullable=False
    )
    """A UUID field with a default value generated using `uuid4`."""

    created_at: Mapped[datetime] = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    """A DateTime field with the current timestamp when an instance is created."""

    updated_at: Mapped[datetime] = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )
    """A DateTime field with the current timestamp when an instance is updated."""


__all__ = ["PersistentModel"]

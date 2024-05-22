"""This package contains SQLAlchemy models for the System.

These models are used to interact with the database using SQLAlchemy,
an SQL toolkit and Object-Relational Mapping (ORM) system for Python.

They provide a high-level API for SQL operations, abstracting the underlying database system.
"""

from .persistent_model import PersistentModel

__all__ = ["PersistentModel"]

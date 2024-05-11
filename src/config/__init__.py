"""Responsible for handling the configuration and environment settings for the project.

This includes reading from .env files or system environment variables, and exposing these
values for use in the application.
"""

from .env_settings import settings

__all__ = ["settings"]

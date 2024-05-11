"""This module contains adapter classes that are driven by the application.

These adapters handle incoming interactions, such as HTTP requests or Command Line Interface
(CLI) commands.

They serve as the entry point for these interactions, translating them into a
format that can be processed by the application's use cases and entities.
"""

from .api import app

__all__ = ["app"]

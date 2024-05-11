"""Contains Adapter classes bridge domain entities/use cases and external services.

These adapters are responsible for transforming data from a format that is convenient for the
domain entities and use cases into a format that is suitable for external services or
infrastructure.
This includes, but is not limited to, databases and message brokers.

The goal of these adapters is to ensure a clean separation of concerns, where the domain logic is
not coupled with specific details of external services or infrastructure.
This allows for greater flexibility and maintainability of the codebase.
"""

"""The 'adapter' package contains both driver and driven adapters.

Driver adapters handle incoming interactions such as HTTP requests, RPCs, and received messages.
Driven adapters, on the other hand,
manage interactions with external services like databases and message brokers.

The primary responsibility of this layer is to convert data between the formats preferred by the
domain entities and use cases, and those preferred by external services and interfaces.
This ensures a clean separation of concerns and enhances the maintainability of the codebase.
"""

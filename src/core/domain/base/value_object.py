from abc import ABC, abstractmethod
from collections.abc import Iterable


class ValueObject(ABC):
    """An abstract base class for Value Objects.

    Value Objects are immutable objects that are defined by their values,
    not their identity.

    They are typically used to represent domain concepts.
    """

    @abstractmethod
    def _get_equality_components(self) -> Iterable:
        """Returns an iterable of components that define the value of this object.

        These components will be used for equality comparisons and hashing.
        """

    def __eq__(self, other: object) -> bool:
        if other is None or not isinstance(other, type(self)):
            return False

        return self._get_equality_components() == other._get_equality_components()

    def __hash__(self) -> int:
        return hash(tuple(x for x in self._get_equality_components() if x is not None))


__all__ = ["ValueObject"]

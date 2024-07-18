from abc import ABC, abstractmethod
from typing import Iterable


class Presenter[OutputModel, InputData](ABC):
    """An abstract base class that defines a template for presenting data.

    This class is designed to be subclassed with specific implementations of the `present` method
    to convert input data into a desired output model format.
    It also provides a utility method `present_many`
    for handling iterable collections of input data.

    Type Variables:
        OutputModel: The type of the output model that the presenter will produce.
        InputData: The type of the input data that the presenter will consume.
    """

    @abstractmethod
    def present(self, data: InputData) -> OutputModel:
        """Abstract method to present a single item of input data as output model.

        This method must be implemented by subclasses to define the specific presentation logic.

        Args:
            data (InputData): The input data to be presented.

        Returns:
            The presented output model.
        """
        pass

    def present_many(self, data: Iterable[InputData]) -> Iterable[OutputModel]:
        """Presents multiple items of input data as output models.

        This method uses the `present` method to individually convert each item in the given
        iterable of input data into the output model format.

        Args:
            data: An iterable collection of input data to be presented.

        Returns:
            Iterable[OutputModel]: An iterable collection of presented output models.
        """
        return [self.present(item) for item in data]


__all__ = ["Presenter"]

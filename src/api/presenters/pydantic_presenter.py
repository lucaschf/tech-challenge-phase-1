from abc import ABC, abstractmethod
from typing import Iterable

from pydantic import BaseModel


class PydanticPresenter[OutputModel: BaseModel, InputData](ABC):
    """Abstract base class for presenters that transform input data into Pydantic models.

    Presenters are responsible for converting raw data (e.g., dictionaries, database results)
    into structured Pydantic models for easier handling and validation in your application.

    Type Parameters:
        OutputModel: The type of Pydantic model this presenter will produce.
        InputData: The type of input data this 'presenter' expects to receive.

    Methods:
        present(data: InputData) -> OutputModel:
            Abstract method to be implemented by subclasses.
            Transforms the given `data` into the corresponding `OutputModel`.
    """

    @abstractmethod
    def present(self, data: InputData) -> OutputModel:
        """Transforms the input data into the corresponding Pydantic model.

        Args:
            data: The raw input data to be transformed.

        Returns:
            The Pydantic model representing the transformed data.
        """

    def present_many(self, data: Iterable[InputData]) -> Iterable[OutputModel]:
        """Transforms a list of input data into a list of Pydantic models.

        Args:
            data: A list of raw input data to be transformed.

        Returns:
            A list of Pydantic models representing the transformed data.
        """
        return [self.present(item) for item in data]


__all__ = ["PydanticPresenter"]

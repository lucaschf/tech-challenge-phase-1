from dataclasses import dataclass
from uuid import UUID


@dataclass
class ProductInputDTO:
    """A data transfer object (DTO) representing the input for creating a new product.

    Attributes:
    name: The name of the product.
    category: The category of the product.
    price: The price of the product.
    description: The description of the product.
    images: A list of image URLs for the product.
    """

    name: str
    category: str
    price: float
    description: str
    images: list[str]


@dataclass
class ProductOutputDTO:
    """A data transfer object (DTO) representing the output for a product.

    Attributes:
    id: The unique identifier of the product.
    name: The name of the product.
    category: The category of the product.
    price: The price of the product.
    description: The description of the product.
    images: A list of image URLs for the product.

    Note: This class is used for returning product data to the client.
    """

    uuid: UUID
    name: str
    category: str
    price: float
    description: str
    images: list[str]


__all__ = ["ProductInputDTO", "ProductOutputDTO"]

from typing import Any, Dict, Tuple, Type

from pydantic import GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import core_schema

from src.core.domain.exceptions.category_error import InvalidCategoryError
from src.core.domain.value_objects.category import Category


class CategoryStr(str):
    """A custom type for handling Category strings.

    This type ensures that the Category is valid according to the predefined categories.
    """

    @classmethod
    def __get_pydantic_core_schema__(
        cls: Type["CategoryStr"],
        *_args: Tuple[()],
        **_kwargs: Dict[str, Any],
    ) -> core_schema.CoreSchema:
        """Return a Pydantic core schema for this type."""
        return core_schema.with_info_after_validator_function(
            cls._validate_category,
            core_schema.str_schema(),
        )

    @classmethod
    def _validate_category(
        cls: Type["CategoryStr"],
        __input_value: str,
        _: core_schema.ValidationInfo | None = None,
    ) -> str:
        """Validate the given Category string.

        Args:
            __input_value: The Category string to validate.
            _: Other values from the Pydantic model. This argument is only for Pydantic
             compatibility and is not used.

        Returns:
            The validated Category string.

        Raises:
            ValueError if the Category is invalid.
        """
        try:
            return Category(__input_value).category
        except InvalidCategoryError as error:
            raise ValueError(error.message) from error

    @classmethod
    def __get_pydantic_json_schema__(
        cls,
        schema: core_schema.CoreSchema,
        handler: GetJsonSchemaHandler,
    ) -> JsonSchemaValue:
        json_schema = handler(schema)
        json_schema.update(
            type="string",
            example="Lanche",
        )
        return json_schema

    def __new__(cls: Type["CategoryStr"], category: str) -> "CategoryStr":
        """Create a new instance of CategoryStr.

        Args:
            category: The Category string to validate.

        Returns:
            A new CategoryStr instance with the validated Category string.
        """
        return super(CategoryStr, cls).__new__(cls, cls._validate_category(category))  # type: ignore


__all__ = ["CategoryStr"]

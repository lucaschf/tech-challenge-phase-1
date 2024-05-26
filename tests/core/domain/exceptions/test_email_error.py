import pytest

from src.core.domain.exceptions import InvalidEmailError
from src.core.domain.value_objects import Email


def test_invalid_email_error_access_email_address_property() -> None:
    email_str = "invalid_email"
    with pytest.raises(InvalidEmailError) as exc_info:
        Email(email_str)

    assert exc_info.value.email_address == email_str

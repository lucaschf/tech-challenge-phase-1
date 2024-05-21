import pytest

from src.core.domain.base import DomainError
from src.core.domain.value_objects.email import Email


@pytest.mark.parametrize(
    "valid_email",
    [
        "test@example.com",
        "user.name@subdomain.example.org",
        "very_long_username+alias@domain.com.br",
    ],
)
def test_creation_of_valid_email(valid_email: str) -> None:
    email = Email(valid_email)
    assert email.address == valid_email


@pytest.mark.parametrize(
    "invalid_email",
    ["test@example", "user.name@.org", "@subdomain.example.com", "invalid_email", "test", "123"],
)
def test_creation_of_invalid_email(invalid_email: str) -> None:
    with pytest.raises(DomainError):
        Email(invalid_email)


def test_access_email_property() -> None:
    email_str = "test@example.com"
    email = Email(email_str)
    assert email.address == email_str


def test_get_equality_components() -> None:
    email_str = "test@example.com"
    email = Email(email_str)
    assert email._get_equality_components() == (email_str,)


@pytest.mark.parametrize(
    "email1, email2, expected",
    [
        ("test@example.com", "test@example.com", True),
        ("test@example.com", "other@example.com", False),
        ("test@example.com", "test@example.org", False),
    ],
)
def test_equality_of_emails(email1: str, email2: str, expected: bool) -> None:
    email_obj1 = Email(email1)
    email_obj2 = Email(email2)
    assert (email_obj1 == email_obj2) == expected


@pytest.mark.parametrize(
    "email, expected",
    [
        ("test@example.com", True),
        ("user.name@subdomain.example.org", True),
        ("very_long_username+alias@domain.com.br", True),
        ("test@example", False),
        ("user.name@.org", False),
        ("@subdomain.example.com", False),
        ("invalid_email", False),
    ],
)
def test_static_method_is_valid(email: str, expected: bool) -> None:
    assert Email._is_valid(email) == expected


@pytest.mark.parametrize(
    "email_address",
    ["test@example.com", "test@example.org"],
)
def test_str(email_address: str) -> None:
    email = Email(email_address)
    assert str(email) == email_address

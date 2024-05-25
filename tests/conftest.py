import pytest
from fastapi.testclient import TestClient

from src.adapter.driver.api import app


@pytest.fixture
def client():  # noqa: ANN201
    with TestClient(app) as c:
        yield c

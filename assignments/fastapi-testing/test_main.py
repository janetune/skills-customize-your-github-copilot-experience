import pytest
from fastapi.testclient import TestClient

import main

client = TestClient(main.app)


@pytest.fixture(autouse=True)
def reset_items():
    main.items[:] = [item.copy() for item in main.INITIAL_ITEMS]
    yield
    main.items[:] = [item.copy() for item in main.INITIAL_ITEMS]


def test_read_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Task API!"}


def test_read_items():
    # TODO: Request GET /items and check the response status and item list.
    pass


def test_read_item():
    # TODO: Request GET /items/1 and check the returned item's fields.
    pass


def test_create_item():
    # TODO: POST a new item, then check its status code and returned fields.
    pass


def test_missing_item():
    # TODO: Request an unknown item and check the 404 response.
    pass


def test_invalid_item():
    # TODO: POST an item without its required name and check the 422 response.
    pass

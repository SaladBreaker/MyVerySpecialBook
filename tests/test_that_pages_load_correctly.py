import pytest
from tests.fixtures import client, configed_app


def test_user_can_access_home_page(client, configed_app):
    with configed_app.test_request_context():
        response = client.get("/home", follow_redirects=False)

    assert (
        response.status_code == 200
    ), f"Home page can not be accessed. Status code: {response.status_code}"


def test_user_can_access_addbook_page(client, configed_app):
    with configed_app.test_request_context():
        response = client.get("/addbook", follow_redirects=False)

    assert (
        response.status_code == 200
    ), f"Addbook page can not be accessed. Status code: {response.status_code}"


def test_user_can_access_addfile_page(client, configed_app):
    with configed_app.test_request_context():
        response = client.get("/addfile", follow_redirects=False)

    assert (
        response.status_code == 200
    ), f"Addfile page can not be accessed. Status code: {response.status_code}"


def test_user_can_access_allbooks_page(client, configed_app):
    with configed_app.test_request_context():
        response = client.get("/allbooks", follow_redirects=False)

    assert (
        response.status_code == 200
    ), f"Allbooks page can not be accessed. Status code: {response.status_code}"

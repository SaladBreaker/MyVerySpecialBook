import pytest
import random
import string

from flask_site.app import app


def random_string():
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(15))


def book():
    title = random_string()
    author = random_string()


@pytest.fixture
def configed_app():
    app.config["WTF_CSRF_ENABLED"] = False
    return app


@pytest.fixture
def client(configed_app):
    return configed_app.test_client()

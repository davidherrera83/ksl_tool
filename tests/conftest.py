import pytest

import fw
from models.user import UserModel
from models.item import ItemModel
from ksl.pages.ksl import KSL
from typing import List


@pytest.fixture
def user() -> UserModel:
    """Instance of user which reads from users.json to set user for each test."""
    _user = fw.get_user()

    return _user

@pytest.fixture
def items()  -> List[ItemModel]:
    _items = fw.get_items()

    return _items

@pytest.fixture
def ksl(py, user):
    """Instance of KSL for each test."""
    _ksl = KSL(py, user)

    return _ksl

@pytest.fixture
def login_to_ksl(py, user):
    _login = KSL(py, user).login()

    return _login

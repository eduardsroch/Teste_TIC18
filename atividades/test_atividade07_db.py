import pytest
from python.atividades.atividade07_db import User, Database, UserService

@pytest.fixture
def user():
    return User("Eduardo Soares", "eduardosroch@gmail.com")

@pytest.fixture
def db():
    return Database()

def test_save_user_valid(user, db):
    service = UserService(db)
    service.save_user(user)

def test_save_user_missing_name(user, db):
    user.name = ""
    service = UserService(db)
    with pytest.raises(ValueError):
        service.save_user(user)

def test_save_user_missing_email(user, db):
    user.email = ""
    service = UserService(db)
    with pytest.raises(ValueError):
        service.save_user(user)
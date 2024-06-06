import pytest
from python.atividades.atividade10_user_service import UserManager

class MockUserService:
    def get_user_info(self, user_id):
        if user_id == 1:
            return {"user_id": 1, "name": "Eduardo Soares"}
        else:
            return None

class TestUserManager:
    def test_fetch_user_info_existing_user(self):
        user_service = MockUserService()
        user_manager = UserManager(user_service)
        user_info = user_manager.fetch_user_info(1)
        assert user_info == {"user_id": 1, "name": "Eduardo Soares"}

    def test_fetch_user_info_non_existing_user(self):
        user_service = MockUserService()
        user_manager = UserManager(user_service)
        with pytest.raises(ValueError):
            user_manager.fetch_user_info(2)
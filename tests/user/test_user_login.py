import allure
import pytest
from methods.user_methods import UserMethods
from data import Data


class TestUserLogin:

    @allure.title('Проверка ответа при успешном логине пользователя')
    def test_login_user_check_response_successful(self, user_create_fixture):
        user = dict(user_create_fixture[0])
        del user['name']
        user_methods = UserMethods()
        token, response = user_methods.login_user(user)
        assert (response.status_code == 200) and ('"success":true' in response.text) and (token is not None)

    @allure.title('Проверка, что нельзя залогиниться с некорректными данными')
    @pytest.mark.parametrize("incorrect_field", ['email', 'password'])
    def test_login_user_check_incorrect_data(self, user_create_fixture, incorrect_field):
        user = dict(user_create_fixture[0])
        del user['name']
        user[incorrect_field] += 'a'
        user_methods = UserMethods()
        _, response = user_methods.login_user(user)
        assert (response.status_code == 401) and (response.text == Data.error_auth_user_incorrect_values_401)

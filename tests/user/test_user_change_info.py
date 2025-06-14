import allure
import pytest
from methods.user_methods import UserMethods
from data import Data


class TestUserChangeInfo:

    @allure.title('Проверка ответа при успешном изменении данных пользователя')
    @pytest.mark.parametrize('field', ['email', 'name'])
    def test_user_change_info_check_response_successful(self, user_create_fixture, field):
        user, token = dict(user_create_fixture[0]), user_create_fixture[1]
        del user['password']
        user[field] = 'new_' + user[field]
        user_methods = UserMethods()
        response = user_methods.change_user_info(user, token)
        assert ((response.status_code == 200) and ('"success":true' in response.text) and
                (f'"{field}":"{user[field]}"' in response.text))

    @allure.title('Проверка, что нельзя изменить данные пользователя без авторизации')
    @pytest.mark.parametrize('field', ['email', 'name'])
    def test_user_change_info_check_without_authorization(self, user_create_fixture, field):
        user = dict(user_create_fixture[0])
        del user['password']
        user[field] = 'new_' + user[field]
        user_methods = UserMethods()
        response = user_methods.change_user_info(user)
        assert (response.status_code == 401) and (response.text == Data.error_user_without_auth_401)

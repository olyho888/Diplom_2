import allure
import pytest
from methods.user_methods import UserMethods
from helpers import Helpers
from data import Data


class TestUserCreate:

    @allure.title('Проверка кода ответа и текста ответа при успешном создании пользователя')
    def test_user_create_check_status_code_and_text_successful(self):
        user_methods = UserMethods()
        _, response = user_methods.create_user()
        assert (response.status_code == 200) and ('"success":true' in response.text)

    @allure.title('Проверка, что нельзя создать пользователя с уже существующим email')
    def test_user_create_check_same_email_creation(self):
        user_methods = UserMethods()
        user, _ = user_methods.create_user()
        user_2 = {'email': user['email'],
                  'password': user['password'] + 'a',
                  'name': user['name'] + 'a'}
        _, response = user_methods.create_user(user_2)
        assert (response.status_code == 403) and (response.text == Data.error_create_user_already_present_403)

    @allure.title('Проверка, что нельзя создать пользователя, если нет одного из обязательных полей')
    @pytest.mark.parametrize("absent_field", ['email', 'password', 'name'])
    def test_user_create_check_required_field_absence(self, absent_field):
        user_methods = UserMethods()
        username = Helpers.generate_random_string(6)
        user = {'email': Helpers.generate_random_email(username),
                'password': Helpers.generate_random_string(6),
                'name': username}
        del user[absent_field]
        _, response = user_methods.create_user(user)
        assert (response.status_code == 403) and (response.text == Data.error_create_user_missing_values_403 )

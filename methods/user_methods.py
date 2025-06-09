import allure
import requests
from data import Data
from helpers import Helpers


class UserMethods:

    @allure.step('Создание уникального пользователя')
    def create_user(self, params=None):
        if params is None:
            username = Helpers.generate_random_string(6)
            params = {'email': Helpers.generate_random_email(username),
                      'password': Helpers.generate_random_string(6),
                      'name': username}
        response = requests.post(url=f'{Data.AUTH_URL}/register', data=params, verify=False)
        return params, response

    @allure.step('Создание уникального пользователя с проверкой успешности')
    def create_user_successful(self, params=None):
        if params is None:
            username = Helpers.generate_random_string(6)
            params = {'email': Helpers.generate_random_email(username),
                      'password': Helpers.generate_random_string(6),
                      'name': username}
        response = requests.post(url=f'{Data.AUTH_URL}/register', data=params, verify=False)
        if response.status_code == 200:
            token = response.json()['accessToken']
            return params, token
        else:
            raise AssertionError('Ошибка при создании пользователя')

    @allure.step('Авторизация пользователя')
    def login_user(self, params):
        token = None
        response = requests.post(url=f'{Data.AUTH_URL}/login', data=params, verify=False)
        if response.status_code == 200:
            token = response.json()['accessToken']
        return token, response

    @allure.step('Изменение данных пользователя')
    def change_user_info(self, params, token=None):
        if token is not None:
            headers = {'Authorization': token}
            response = requests.patch(url=f'{Data.AUTH_URL}/user', headers=headers, data=params, verify=False)
        else:
            response = requests.patch(url=f'{Data.AUTH_URL}/user', data=params, verify=False)
        return response

    @allure.step('Удаление пользователя')
    def delete_user(self, token):
        headers = {'Authorization': token}
        response = requests.delete(url=f'{Data.AUTH_URL}/user', headers=headers, verify=False)
        return response

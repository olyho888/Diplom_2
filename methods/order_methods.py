import allure
import requests
from data import Data

class OrderMethods:

    @allure.step('Получение данных об ингредиентах')
    def get_ingredients(self):
        ingredients = []
        response = requests.get(url=f'{Data.BASE_URL}/ingredients', verify=False)
        if response.status_code == 200:
            data = response.json()['data']
            ingredients.append(data[0]["_id"])
            ingredients.append(data[1]["_id"])
        return ingredients

    @allure.step('Создание заказа')
    def create_order(self, params, token, auth):
        number = None
        if auth:
            headers = {'Authorization': token}
            response = requests.post(url=f'{Data.ORDERS_URL}', data=params, headers=headers, verify=False)
        else:
            response = requests.post(url=f'{Data.ORDERS_URL}', data=params, verify=False)
        if response.status_code == 200:
            number = response.json()['order']['number']
        return number, response

    @allure.step('Создание заказа с авторизацией и проверкой успешности')
    def create_order_with_auth_successful(self, params, token):
        headers = {'Authorization': token}
        response = requests.post(url=f'{Data.ORDERS_URL}', data=params, headers=headers, verify=False)
        if response.status_code == 200:
            number = response.json()['order']['number']
            return number, response
        else:
            raise AssertionError('Ошибка при создании заказа')

    @allure.step('Получение заказов пользователя')
    def get_user_orders(self, token=None):
        numbers = []
        if token is not None:
            headers = {'Authorization': token}
            response = requests.get(url=f'{Data.ORDERS_URL}', headers=headers, verify=False)
        else:
            response = requests.get(url=f'{Data.ORDERS_URL}', verify=False)
        if response.status_code == 200:
            orders = response.json()['orders']
            for order in orders:
                numbers.append(order['number'])
        return numbers, response

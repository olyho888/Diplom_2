import allure
import pytest
from methods.order_methods import OrderMethods
from data import Data


class TestOrderCreate:

    @allure.title('Проверка, что можно создать заказ с ингредиентами')
    @pytest.mark.parametrize('auth', [True, False])
    def test_order_create_with_ingredients_successful(self, user_create_fixture, auth):
        token = user_create_fixture[1]
        order_methods = OrderMethods()
        params = {'ingredients': order_methods.get_ingredients()}
        number, response = order_methods.create_order(params, token, auth)
        assert (response.status_code == 200) and ('"success":true' in response.text) and (number is not None)

    @allure.title('Проверка, что нельзя создать заказ без ингредиентов')
    @pytest.mark.parametrize('auth', [True, False])
    def test_order_create_without_ingredients(self, user_create_fixture, auth):
        token = user_create_fixture[1]
        order_methods = OrderMethods()
        params = {'ingredients': []}
        number, response = order_methods.create_order(params, token, auth)
        assert (response.status_code == 400) and (response.text == Data.error_order_without_ingredients_400)

    @allure.title('Проверка, что нельзя создать заказ c неверным хешем ингредиентов')
    @pytest.mark.parametrize('auth', [True, False])
    def test_order_create_incorrect_ingredients(self, user_create_fixture, auth):
        token = user_create_fixture[1]
        order_methods = OrderMethods()
        ingredients = order_methods.get_ingredients()
        for i in range(len(ingredients)):
            ingredients[i] += '1a'
        params = {'ingredients': ingredients}
        number, response = order_methods.create_order(params, token, auth)
        assert (response.status_code == 500) and ("Internal Server Error" in response.text)

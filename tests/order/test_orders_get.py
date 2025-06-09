import allure
from methods.order_methods import OrderMethods
from data import Data


class TestOrdersGet:

    @allure.title('Проверка, что можно получить список заказов авторизированному пользователю')
    def test_orders_get_for_auth_user_finish_successful(self, orders_create_fixture):
        token, expected_numbers = orders_create_fixture
        order_methods = OrderMethods()
        numbers, response = order_methods.get_user_orders(token)
        assert (response.status_code == 200) and ('"success":true' in response.text) and (numbers == expected_numbers)

    @allure.title('Проверка, что неавторизированный пользователь не может получить список заказов')
    def test_orders_get_for_not_auth_user(self, orders_create_fixture):
        order_methods = OrderMethods()
        _, response = order_methods.get_user_orders()
        assert (response.status_code == 401) and (response.text == Data.error_user_without_auth_401)

import pytest
from methods.user_methods import UserMethods
from methods.order_methods import OrderMethods


@pytest.fixture
def user_create_fixture():
    user_methods = UserMethods()
    user, token = user_methods.create_user_successful()
    yield user, token
    user_methods.delete_user(token)

@pytest.fixture
def orders_create_fixture():
    numbers = []
    user_methods = UserMethods()
    _, token = user_methods.create_user_successful()
    order_methods = OrderMethods()
    params = {'ingredients': order_methods.get_ingredients()}
    for i in range(3):
        number, _ = order_methods.create_order_with_auth_successful(params, token)
        numbers.append(number)
    yield token, numbers
    user_methods.delete_user(token)

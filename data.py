class Data:

    BASE_URL = 'https://stellarburgers.nomoreparties.site/api'
    AUTH_URL = f'{BASE_URL}/auth'
    ORDERS_URL = f'{BASE_URL}/orders'

    error_create_user_already_present_403 = '{"success":false,"message":"User already exists"}'
    error_create_user_missing_values_403 = '{"success":false,"message":"Email, password and name are required fields"}'
    error_auth_user_incorrect_values_401 = '{"success":false,"message":"email or password are incorrect"}'
    error_user_without_auth_401 = '{"success":false,"message":"You should be authorised"}'
    error_order_without_ingredients_400 = '{"success":false,"message":"Ingredient ids must be provided"}'

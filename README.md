# Diplom_2

Тесты для тестирования API для Stellar Burgers (https://stellarburgers.nomoreparties.site/). Его документация: https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma/api-documentation.pdf?etag=3403196b527ca03259bfd0cb41163a89

Основа для написания тестов — фреймворк pytest и библиотека requests
Директория allure-report - содержит отчет о результатах выполнения тестов, сгенерированный с посмощью фреймворк Allure

Проект состоит из:

Директории methods - содержит методы:
order_methods - выполняемые методы для работы с заказом
user_methods - выполняемые методы для работы с пользователе

Директория tests - содержит в себе поддиректории:

order - влючает тесты:
- test_order_create - тесты на проверку создания заказа
- test_orders_get - тесты на проверку получения списка заказов

user - включает тесты:
- test_user_create - тесты на проверку создания пользователя 
- test_user_login - тесты на проверку авторизации пользователя 
- test_user_change_info - тесты на проверку изменений данных пользователя

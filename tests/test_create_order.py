import allure
import pytest

from data import DataOrder
from helper import Helper
from methods.order_methods import OrderMethods


class TestCreateOrder:
    @allure.title("Test select color and order scooter")
    @allure.description("Тест проверяет выбор цветов самоката и создание заказа")
    @pytest.mark.parametrize("color", DataOrder.color)
    def test_create_order(self, color):
        payload = Helper.modify_create_order_body("color", color)
        response = OrderMethods.create_order(payload)
        assert 201 == response.status_code
        response = response.json()
        number = response["track"]
        OrderMethods.cancel_order(number)

    @allure.title("Test body contains track create order")
    @allure.description("Тест проверяет что тело ответа содержит track при создании заказа")
    def test_body_contains_track_create_order(self):
        response = OrderMethods.create_order(DataOrder.ORDER_DATA)
        assert 'track' in response.json()
        response = response.json()
        number = response["track"]
        OrderMethods.cancel_order(number)


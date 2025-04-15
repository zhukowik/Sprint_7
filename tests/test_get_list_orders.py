import allure

from methods.order_methods import OrderMethods


class TestGetListOrders:
    @allure.title("Тest Get list orders")
    @allure.description("Тест получения списка заказов")
    def test_get_list_orders(self):
        response = OrderMethods.get_list_order()
        assert 'orders' in response.json()
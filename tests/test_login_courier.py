import allure
import requests
from data import DataCourier
from methods.courier_methods import CourierMethods


class TestLoginCourier:
    @allure.title("Test sucsessfull login courier")
    @allure.description("Проверяем успешную авторизацию курьера")
    def test_sucsessfull_login_courier(self):
        response = CourierMethods.login_courier(DataCourier.LOGIN_COURIER, DataCourier.PASSWORD_COURIER)
        assert response.status_code == 200

    @allure.title("Test all required fields must be submitted for authorization.")
    @allure.description("Проверка Авторизации при пустых полях")
    def test_all_required_fields_must_be_submitted_for_authorization(self):
        response = CourierMethods.login_courier("", "")
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}

    @allure.title("Test error enter your username or password incorrectly")
    @allure.description("Проверка ошибки авторизации с некорректными данными")
    def test_error_enter_your_username_or_password_incorrectly(self):
        response = CourierMethods.login_courier("ArtemZ132", "Artem132")
        assert response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}

    @allure.title("Test required field must be password for authorization.")
    @allure.description("Проверка ошибки авторизации с пустым поле пароль")
    def test_required_field_must_be_password_for_authorization(self):
        response = CourierMethods.login_courier("ArtemZ132", "")
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}

    @allure.title("Test error by a non-existent user")
    @allure.description("Проверка ошибки авторизации с несуществующим пользователем")
    def test_error_by_a_non_existent_user(self):
        response = CourierMethods.login_courier("Artem1231323123123", "Artem13212333333333")
        assert response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}

    @allure.title("Test sucsessfull login courier return id")
    @allure.description("Проверка успешной авторизации и возращение id")
    def test_sucsessfull_login_courier_return_id(self):
        response = CourierMethods.login_courier(DataCourier.LOGIN_COURIER, DataCourier.PASSWORD_COURIER)
        assert {'id': 502688} == response.json()
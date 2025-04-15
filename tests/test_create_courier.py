from methods.courier_methods import CourierMethods
import allure

class TestCreateCourier:
    @allure.title('Test sucsessfull create courier')
    @allure.description('Тут создаем курьера и проверяем тело')
    def test_successful_create_courier(self):
        new_courier = CourierMethods.create_new_courier()
        assert {'ok': True} == new_courier[0].json()
        print(new_courier)
        id_courier = CourierMethods.get_id_courier(new_courier[1], new_courier[2])
        CourierMethods.delete_courier(id_courier)

    @allure.title('Test cant create two identical couriers')
    @allure.description('Тут создаем курьера с существующими данными и проверяем тело')
    def test_cant_create_two_identical_couriers(self):
        new_courier = CourierMethods.create_new_courier()
        response = CourierMethods.create_courier(new_courier[1], new_courier[2], new_courier[3])
        assert response.json() == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
        id_courier = CourierMethods.get_id_courier(new_courier[1], new_courier[2])
        CourierMethods.delete_courier(id_courier)

    @allure.title('Test to create a courier,need to pass all the required fields to the handle.')
    @allure.description('Тут при создании курьера оставляем обязательные поля пустыми')
    def test_create_courier_need_to_pass_all_required_fields_to_handle(self):
        response = CourierMethods.create_courier('','','')
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}

    @allure.title('Test sucsessfull code response courier')
    @allure.description('Тут создаем курьера и проверяем код ответа')
    def test_successful_create_courier(self):
        new_courier = CourierMethods.create_new_courier()
        assert 201 == new_courier[0].status_code
        id_courier = CourierMethods.get_id_courier(new_courier[1], new_courier[2])
        CourierMethods.delete_courier(id_courier)

    @allure.title('Test sucsessfull create courier return {"ok": True}')
    @allure.description('Тут создаем курьера и проверяем {"ok": True}')
    def test_successful_create_courier(self):
        new_courier = CourierMethods.create_new_courier()
        assert {'ok': True} == new_courier[0].json()
        id_courier = CourierMethods.get_id_courier(new_courier[1], new_courier[2])
        CourierMethods.delete_courier(id_courier)

    @allure.title('Test one_of the fields missing the request returns an error')
    @allure.description('При создании курьера если  отсутствует одно из полей, возвращается ошибка')
    def test_one_of_the_fields_missing_the_request_returns_an_error(self):
        response = CourierMethods.create_courier('', 'zaqq', 'xswq')
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}

    @allure.title("Test create a user with a username that already exists, an error is returned.")
    @allure.description("При создании курьера с существующим логином, возвращается ошибка")
    def test_create_user_with_login_that_already_exists_an_error_returned(self):
        new_courier = CourierMethods.create_new_courier()
        response = CourierMethods.create_courier(new_courier[1], 'qwer0987', 'ivan')
        assert response.json() == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
        id_courier = CourierMethods.get_id_courier(new_courier[1], new_courier[2])
        CourierMethods.delete_courier(id_courier)


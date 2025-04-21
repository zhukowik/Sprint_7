

class Url:
    MAIN_SITE = 'https://qa-scooter.praktikum-services.ru'
    CREATE_COURIER = f'{MAIN_SITE}/api/v1/courier'
    LOGIN_COURIER = f'{MAIN_SITE}/api/v1/courier/login'
    CREATE_ORDER = f'{MAIN_SITE}/api/v1/orders'
    CANCEL_ORDER = f'{MAIN_SITE}/api/v1/orders/cancel'
    GET_LIST_ORDER = f'{MAIN_SITE}/api/v1/orders'
    @staticmethod
    def url_delete_courier(id_courier):
        return f'https://qa-scooter.praktikum-services.ru/api/v1/courier/:{id_courier}'



class DataCourier:
    LOGIN_COURIER = "ArtemZ123"
    PASSWORD_COURIER = "ArtemZ123"
    FIRST_NAME_COURIER = "ArtemZ123"

class DataOrder:
    ORDER_DATA = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
    "color": ["GREY", "BLACK"]
}
    color = [["BLACK"],["GREY"], ["GREY", "BLACK"], [""]]

    @staticmethod
    def cancel_order_body(number):
        return {"track": number}
import requests
from faker import Faker
from data import Url
from generators_data import GeneratePayload

fake = Faker()

class CourierMethods:
    @staticmethod
    def create_new_courier(payload):
        login = payload['login']
        password = payload['password']
        first_name = payload['firstName']
        return requests.post(Url.CREATE_COURIER, data=payload), login, password, first_name

    @staticmethod
    def create_courier(login, password, first_name):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return requests.post(Url.CREATE_COURIER, data=payload)

    @staticmethod
    def get_id_courier(login, password):
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(Url.LOGIN_COURIER, data=payload)
        id_courier = response.json()
        return id_courier["id"]

    @staticmethod
    def delete_courier(id_courier):
        return requests.delete(Url.url_delete_courier(id_courier))

    @staticmethod
    def login_courier(login, password):
        payload = {
            "login": login,
            "password": password
        }
        return requests.post(Url.LOGIN_COURIER, data=payload)
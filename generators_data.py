import random

from faker import Faker
fake = Faker()

class GeneratePayload:
    @staticmethod
    def generate_courier_payload():
        # генерируем логин, пароль и имя курьера
        login = fake.text(5)
        password = fake.password()
        first_name = fake.first_name()

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return payload

    @staticmethod
    def generate_order_payload():
        lict_colour = ["BLACK", "GREY"]
        return {
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "address": fake.address(),
            "metroStation": fake.random_int(min=1, max=20),
            "phone": fake.phone_number(),
            "rentTime": fake.random_int(min=1, max=7),
            "deliveryDate": fake.date_between(start_date='today', end_date='+30d').isoformat(),
            "comment": fake.word(),
            "color": [
                random.choice(lict_colour)
            ]
        }
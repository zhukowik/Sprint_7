import pytest

from generators_data import GeneratePayload
from methods.courier_methods import CourierMethods


@pytest.fixture
def generate_courier_data():
    courier_body = GeneratePayload.generate_courier_payload()
    login = courier_body['login']
    password = courier_body['password']
    firstname = courier_body['firstName']
    yield [courier_body, login, password, firstname]
    courier_id = CourierMethods.login_courier(login, password)
    CourierMethods.delete_courier(courier_id)
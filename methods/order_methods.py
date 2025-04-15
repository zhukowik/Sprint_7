import requests

from data import DataOrder, Url



class OrderMethods:

    @staticmethod
    def create_order(payload):
        return requests.post(Url.CREATE_ORDER, data=payload)

    @staticmethod
    def cancel_order(number):
        payload = DataOrder.cancel_order_body(number)
        return requests.put(Url.CANCEL_ORDER, data=payload)

    @staticmethod
    def get_list_order():
        return requests.get(Url.GET_LIST_ORDER)




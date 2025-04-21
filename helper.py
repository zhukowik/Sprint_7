import data

class Helper:
    @staticmethod
    def modify_create_order_body(key,value):
        body = data.DataOrder.ORDER_DATA.copy()
        body[key]=value
        return body
import requests



class CART_MANAGEMENT:
    # host = str(socket.gethostbyname(socket.gethostname()))
    host = "localhost"
    port = 30000

    def __init__(self):
        pass

    def add_to_cart(self, user_id, product_id: int)->str:
        responce = requests.post(f'http://{self.host}:{self.port}/add_cart', json={
                "user_id": user_id,
                "product_id": product_id,
                "order_id": -1
            })
        return responce.json()

    def remove_from_cart(self, user_id: int, product_id: int)->str:
        responce = requests.post(f'http://{self.host}:{self.port}/remove_from_cart', json={
            "user_id": user_id,
            "product_id": product_id,
            "order_id": -1
        })
        return responce.json()

    def get_cart(self, user_id: int)->str:
        responce = requests.post(f'http://{self.host}:{self.port}/get_cart', json={
            "user_id": user_id,
            "product_id": -1,
            "order_id": -1
        })
        return responce.json()

    def clear_cart(self, user_id: int)->str:
        responce = requests.post(f'http://{self.host}:{self.port}/clear_cart', json={
            "user_id": user_id,
            "product_id": -1,
            "order_id": -1
        })
        return responce.json()

    def create_order(self, user_id: int, product_id: int)->str:
        responce = requests.post(f'http://{self.host}:{self.port}/create_order', json={
            "user_id": user_id,
            "product_id": product_id,
            "order_id": -1
        })
        return responce.json()

    def create_direct_order(self, user_id: int, product_id: int)->str:
        responce = requests.post(f'http://{self.host}:{self.port}/create_direct_order', json={
            "user_id": user_id,
            "product_id": product_id,
            "order_id": -1
        })


        return responce.json()

    def cancel_order(self, order_id: int)->str:
        responce = requests.post(f'http://{self.host}:{self.port}/cancel_order', json={
            "user_id": -1,
            "product_id": -1,
            "order_id": order_id
        })
        return responce.json()

    def get_all_orders(self, user_id: int)->list:
        responce = requests.post(f'http://{self.host}:{self.port}/get_all_orders', json={
            "user_id": user_id,
            "product_id": -1,
            "order_id": -1
        })
        value_list = []
        for i in responce.json():
            value_list.append(list(i.values()))

        return value_list

if __name__ == '__main__':
    CART = CART_MANAGEMENT()
    # print(CART.add_to_cart(13, 12))
    # print(CART.remove_from_cart(13,12))
    # print(CART.get_cart(13))
    # print(CART.clear_cart(13))
    # print(CART.create_order(user_id=13, product_id=12))
    # print(CART.create_direct_order(13, 12))
    # print(CART.cancel_order(5))
    # for i in CART.get_all_orders(user_id=13):
    #     print(i)



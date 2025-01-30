from functools import lru_cache
import requests
import io
import base64
import configparser
import os

from help_function.Crypt import Crypt


from help_function.cartmanagement import CART_MANAGEMENT

class Navigation(CART_MANAGEMENT):

    @staticmethod
    def read_config():
        base_dir = os.path.dirname(os.path.abspath(__file__))
        project_dir = os.path.dirname(base_dir)
        filename = os.path.join(project_dir, "client_config.ini")

        if not os.path.exists(filename):
            raise FileNotFoundError(f"Файл конфигурации не найден: {filename}")

        config = configparser.ConfigParser()
        config.read(filename)

        try:
            server_ip = config["server"]["ip"]
            server_port = int(config["server"]["port"])
        except KeyError as e:
            raise KeyError(f"Ошибка в конфигурационном файле: отсутствует ключ {e}")

        return [server_ip, server_port]

    def __init__(self):
        self.host, self.port = self.read_config()
        super().__init__()

    @lru_cache
    def get_image(self, name, val, style=None):
        if style:
            request = requests.get(f"http://{self.host}:{self.port}/images/{style}/{name}.{val}")
            base_64_image = base64.b64encode(io.BytesIO(request.content).read()).decode()
            return base_64_image
        else:
            request = requests.get(
                f"http://{self.host}:{self.port}/images/{name}.{val}")
            image = io.BytesIO(request.content)
            base_64_image = base64.b64encode(image.read()).decode()
            return base_64_image

    def get_products_total(self):
        try:
            response = requests.get(f"http://{self.host}:{self.port}/products/total")

            # Проверка успешного ответа от сервера (HTTP 200)
            if response.status_code == 200:
                # Преобразуем JSON-ответ в Python-словарь
                data = response.json()

                # Выводим полученные данные (можно адаптировать в зависимости от структуры данных)
                return data["products"]

            else:
                print(f"Ошибка при запросе данных: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"Произошла ошибка при подключении: {e}")

    def get_products_categoryes(self, name_category):
        try:
            response = requests.get(
                f"http://{self.host}:{self.port}/products/category/{name_category.replace(' ', '')}")

            # Проверка успешного ответа от сервера (HTTP 200)
            if response.status_code == 200:
                # Преобразуем JSON-ответ в Python-словарь
                data = response.json()

                # Выводим полученные данные (можно адаптировать в зависимости от структуры данных)
                return data["products"]

            else:
                print(f"Ошибка при запросе данных: {response.status_code}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Произошла ошибка при подключении: {e}")

    def get_product_id(self, id_product):
        try:
            response = requests.get(
                f"http://{self.host}:{self.port}/products/{id_product}")

            # Проверка успешного ответа от сервера (HTTP 200)
            if response.status_code == 200:
                # Преобразуем JSON-ответ в Python-словарь
                data = response.json()

                # Выводим полученные данные (можно адаптировать в зависимости от структуры данных)
                return data["id"]

            else:
                print(f"Ошибка при запросе данных: {response.status_code}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Произошла ошибка при подключении: {e}")

    def get_all_products(self):
        try:
            response = requests.get(f"http://{self.host}:{self.port}/products")

            if response.status_code == 200:
                data = response.json()
                return data['products']
            elif response.status_code == 404:
                print("Продукты не найдены.")
                return None
            else:
                print(f"Ошибка: {response.status_code} - {response.reason}", "get_all_products")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Произошла ошибка при подключении: {e}")
            return None

    def get_all_manufacturers(self):
        try:
            response = requests.get(f"http://{self.host}:{self.port}/manufacturers")

            # Проверяем успешность запроса
            if response.status_code == 200:
                # Возвращаем JSON-данные
                data = response.json()

                return data['manufacturers']
            elif response.status_code == 404:
                print("Производители не найдены.")
                return None
            else:
                print(f"Ошибка: {response.status_code} - {response.reason}", "get_all_manufacturers")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Произошла ошибка при подключении: {e}")
            return None

    def get_manufacturer_by_id(self, id: int):
        try:
            # Отправляем GET-запрос на эндпоинт с указанным ID
            response = requests.get(f"http://{self.host}:{self.port}/manufacturers/{id}")

            # Проверяем успешность запроса
            if response.status_code == 200:
                # Возвращаем JSON-данные
                data = response.json()
                return data['manufacturer']  # Ожидаем, что API возвращает ключ "manufacturer"
            elif response.status_code == 404:
                print(f"Производитель с ID {id} не найден.")
                return None
            else:
                print(f"Ошибка: {response.status_code} - {response.reason}", "get_manufacturer_by_id")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Произошла ошибка при подключении: {e}")
            return None

    def get_products_by_manufacturer(self, manufacturer: str):
        try:
            # Отправляем GET-запрос на эндпоинт
            response = requests.get(
                f"http://{self.host}:{self.port}/products/manufacturer/{manufacturer}"
            )

            # Проверяем успешность запроса
            if response.status_code == 200:
                # Преобразуем JSON-ответ в Python-словарь
                data = response.json()

                # Возвращаем список продуктов
                return data["products"]
            elif response.status_code == 404:
                print(f"Продукты производителя {manufacturer} не найдены.")
                return None
            else:
                print(f"Ошибка: {response.status_code} - {response.reason}", "get_products_by_manufacturer")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Произошла ошибка при подключении: {e}")
            return None

    def get_user_info(self, user_name, key):
        try:
            response = requests.get(f"http://{self.host}:{self.port}/profile/{user_name}/{key}")
            if response.status_code == 200:
                if isinstance(response.json(), str):
                    return response.json()
                else:
                    data = response.json()["inf"]
                    data = Crypt().decrypt_message(key, data)
                    data = data.split(",")
                    if isinstance(data, list):
                        return data
                    else:
                        return data
            elif response.status_code == 404:
                print(f"Произошла ошибка!")
                return None
            else:
                print(f"Ошибка: {response.status_code} - {response.reason}", "get_user_info")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Произошла ошибка при подключении: {e}")
            return None

    def update_photo(self, photo, key, id):
        try:
            muve = ["photo", photo]
            response = requests.post(f'http://{self.host}:{self.port}/editprofile', json={
                "id": id,
                "muve": muve,
                "key": key
            })
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                print(f"Произошла ошибка!")
                return None
            else:
                print(f"Ошибка: {response.status_code} - {response.reason}", "update_photo")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Произошла ошибка при подключении: {e}")
            return None

    def update_password(self, new_password, key, id):
        try:
            muve = ["password", new_password]
            response = requests.post(f'http://{self.host}:{self.port}/editprofile', json={
                "id": id,
                "muve": muve,
                "key": key
            })
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                print(f"Произошла ошибка!")
                return None
            else:
                print(f"Ошибка: {response.status_code} - {response.reason}", "update_password")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Произошла ошибка при подключении: {e}")
            return None

    def update_phone(self, number, key, id):
        try:
            muve = ["phone", number]
            response = requests.post(f'http://{self.host}:{self.port}/editprofile', json={
                "id": id,
                "muve": muve,
                "key": key
            })
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                print(f"Произошла ошибка!")
                return None
            else:
                print(f"Ошибка: {response.status_code} - {response.reason}", "update_phone")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Произошла ошибка при подключении: {e}")
            return None

    def LOG_OUT(self, key, id):
        try:
            muve = ["logout"]
            response = requests.post(f'http://{self.host}:{self.port}/editprofile', json={
                "id": id,
                "muve": muve,
                "key": key
            })
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                print(f"Произошла ошибка!")
                return None
            else:
                print(f"Ошибка: {response.status_code} - {response.reason}", "LOG_OUT")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Произошла ошибка при подключении: {e}")
            return None

    def DELETE_ACCOUNT(self, key, id):
        try:
            muve = ["delete"]
            response = requests.post(f'http://{self.host}:{self.port}/editprofile', json={
                "id": id,
                "muve": muve,
                "key": key
            })
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                print(f"Произошла ошибка!")
                return None
            else:
                print(f"Ошибка: {response.status_code} - {response.reason}", "DELETE_ACCOUNT")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Произошла ошибка при подключении: {e}")
            return None

    def search_product(self, name=None, category=None, min_price=None, max_price=None, manufacturer=None, color=None, sort_by=None ):
        try:
            if min_price and max_price:
                pass
            elif min_price:
                min_price = min_price
                max_price = 100000000000
            elif max_price:
                max_price = max_price
                min_price = 1
            else:
                pass
            response = requests.post(f'http://{self.host}:{self.port}/search', json={
                "search_term": name,
                "category": category,
                "min_price": min_price,
                "max_price": max_price,
                "manufacturer": manufacturer,
                "color": color,
                "sort_by": sort_by
            }
            )

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                print(f"Произошла ошибка!")
                return None
            else:
                print(f"Ошибка: {response.status_code} - {response.reason}", "search_product")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Произошла ошибка при подключении: {e}")
            return None

    def get_shop_state(self, user_role):
        if user_role == "admin":
            response = requests.get(f'http://{self.host}:{self.port}/get_state_shop')
            return response.json()
        return "У вас нет прав!"


    def update_shop_state(self, user_id):
        response = requests.post(f'http://{self.host}:{self.port}/set_state_shop', json={
            "user_id": user_id,
        })
        return response.json()
from functools import lru_cache
import requests
import io
import base64

class Navigation:
    host = "localhost"
    port = 30000
    def __init__(self):
        pass

    @lru_cache
    def get_image(self, name, val, style=None):
        if style:
            request = requests.get(f"http://{self.host}:{self.port}/images/{style}/{name}.{val}")
            base_64_image = base64.b64encode(io.BytesIO(request.content).read()).decode()
            return base_64_image
        else:
            request = requests.get(
                f"http://{self.host}:{self.port}/{name}.{val}")
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
            response = requests.get(f"http://{self.host}:{self.port}/products/category/{name_category.replace(' ', '')}")

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
                print(f"Ошибка: {response.status_code} - {response.reason}")
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
                print(f"Ошибка: {response.status_code} - {response.reason}")
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
                print(f"Ошибка: {response.status_code} - {response.reason}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Произошла ошибка при подключении: {e}")
            return None


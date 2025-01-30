from help_function.Crypt import Crypt
import requests


class Admin_control:
    # host = str(socket.gethostbyname(socket.gethostname()))
    host = "localhost"
    port = 30000

    def admin_command(self, user_id, command):
        command = command.decode('utf-8')
        user_id = int(user_id)
        request = requests.post(f"http://{self.host}:{self.port}/edit", json={
            "user_id": user_id,
            "data": command
        })
        return request.json()


class AdminDEF(Admin_control, Crypt):
    def __init__(self, user_id, key):
        super().__init__()
        self.admin_id = user_id
        self.key = key

    def update_user(self, user_id, user_name=None, password=None, phone_number=None, rule=None, photo=None, token=None):
        command = "edit_profile"

        # Формируем update_data только с непустыми значениями
        update_data = {
            "user_name": user_name,
            "password": password,
            "phone_number": phone_number,
            "role": rule,
            "photo": photo,
            "token": token
        }
        # Убираем ключи с пустыми значениями
        filtered_update_data = {key: value for key, value in update_data.items() if value is not None}

        # Формируем общий словарь команды
        dict_command = {
            "command": command,
            "data": {
                "user_id": user_id,
                "update_data": filtered_update_data
            }
        }

        # Отправка команды
        result = self.admin_command(self.admin_id, self.encrypt_dict(self.key, dict_command))
        res = self.decrypt_message(self.key, result)
        return res

    def get_users(self):
        command = "get_user_info"
        dict_command = {"command": command}
        result = self.admin_command(self.admin_id, self.encrypt_dict(self.key, dict_command))
        res = self.decrypt_dict(self.key, result)
        return res

    def update_products(self, product_id, product_name=None, category=None, manufacturer_id=None, price=None,
                        total_purchases=None,
                        color=None,
                        photo_base64=None, warehouse=None):
        command = "edit_product"
        # Формируем update_data только с непустыми значениями
        update_data = {
            "product_name": product_name,
            "category": category,
            "manufacturer_id": manufacturer_id,
            "price": price,
            "total_purchases": total_purchases,
            "color": color,
            "photo_base64": photo_base64,
            "warehouse": warehouse
        }
        # Убираем ключи с пустыми значениями
        filtered_update_data = {key: value for key, value in update_data.items() if value is not None}

        # Формируем общий словарь команды
        dict_command = {
            "command": command,
            "data": {
                "product_id": product_id,
                "update_data": filtered_update_data
            }
        }

        # Отправка команды
        result = self.admin_command(self.admin_id, self.encrypt_dict(self.key, dict_command))
        res = self.decrypt_message(self.key, result)
        return res

    def get_all_products(self):
        command = "get_products_info"
        dict_command = {"command": command}
        result = self.admin_command(self.admin_id, self.encrypt_dict(self.key, dict_command))
        res = self.decrypt_dict(self.key, result)
        return res

    def update_order(self, order_id, product_id=None, user_id=None, delivery_date=None, quantity=None, total_price=None, status=None):
        command = "edit_order"

        # Формируем update_data только с непустыми значениями
        update_data = {
            "product_id": product_id,
            "user_id": user_id,
            "delivery_date": delivery_date,
            "quantity": quantity,
            "total_price": total_price,
            "status": status
        }
        # Убираем ключи с пустыми значениями
        filtered_update_data = {key: value for key, value in update_data.items() if value is not None}

        # Формируем общий словарь команды
        dict_command = {
            "command": command,
            "data": {
                "order_id": order_id,
                "update_data": filtered_update_data
            }
        }

        # Отправка команды
        result = self.admin_command(self.admin_id, self.encrypt_dict(self.key, dict_command))
        res = self.decrypt_message(self.key, result)
        return res

    def get_all_orders(self):
        command = "get_orders_info"
        dict_command = {"command": command}
        result = self.admin_command(self.admin_id, self.encrypt_dict(self.key, dict_command))
        res = self.decrypt_dict(self.key, result)
        return res

    def update_manufacturer(self, manufacture_id, manufacturer_name=None, logo_base64=None, purchased_items_count=None):
        command = "edit_manufactures"
        # Формируем update_data только с непустыми значениями
        update_data = {
            "manufacturer_name": manufacturer_name,
            "logo_base64": logo_base64,
            "purchased_items_count": purchased_items_count
        }
        # Убираем ключи с пустыми значениями
        filtered_update_data = {key: value for key, value in update_data.items() if value is not None}

        # Формируем общий словарь команды
        dict_command = {
            "command": command,
            "data": {
                "manufacturer_id": manufacture_id,
                "update_data": filtered_update_data
            }
        }

        # Отправка команды
        result = self.admin_command(self.admin_id, self.encrypt_dict(self.key, dict_command))
        res = self.decrypt_message(self.key, result)
        return res

    def get_all_manufacturers(self):
        command = "get_manufacturer_info"
        dict_command = {"command": command}
        result = self.admin_command(self.admin_id, self.encrypt_dict(self.key, dict_command))
        res = self.decrypt_dict(self.key, result)
        return res

    def update_cart(self, item_id, cart_id=None, product_id=None, quantity=None, is_paid=None):
        command = "edit_cart"
        # Формируем update_data только с непустыми значениями
        update_data = {
            "cart_id": cart_id,
            "product_id": product_id,
            "quantity": quantity,
            "is_paid": is_paid
        }
        # Убираем ключи с пустыми значениями
        filtered_update_data = {key: value for key, value in update_data.items() if value is not None}

        # Формируем общий словарь команды
        dict_command = {
            "command": command,
            "data": {
                "cart_item_id": item_id,
                "update_data": filtered_update_data
            }
        }

        # Отправка команды
        result = self.admin_command(self.admin_id, self.encrypt_dict(self.key, dict_command))
        res = self.decrypt_message(self.key, result)
        return res

    def get_all_carts(self):
        command = "get_carts_info"
        dict_command = {"command": command}
        result = self.admin_command(self.admin_id, self.encrypt_dict(self.key, dict_command))
        res = self.decrypt_dict(self.key, result)
        return res

    def add_product(self, product_name, category, manufacturer_id, price, total_purchases, color, photo_base64, warehouse):
        command = "add_product"
        update_data = {
            "product_name": product_name,
            "category": category,
            "manufacturer_id": manufacturer_id,
            "price": price,
            "total_purchases": total_purchases,
            "color": color,
            "photo_base64": photo_base64,
            "warehouse": warehouse
        }
        dict_command = {
            "command": command,
            "data": {
                "update_data": update_data
            }
        }
        result = self.admin_command(self.admin_id, self.encrypt_dict(self.key, dict_command))
        res = self.decrypt_message(self.key, result)
        return res

    def delete_product(self, product_id):
        command = "delete_product"
        dict_command = {
            "command": command,
            "data": {
                "product_id": product_id
            }
        }
        result = self.admin_command(self.admin_id, self.encrypt_dict(self.key, dict_command))
        res = self.decrypt_message(self.key, result)
        return res

    def delete_account(self, user_id):
        command = "delete_account"
        dict_command = {
            "command": command,
            "data": {
                "user_id": user_id
            }
        }
        result = self.admin_command(self.admin_id, self.encrypt_dict(self.key, dict_command))
        res = self.decrypt_message(self.key, result)
        return res

    def block_account(self, user_id):
        command = "block_account"
        dict_command = {
            "command": command,
            "data": {
                "user_id": user_id
            }
        }
        result = self.admin_command(self.admin_id, self.encrypt_dict(self.key, dict_command))
        res = self.decrypt_message(self.key, result)
        return res

    def add_manufacturer(self, manufacturer_name, logo_base64, purchased_items_count):
        command = "add_manufacturer"
        add_data = {
            "manufacturer_name": manufacturer_name,
            "logo_base64": logo_base64,
            "purchased_items_count": purchased_items_count
        }
        dict_command = {
            "command": command,
            "data": {
                "add_data": add_data
            }
        }
        result = self.admin_command(self.admin_id, self.encrypt_dict(self.key, dict_command))
        res = self.decrypt_message(self.key, result)
        return res

    def delete_manufacturer(self, manufacturer_id):
        command = "delete_manufacturer"
        dict_command = {
            "command": command,
            "data": {
                "manufacturer_id": manufacturer_id
            }
        }
        result = self.admin_command(self.admin_id, self.encrypt_dict(self.key, dict_command))
        res = self.decrypt_message(self.key, result)
        return res




import base64

import aiohttp

from help_function.Admin_control import AdminDEF
from flet import *
from flet_route import Params, Basket

from help_function.Navigation import Navigation
from help_function.product_card import ProductCard
from help_function.user_card import UserCard
from help_function.manufacturer_card import ManufacturerCard
from help_function.Cart_admin_carD import CartCard
from help_function.Orders_admin_card import OrderCard


class Settings_shop_page(Navigation):
    def __init__(self):
        super().__init__()
        self.base64_photo = None

    def view(self, page: Page, params: Params, basket: Basket):
        def next_page(muve):
            page.client_storage.set("muve", muve)
            page.go("/loading")

        self.key, self.user_name = page.client_storage.get("key")
        user_info = self.get_user_info(self.user_name, self.key)
        self.id = user_info[0]
        self.name = user_info[1]
        self.number = user_info[2]
        self.role = user_info[3]
        self.photo = user_info[4]
        admin = AdminDEF(user_id=self.id, key=self.key)

        # Контейнер для отображения содержимого вкладок
        content_container = Column()

        # Функции для отображения содержимого вкладок
        def show_products_tab():
            content_container.controls.clear()
            products = admin.get_all_products()
            for product in products:
                product_card = ProductCard(
                    page=page,
                    id=product["id"],
                    product_name=product["product_name"],
                    category=product["category"],
                    manufacturer_id=product["manufacturer_id"],
                    price=product["price"],
                    total_purchases=product["total_purchases"],
                    color=product["color"],
                    photo_base64=product["photo_base64"],
                    warehouse=product["warehouse"],
                    admin_panel=admin,
                ).build()
                content_container.controls.append(product_card)
            page.update()

        def show_users_tab():
            content_container.controls.clear()
            users = admin.get_users()
            for user in users:
                if user["rule"] == "admin":
                    continue
                user_card = UserCard(
                    page=page,
                    user_id=user["user_id"],
                    name=user["user_name"],
                    password=user["password"],
                    number=user["phone_number"],
                    role=user["rule"],
                    photo=user["photo"],
                    token=user["token"],
                    admin_panel=admin
                ).build()
                content_container.controls.append(user_card)
            page.update()

        def show_manufacturers_tab():
            content_container.controls.clear()
            manufacturers = admin.get_all_manufacturers()
            for manufacturer in manufacturers:
                manufacturer_card = ManufacturerCard(
                    page=page,
                    id=manufacturer["id"],
                    name=manufacturer["manufacturer_name"],
                    photo=manufacturer["logo_base64"],
                    items_count=manufacturer["purchased_items_count"],
                    admin=admin,
                ).build()
                content_container.controls.append(manufacturer_card)
            page.update()

        def show_profile_tab():
            next_page("/profile")

        def show_cart_tab():
            content_container.controls.clear()
            carts = admin.get_all_carts()
            for cart in carts:
                cart_card = CartCard(
                    page=page,
                    id=cart["cart_item_id"],
                    cart_id=cart["cart_id"],
                    product_id=cart["product_id"],
                    total=cart["quantity"],
                    buy=cart["is_paid"]
                ).build()
                content_container.controls.append(cart_card)
            page.update()

        def show_order_tab():
            content_container.controls.clear()
            orders = admin.get_all_orders()
            for order in orders:
                order_card = OrderCard(
                    page=page,
                    id=order["order_id"],
                    product_id=order["product_id"],
                    user_id=order["user_id"],
                    order_date=order["order_date"],
                    delivery_date=order["delivery_date"],
                    price=order["total_price"],
                    status=order["status"]
                ).build()
                content_container.controls.append(order_card)
            page.update()

        def show_add_product_tab():
            content_container.controls.clear()

            # Поля для ввода данных товара
            name_field = TextField(label="Название товара", width=400)
            category_field = TextField(label="Категория", width=400)
            brand_field = TextField(label="бренд", width=400)
            price_field = TextField(label="цена", width=400)
            total_field = TextField(label="Количество покупателей", width=400)
            color_field = TextField(label="цвет", width=400)
            sclad_field = TextField(label="на складе", width=400)

            product_photo_url_field = TextField(label="URL фото товара")

            async def fetch_image_base64(image_url):
                try:
                    async with aiohttp.ClientSession() as session:
                        async with session.get(image_url) as response:
                            if response.status == 200:
                                image_bytes = await response.read()
                                return base64.b64encode(image_bytes).decode("utf-8")
                            else:
                                print(f"Ошибка при загрузке изображения: {response.status}")
                                return None
                except Exception as e:
                    print(f"Ошибка при загрузке изображения: {e}")
                    return None

            async def process_image():
                if product_photo_url_field.value:
                    try:
                        self.base64_photo = await fetch_image_base64(product_photo_url_field.value)
                        if self.base64_photo:
                            page.snack_bar = SnackBar(Text("Фото успешно загружено и преобразовано в Base64"))
                            print(f"Base64 Photo: {self.base64_photo[:15]}")  # Можно сохранить или использовать базу
                        else:
                            page.snack_bar = SnackBar(Text("Не удалось загрузить фото. Проверьте URL."))
                    except Exception as ex:
                        page.snack_bar = SnackBar(Text(f"Ошибка загрузки: {ex}"))
                    page.snack_bar.open = True
                    page.update()

            # Кнопка загрузки фото
            def upload_photo(e):
                import base64
                import requests
                if product_photo_url_field.value:
                    try:
                        response = requests.get(product_photo_url_field.value)
                        if response.status_code == 200:
                            self.base64_photo = base64.b64encode(response.content).decode('utf-8')
                            page.snack_bar = SnackBar(Text("Фото успешно загружено и преобразовано в Base64"))
                        else:
                            page.snack_bar = SnackBar(Text("Не удалось загрузить фото. Проверьте URL."))
                    except Exception as ex:
                        page.snack_bar = SnackBar(Text(f"Ошибка загрузки: {ex}"))
                    page.snack_bar.open = True
                    page.update()


            upload_photo_button = ElevatedButton(
                text="Загрузить фото",
                on_click=lambda e: upload_photo(e)
            )

            # Кнопка для добавления товара
            def add_product(e):

                admin.add_product(
                    product_name=name_field.value,
                    category=category_field.value,
                    manufacturer_id=int(brand_field.value),
                    price=float(price_field.value),
                    total_purchases=int(total_field.value),
                    color=color_field.value,
                    photo_base64=self.base64_photo,
                    warehouse=int(sclad_field.value),
                )
                page.snack_bar = SnackBar(Text(f"Товар '{name_field.value}' добавлен!"))
                page.snack_bar.open = True
                page.update()


            add_product_button = ElevatedButton(
                text="Добавить товар",
                on_click=add_product
            )

            # Размещение элементов на странице
            content_container.controls.append(
                Column([
                    name_field,
                    category_field,
                    brand_field,
                    price_field,
                    total_field,
                    color_field,
                    sclad_field,
                    Row([
                        product_photo_url_field,
                        upload_photo_button
                    ],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                    add_product_button
                ],
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,

                )
            )

            page.update()

        # Обработчик изменения вкладки
        def on_navigation_change(index):
            if index == 0:
                show_products_tab()
            elif index == 1:
                show_users_tab()
            elif index == 2:
                show_manufacturers_tab()
            elif index == 3:
                show_cart_tab()
            elif index == 4:
                show_order_tab()
            elif index == 5:
                show_add_product_tab()
            elif index == 6:
                show_profile_tab()

        # Навигационная панель
        navigation_bar = NavigationBar(
            destinations=[
                NavigationBarDestination(icon=Icons.SHOP, label="Товары"),
                NavigationBarDestination(icon=Icons.PERSON, label="Пользователи"),
                NavigationBarDestination(icon=Icons.FACTORY, label="Производители"),
                NavigationBarDestination(icon=Icons.SHOPPING_CART, label="Корзины"),
                NavigationBarDestination(icon=Icons.RECEIPT, label="Заказы"),
                NavigationBarDestination(icon=Icons.ADD_SHOPPING_CART_OUTLINED, label="Добавить товар"),
                NavigationBarDestination(icon=Icons.HOME, label="Профиль"),
            ],
            on_change=lambda e: on_navigation_change(
                e.control.selected_index if e.control.selected_index is not None else 0)
        )

        # Добавляем элементы на страницу
        content = Column([
            navigation_bar,
            content_container
        ])

        # Показать первую вкладку по умолчанию
        show_products_tab()

        return View("/settings_admin", controls=[content])

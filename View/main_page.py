import flet as ft
from flet_core import Alignment

from help_function.Navigation import Navigation
from help_function.Category_batton import Category_batton
from help_function.Card_generate import Card_generate
from flet_route import Params, Basket
from help_function.manufactures_card import Manufactures_Card


class Main_page(Navigation):
    def __init__(self):
        self.kat_but = Category_batton()
        self.instruments_light = [
            self.get_image("drum_light", "png", "LIGHT"),
            self.get_image("electro_light", "png", "LIGHT"),
            self.get_image("fleit_light", "png", "LIGHT"),
            self.get_image("guitar_light", "png", "LIGHT"),
            self.get_image("piano_light", "png", "LIGHT"),
            self.get_image("pick_light", "png", "LIGHT"),
        ]
        self.instruments_dark = [
            self.get_image("drum_dark", "png", "DARK"),
            self.get_image("electro_dark", "png", "DARK"),
            self.get_image("fleit_dark", "png", "DARK"),
            self.get_image("guitar_dark", "png", "DARK"),
            self.get_image("piano_dark", "png", "DARK"),
            self.get_image("pick_dark", "png", "DARK"),
        ]
        self.button_kat_names = [
            "Струнные",
            "Духовые",
            "Ударные",
            "Клавишные",
            "Электро инструменты",
            "Аксессуары",
            "Производители",
        ]
        self.image_paths = [
            self.get_image("1Струнные", "jpg", "MAIN"),
            self.get_image("2Духовые", "jpg", "MAIN"),
            self.get_image("3Ударные", "jpg", "MAIN"),
            self.get_image("4Клавишные", "jpg", "MAIN"),
            self.get_image("5Электро", "jpg", "MAIN"),
            self.get_image("6Аксессуары", "jpg", "MAIN"),
        ]
        super().__init__()

    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.theme_mode = ft.ThemeMode.DARK
        page.client_storage.set("style", page.theme_mode.value)

        self.get_products_total()

        def next_page(muve):
            page.theme_mode = ft.ThemeMode.DARK
            page.client_storage.set("muve", muve)
            page.go("/loading")

        def profile_muve(e):
            if page.client_storage.get("key") == None:
                next_page("/login")
            else:
                next_page("/profile")


        # Функция для конвертации Base64 в изображение
        def image_from_base64(base64_str: str):
            return ft.Image(src=f"data:image/jpeg;base64,{base64_str}", width=200, height=200)

        # Функция для обновления цветов
        def update_colors():
            if page.theme_mode == ft.ThemeMode.LIGHT:
                return {
                    "bgcolor": ft.colors.WHITE,
                    "border_color": ft.colors.BLACK,
                    "icon_color": ft.colors.BLACK,
                    "text_color": ft.colors.BLACK,
                    "tab_color": ft.colors.BLACK,
                    "border_color_info": ft.colors.BLACK12,
                    "card_background_color": ft.colors.BLACK12,
                    "icon_background_color": ft.colors.WHITE,
                    "card_border_color": ft.colors.BLACK,

                }
            else:
                return {
                    "bgcolor": ft.colors.BLACK,
                    "border_color": ft.colors.BLUE,
                    "icon_color": ft.colors.BLUE,
                    "text_color": ft.colors.BLUE,
                    "tab_color": ft.colors.BLUE,
                    "border_color_info": ft.colors.BLACK,
                    "card_background_color": ft.colors.BLACK,
                    "icon_background_color": ft.colors.BLACK,
                    "card_border_color": ft.colors.WHITE24,
                }

        def update_size():
            return {
                "icon_rectangle_size": 20,
                "divider_size": 5,
                "Menu_zag_text_size": 20,
                "Menu_other_text_size": 18,
                "Title_size": 35,
            }

        # Функция для смены темы
        def style_revert(e):
            if page.theme_mode == ft.ThemeMode.DARK:
                page.theme_mode = ft.ThemeMode.LIGHT
                icon_but.icon = ft.icons.DARK_MODE_OUTLINED
                icon_but.icon_color = ft.colors.BLACK
            else:
                page.theme_mode = ft.ThemeMode.DARK
                icon_but.icon = ft.icons.SUNNY
                icon_but.icon_color = ft.colors.BLUE

            colors = update_colors()
            name_shop.color = colors["text_color"]
            search_field.bgcolor = colors["bgcolor"]
            search_field.border_color = colors["border_color"]
            search_field.color = colors["text_color"]
            search_button.icon_color = colors["icon_color"]
            divider.color = colors["border_color"]

            # Обновление иконок в top_rectangle
            Cart_button.icon_color = colors["icon_color"]
            Profile_button.icon_color = colors["icon_color"]

            # Обновление фона с изображениями
            icon_back.content = update_images()

            # обновление меню
            Menu_but.icon_color = colors["icon_color"]

            # Menu_content.controls[0].bgcolor=update_colors()['bgcolor']
            # Menu_content.controls[0].border=update_colors()['border_color']
            """Обновление цветов в меню"""
            Menu_content.controls[0].bgcolor = update_colors()['bgcolor']
            Menu_content.controls[0].border = ft.border.all(2, update_colors()['border_color'])
            Menu_content.controls[0].content.controls[0].content.color = update_colors()['text_color']
            Menu_content.controls[0].content.controls[1].color = update_colors()['text_color']
            Menu_content.controls[0].content.controls[2].content.content.color = update_colors()['text_color']
            Menu_content.controls[0].content.controls[3].content.content.color = update_colors()['text_color']
            Menu_content.controls[0].content.controls[4].content.content.color = update_colors()['text_color']
            Menu_content.controls[0].content.controls[5].content.content.color = update_colors()['text_color']
            Menu_content.controls[0].content.controls[6].content.content.color = update_colors()['text_color']
            Menu_content.controls[0].content.controls[7].content.content.color = update_colors()['text_color']
            Menu_content.controls[0].content.controls[8].content.content.color = update_colors()['text_color']
            Menu_content.controls[0].content.controls[9].color = update_colors()['text_color']
            Menu_content.controls[0].content.controls[10].content.content.color = update_colors()['text_color']
            Menu_content.controls[0].content.controls[11].content.content.color = update_colors()['text_color']
            # Категории
            title_catigories.color = colors["text_color"]
            title_total_products.color = colors["text_color"]
            show_conteiner.content.controls[0].controls[0].bgcolor = update_colors()['bgcolor']
            show_conteiner.content.controls[0].controls[0].border = ft.border.all(2,
                                                                                  color=update_colors()['border_color'])
            show_conteiner.content.controls[0].controls[0].content.content.controls[1].color = update_colors()[
                'text_color']

            show_conteiner.content.controls[1].controls[0].bgcolor = update_colors()['bgcolor']
            show_conteiner.content.controls[1].controls[0].border = ft.border.all(2,
                                                                                  color=update_colors()['border_color'])
            show_conteiner.content.controls[1].controls[0].content.content.controls[1].color = update_colors()[
                'text_color']

            for card_app in product_card:
                updated_colors = card_app.update_colors()
                card_app.container1.bgcolor = updated_colors["bgcolor"]
                card_app.container1.border = ft.border.all(2, updated_colors["card_border_color"])
                # card_app.icon_container_.bgcolor = updated_colors["icon_background_color"]

                card_app.container1.content.controls[0].content.controls[0].border = ft.border.all(2, updated_colors[
                    "border_color"])
                card_app.container1.content.controls[1].color = updated_colors["text_color"]
                """Нижняя часть карточки"""
                card_app.container1.content.controls[2].bgcolor = updated_colors["bgcolor"]
                card_app.container1.content.controls[2].content.controls[0].controls[0].color = updated_colors[
                    "text_color"]
                card_app.container1.content.controls[2].content.controls[0].controls[1].color = updated_colors[
                    "text_color"]
                card_app.container1.content.controls[2].content.controls[0].controls[2].color = updated_colors[
                    "text_color"]
                card_app.container1.content.controls[2].content.controls[0].controls[3].color = updated_colors[
                    "text_color"]
                card_app.container1.content.controls[2].content.controls[0].controls[4].color = updated_colors[
                    "text_color"]
                # Обновляем элементы
                # card_app.icon_container_.update()
                card_app.container1.update()

            page.update()

        # Функция для обновления изображений на фоне
        def update_images():
            controls = []
            instruments = self.instruments_dark if page.theme_mode == ft.ThemeMode.DARK else self.instruments_light
            rows, cols = 20, 50
            for row in range(rows):
                row_controls = []
                for col in range(cols):
                    if (row + col) % 2 == 0:
                        instrument_image = instruments[(row * cols + col) % len(instruments)]
                        row_controls.append(
                            ft.Image(
                                src="data:image/png;base64," + instrument_image,
                                width=20,
                                height=20,
                                fit=ft.ImageFit.CONTAIN,
                            )
                        )
                    else:
                        row_controls.append(ft.Container(width=50, height=50))
                controls.append(ft.Row(row_controls, alignment=ft.MainAxisAlignment.CENTER))
            return ft.Column(controls, alignment=ft.MainAxisAlignment.CENTER)

        def animate_menu(e):
            Menu_content.offset = ft.transform.Offset(0, 0) if Menu_content.offset == ft.transform.Offset(-2,
                                                                                                          0) else ft.transform.Offset(
                -2, 0)
            Menu_content.update()

        def simple_search(e):
            name_product = search_field.value
            next_page(f"/search/:{name_product}")


        buttons = []
        for i in range(len(self.button_kat_names)):
            if i < len(self.image_paths):
                button = self.kat_but.build_card(self.button_kat_names[i],
                                                 f"/category/{self.button_kat_names[i].replace(" ", "")}", page,
                                                 self.image_paths[i])
            else:
                button = self.kat_but.build_card(self.button_kat_names[i],
                                                 f"/category/{self.button_kat_names[i].replace(" ", "")}", page)
            buttons.append(button)
        products = self.get_products_total()

        # Для каждого товара создаем карточку
        product_card = []
        if products:
            for product in products:
                id_product = product[0]
                name = product[1]
                category = product[2]
                brand = product[3]
                price = product[4]
                quantity = product[5]
                color = product[6]
                image_base64 = product[7]
                warehouse = product[8]

                app = Card_generate(id_product, name, price, image_from_base64(image_base64), category, quantity, page,
                                    brand)
                product_card.append(app)
        else:
            pass

        manufacture = self.get_all_manufacturers()
        manufacturer_cards = []
        if manufacture:
            for manufacturer in manufacture:
                id_manufacturer = manufacturer[0]
                image = manufacturer[2]

                card_builder = Manufactures_Card(id_manufacturer, image, page)
                manufacturer_cards.append(card_builder.container)
        else:
            pass

        rows = []  # Массив строк
        for i in range(0, len(manufacturer_cards), 2):
            if i + 1 < len(manufacturer_cards):
                # Если есть две карточки для строки
                row = ft.Row(
                    controls=[
                        manufacturer_cards[i],
                        manufacturer_cards[i + 1]
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20,
                )
            else:
                # Если последняя карточка без пары
                row = ft.Row(
                    controls=[manufacturer_cards[i]],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20,
                )
            rows.append(row)

        buttons_row = ft.Row(
            controls=buttons,
            spacing=20,
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

        product_row = ft.Row(
            controls=[card.card2 for card in product_card],
            spacing=20,
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

        Menu_content = ft.Row(
            controls=[
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Container(
                                content=ft.Text("Категории", size=update_size()["Menu_zag_text_size"],
                                                color=update_colors()["text_color"]),
                                padding=ft.padding.only(top=10, left=10),
                            ),
                            ft.Divider(height=2, color=update_colors()["text_color"]),
                            ft.Container(
                                content=ft.TextButton(
                                    content=ft.Text("Струнные", size=update_size()["Menu_other_text_size"],
                                                    color=update_colors()["text_color"]),
                                    on_click=lambda e: next_page("/category/Струнные")),
                                padding=ft.padding.only(left=10),
                            ),
                            ft.Container(
                                content=ft.TextButton(
                                    content=ft.Text("Духовые", size=update_size()["Menu_other_text_size"],
                                                    color=update_colors()["text_color"]),
                                    on_click=lambda e: next_page("/category/Духовые")),
                                padding=ft.padding.only(left=10),
                            ),
                            ft.Container(
                                content=ft.TextButton(
                                    content=ft.Text("Ударные", size=update_size()["Menu_other_text_size"],
                                                    color=update_colors()["text_color"]),
                                    on_click=lambda e: next_page('/category/Ударные')),
                                padding=ft.padding.only(left=10),
                            ),
                            ft.Container(
                                content=ft.TextButton(
                                    content=ft.Text("Клавишные", size=update_size()["Menu_other_text_size"],
                                                    color=update_colors()["text_color"]),
                                    on_click=lambda e: next_page('/category/Клавишные')),
                                padding=ft.padding.only(left=10),
                            ),
                            ft.Container(
                                content=ft.TextButton(
                                    content=ft.Text("Электро инструменты", size=update_size()["Menu_other_text_size"],
                                                    color=update_colors()["text_color"]),
                                    on_click=lambda e: next_page('/category/Электроинструменты')),
                                padding=ft.padding.only(left=10),
                            ),
                            ft.Container(
                                content=ft.TextButton(
                                    content=ft.Text("Аксессуары", size=update_size()["Menu_other_text_size"],
                                                    color=update_colors()["text_color"]),
                                    on_click=lambda e: next_page('/category/Аксессуары')),
                                padding=ft.padding.only(left=10),
                            ),
                            ft.Container(
                                content=ft.TextButton(
                                    content=ft.Text("Производители", size=update_size()["Menu_other_text_size"],
                                                    color=update_colors()["text_color"]),
                                    on_click=lambda e: next_page('/Производители')),
                                padding=ft.padding.only(left=10),
                            ),
                            ft.Divider(height=2, color=update_colors()["text_color"]),
                            ft.Container(
                                content=ft.TextButton(
                                    content=ft.Text("Главная", size=update_size()["Menu_zag_text_size"],
                                                    color=update_colors()["text_color"]),
                                    on_click=lambda e: next_page('/')),
                                padding=ft.padding.only(left=10),
                            ),
                            ft.Container(
                                content=ft.TextButton(
                                    content=ft.Text("Лента товаров", size=update_size()["Menu_zag_text_size"],
                                                    color=update_colors()["text_color"]),
                                    on_click=lambda e: next_page('/productsfeed')),
                                padding=ft.padding.only(left=10),
                            ),

                        ],
                        # scroll=ft.ScrollMode.ALWAYS
                    ),
                    expand=1,
                    border_radius=15,
                    alignment=ft.Alignment(-1, 1),
                    border=ft.border.all(width=2, color=update_colors()["border_color"]),
                    bgcolor=update_colors()["bgcolor"],
                ),
                ft.Container(
                    ft.Container(
                        on_click=animate_menu,
                    ),
                    expand=5
                ),
            ],
            expand=True,
            width=page.width,
            height=page.height - 15,
            offset=ft.transform.Offset(-2, 0),
            animate_offset=ft.animation.Animation(300),
        )

        Menu_but = ft.IconButton(icon=ft.icons.MENU,
                                 icon_color=update_colors()["icon_color"],
                                 icon_size=update_size()["icon_rectangle_size"],
                                 on_click=animate_menu, )
        # Верхний прямоугольник
        icon_but = ft.IconButton(icon=ft.icons.SUNNY, on_click=style_revert, icon_color=update_colors()["icon_color"],
                                 icon_size=update_size()['icon_rectangle_size'])
        Cart_button = ft.IconButton(icon=ft.icons.SHOPPING_CART, icon_color=update_colors()["icon_color"],
                                    icon_size=update_size()['icon_rectangle_size'])
        Profile_button = ft.IconButton(icon=ft.icons.PERSON, icon_color=update_colors()["icon_color"],
                                       icon_size=update_size()['icon_rectangle_size'], on_click=profile_muve)
        """Menu content"""
        name_shop = ft.Text(
            "Music Store",
            size=70,
            weight=ft.FontWeight.BOLD,
            color=update_colors()["text_color"],
        )

        search_button = ft.IconButton(
            icon=ft.icons.SEARCH,
            icon_size=20,
            icon_color=update_colors()["icon_color"],
            on_click=simple_search
        )

        search_field = ft.TextField(
            hint_text="Поиск",
            height=40,
            width=700,
            border_radius=15,
            bgcolor=update_colors()["bgcolor"],
            border_color=update_colors()["border_color"],
            color=update_colors()["text_color"],
            text_style=ft.TextStyle(size=16),
            suffix=search_button,
        )

        """Полоска разделитель"""
        divider = ft.Divider(height=update_size()["divider_size"], color=update_colors()["border_color"])

        top_rectangle = ft.Container(
            content=ft.Row(
                [
                    Menu_but,
                    ft.Row(
                        [icon_but, Cart_button, Profile_button],
                        alignment=ft.MainAxisAlignment.END,
                        spacing=10,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
        )
        title_catigories = ft.Text("Популярные категории", color=update_colors()["text_color"],
                                   size=update_size()["Title_size"])
        title_total_products = ft.Text("Популярные товары", color=update_colors()["text_color"],
                                       size=update_size()["Title_size"])
        title_manufacture = ft.Text("Производители", color=update_colors()["text_color"],
                                    size=update_size()["Title_size"])
        icon_back = ft.Container(content=update_images(), expand=True)
        """Популярные категории и товары"""
        show_conteiner = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(controls=[
                        ft.Container(
                            content=ft.Container(
                                content=ft.Column(
                                    controls=[
                                        title_catigories,
                                        ft.Divider(height=2, color=update_colors()['text_color']),
                                        ft.Row(
                                            controls=[ft.Container(content=buttons_row, height=215,
                                                                   alignment=ft.Alignment(0, -1))],
                                            scroll=ft.ScrollMode.AUTO,
                                        ),
                                    ],
                                    expand=True,
                                ),
                                padding=ft.padding.only(left=10, right=10, top=10, bottom=10),
                            ),
                            border=ft.border.all(width=2, color=update_colors()["border_color"]),
                            bgcolor=update_colors()["bgcolor"],
                            border_radius=10,
                            alignment=ft.Alignment(0, 0),
                            height=310,
                            width=page.width - 300,
                        ),
                    ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row([
                        ft.Container(
                            content=ft.Container(
                                content=ft.Column(
                                    controls=[
                                        title_total_products,
                                        ft.Divider(height=2, color=ft.colors.BLUE),
                                        ft.Row(
                                            controls=[ft.Container(content=product_row, height=380,
                                                                   alignment=ft.Alignment(0, -1))],
                                            scroll=ft.ScrollMode.ALWAYS,
                                        ),
                                    ],
                                    expand=True,
                                ),
                                padding=ft.padding.only(left=10, right=10, top=10, bottom=10),
                            ),
                            border=ft.border.all(width=2, color=update_colors()["border_color"]),
                            border_radius=10,
                            alignment=ft.Alignment(0, 0),
                            height=470,
                            width=page.width - 300,
                            bgcolor=update_colors()["bgcolor"],
                        ),
                    ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Container(content=title_manufacture, alignment=Alignment(0, 0), expand=True),
                    ft.Divider(height=2, color=update_colors()["border_color"]),
                    ft.Container(
                        content=ft.Column(
                            controls=rows,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        alignment=ft.Alignment(0, 0),
                        expand=True,
                    )
                ],
                spacing=10,
                scroll=ft.ScrollMode.ALWAYS,
            ),
            width=page.width,
            height=page.height / 1.42,
            # padding=ft.padding.only(bottom=10),
            # border=ft.border.all(width=2, color='white'),
        )

        """Популярные товары"""

        content = ft.Stack(
            [
                ft.Column(
                    [
                        top_rectangle,
                        ft.Container(content=name_shop, alignment=ft.Alignment(0, 0), padding=ft.padding.only(top=20)),
                        ft.Row(
                            [search_field],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Container(content=divider, alignment=ft.Alignment(0, 0), padding=ft.padding.only(top=20)),
                        ft.Stack(
                            [
                                icon_back,
                                show_conteiner,
                            ]
                        ),
                    ],
                    spacing=10,
                    expand=True,
                ),
                Menu_content
            ]
        )

        return ft.View("/", controls=[content])

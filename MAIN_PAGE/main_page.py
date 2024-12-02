
import flet as ft
from functools import lru_cache
import requests
import io
import base64


class Main_page:
    def __init__(self):
        self.instruments_light = [
            self.get_image(r"drum_light", "LIGHT", "png"),
            self.get_image(r"electro_light", "LIGHT", "png"),
            self.get_image(r"fleit_light", "LIGHT", "png"),
            self.get_image(r"guitar_light", "LIGHT", "png"),
            self.get_image(r"piano_light", "LIGHT", "png"),
            self.get_image(r"pick_light", "LIGHT", "png"),
        ]
        self.instruments_dark = [
            self.get_image(r"drum_dark", "DARK", "png"),
            self.get_image(r"electro_dark", "DARK", "png"),
            self.get_image(r"fleit_dark", "DARK", "png"),
            self.get_image(r"guitar_dark", "DARK", "png"),
            self.get_image(r"piano_dark", "DARK", "png"),
            self.get_image(r"pick_dark", "DARK", "png"),
        ]

    @lru_cache
    def get_image(self, name, style, val):
        request = requests.get(f"http://127.0.0.1:8000/images/{style}/{name}.{val}")
        image = io.BytesIO(request.content)
        base_64_image = base64.b64encode(image.read()).decode()
        return base_64_image

    def view(self, page: ft.Page, params=None, basket=None):
        page.theme_mode = ft.ThemeMode.LIGHT  # Устанавливаем начальный стиль

        # Функция для обновления цветов
        def update_colors():
            if page.theme_mode == ft.ThemeMode.LIGHT:
                return {
                    "bgcolor": ft.colors.WHITE,
                    "border_color": ft.colors.BLACK,
                    "icon_color": ft.colors.BLACK,
                    "text_color": ft.colors.BLACK,
                }
            else:
                return {
                    "bgcolor": ft.colors.BLACK,
                    "border_color": ft.colors.BLUE,
                    "icon_color": ft.colors.BLUE,
                    "text_color": ft.colors.BLUE,
                }

        def update_size():
            return {
                "icon_rectangle_size": 20,
                "divider_size": 5,
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
            #top_rectangle.bgcolor = colors["bgcolor"]
            #top_rectangle.border = ft.border.all(1, colors["border_color"])
            name_shop.color = colors["text_color"]
            search_field.bgcolor = colors["bgcolor"]
            search_field.border_color = colors["border_color"]
            search_field.color = colors["text_color"]
            search_button.icon_color = colors["icon_color"]
            divider.color = colors["border_color"]

            # Обновление иконок в top_rectangle
            Menu_button.icon_color = colors["icon_color"]
            Favorite_button.icon_color = colors["icon_color"]
            Cart_button.icon_color = colors["icon_color"]
            Profile_button.icon_color = colors["icon_color"]

            # Обновление фона с изображениями
            icon_back.content = update_images()
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

        # Верхний прямоугольник
        icon_but = ft.IconButton(icon=ft.icons.SUNNY, on_click=style_revert, icon_color=update_colors()["icon_color"], icon_size=update_size()['icon_rectangle_size'])
        Menu_button = ft.IconButton(icon=ft.icons.MENU, icon_color=update_colors()["icon_color"], icon_size=update_size()['icon_rectangle_size'])
        Favorite_button = ft.IconButton(icon=ft.icons.FAVORITE, icon_color=update_colors()["icon_color"], icon_size=update_size()['icon_rectangle_size'])
        Cart_button = ft.IconButton(icon=ft.icons.SHOPPING_CART, icon_color=update_colors()["icon_color"], icon_size=update_size()['icon_rectangle_size'])
        Profile_button = ft.IconButton(icon=ft.icons.PERSON, icon_color=update_colors()["icon_color"], icon_size=update_size()['icon_rectangle_size'])

        top_rectangle = ft.Container(
            content=ft.Row(
                [
                    Menu_button,
                    #ft.Container(content=icon_but, alignment=ft.Alignment(0.06, 0), expand=True),
                    ft.Row(
                        [icon_but, Favorite_button, Cart_button, Profile_button],
                        alignment=ft.MainAxisAlignment.END,
                        spacing=10,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            #height=32,
            #border_radius=15,
            # bgcolor=update_colors()["bgcolor"],
            # border=ft.border.all(1, update_colors()["border_color"]),
        )

        # Название магазина
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


        divider = ft.Divider(height=update_size()["divider_size"], color=update_colors()["border_color"])


        # Основной контейнер
        icon_back = ft.Container(content=update_images(), expand=True)

        content = ft.Column(
                    [
                        top_rectangle,
                        ft.Container(content=name_shop, alignment=ft.Alignment(0, 0), padding=ft.padding.only(top=50)),
                        ft.Row(
                            [search_field],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Container(content=divider, alignment=ft.Alignment(0,0), padding=ft.padding.only(top=20)),
                        ft.Stack(
                            [
                                icon_back,
                            ]
                        )

                    ],
                    spacing=10,
                    expand=True,
                )

        return ft.View("/", controls=[content])

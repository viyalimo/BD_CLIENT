import flet as ft
from flet_route import Params, Basket
import base64
import io
import requests
from functools import lru_cache


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

    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.theme_mode = ft.ThemeMode.LIGHT  # Устанавливаем начальный стиль

        def update_colors():
            if page.theme_mode == ft.ThemeMode.LIGHT:
                return {
                    "bgcolor": ft.colors.WHITE,
                    "border_color": ft.colors.BLACK,
                    "icon_color": ft.colors.BLACK,
                }
            else:
                return {
                    "bgcolor": ft.colors.BLACK,
                    "border_color": ft.colors.BLUE,
                    "icon_color": ft.colors.BLUE,
                }

        # Функция для обновления иконок
        def update_images():
            controls = []
            instruments = self.instruments_dark if page.theme_mode == ft.ThemeMode.DARK else self.instruments_light
            rows = 20
            cols = 50

            for row in range(rows):
                row_controls = []
                for col in range(cols):
                    if (row + col) % 2 == 0:  # Чередуем размещение иконок
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

        # Контейнер для иконок
        icon_back = ft.Container(
            content=update_images(),
            expand=True,
        )

        def style_revert(e):
            if page.theme_mode == ft.ThemeMode.DARK:
                page.theme_mode = ft.ThemeMode.LIGHT
                icon_but.icon = ft.icons.DARK_MODE_OUTLINED
            else:
                page.theme_mode = ft.ThemeMode.DARK
                icon_but.icon = ft.icons.SUNNY

            # Обновляем цвета
            colors = update_colors()
            top_rectangle.bgcolor = colors["bgcolor"]
            top_rectangle.border = ft.border.all(1, colors["border_color"])

            # Обновляем цвета иконок
            Menu_button.icon_color = colors["icon_color"]
            Favorite_button.icon_color = colors["icon_color"]
            Cart_button.icon_color = colors["icon_color"]
            Profile_button.icon_color = colors["icon_color"]

            icon_back.content = update_images()
            page.update()

        # Кнопка смены стиля
        icon_but = ft.IconButton(icon=ft.icons.SUNNY, on_click=style_revert)

        Menu_button = ft.IconButton(icon=ft.icons.MENU, icon_color=update_colors()["icon_color"])
        Favorite_button = ft.IconButton(icon=ft.icons.FAVORITE, icon_color=update_colors()["icon_color"])
        Cart_button = ft.IconButton(icon=ft.icons.SHOPPING_CART, icon_color=update_colors()["icon_color"])
        Profile_button = ft.IconButton(icon=ft.icons.PERSON_2, icon_color=update_colors()["icon_color"])

        # Прямоугольник сверху
        top_rectangle = ft.Container(
            content=ft.Row(
                [
                    # Левый блок с кнопкой меню
                    Menu_button,
                    # Центральная иконка смены темы
                    ft.Container(
                        content=icon_but,
                        alignment=ft.Alignment(0, 0),
                        expand=True,  # Центрирование
                    ),
                    # Правый блок с остальными иконками
                    ft.Row(
                        [
                            Favorite_button,
                            Cart_button,
                            Profile_button,
                        ],
                        alignment=ft.MainAxisAlignment.END,
                        spacing=10,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            height=40,
            border_radius=15,
            bgcolor=update_colors()["bgcolor"],  # Фон в зависимости от темы
            border=ft.border.all(1, update_colors()["border_color"]),  # Граница в зависимости от темы
        )

        # Основное содержимое
        content = ft.Stack(
            [
                icon_back,  # Фоновые иконки
                top_rectangle,  # Прямоугольник сверху
            ],
            expand=True,
        )

        return ft.View("/", controls=[content])



# class Main_page:
#     def __init__(self):
#         self.back_ground_img = "Задний фон\\задний фон.jpg"
#         self.image_paths = [
#             self.get_image("1Струнные", "MAIN"),
#             self.get_image("2Духовые", "MAIN"),
#             self.get_image("3Ударные", "MAIN"),
#             self.get_image("4Клавишные", "MAIN"),
#             self.get_image("5Электро", "MAIN"),
#             self.get_image("6Аксесуары", "MAIN"),
#         ]
#         print(self.image_paths)
#         self.button_names = [
#             "Струнные",
#             "Духовые",
#             "Ударные",
#             "Клавишные",
#             "    Электро \n инструменты",
#             "Аксессуары",
#             "Производители",
#         ]
#
#     # @lru_cache
#     def get_image(self, name, style):
#         request = requests.get(
#             f"http://127.0.0.1:8000/images/{style}/{name}.jpg")
#         image = io.BytesIO(request.content)
#         base_64_image = base64.b64encode(image.read()).decode()
#         return base_64_image
#
#
#     def view(self, page: ft.Page, params: Params, basket: Basket):
#         def button_clicked(e):
#             pass
#
#         """Назвние магазина"""
#         page.controls.clear()
#         page.title = "Music Store"
#         page.bgcolor = ft.colors.LIGHT_BLUE_50
#         title = ft.Text("Music Store", size=30, weight=ft.FontWeight.BOLD, color=ft.colors.PURPLE)
#
#         """Кнопка для профиля"""
#         page.title = "Text button with 'click' event"
#         # icon_profile = ft.Icon(ft.icons.PROFILE)
#         profile = ft.TextButton("Профиль", on_click=button_clicked)
#
#         """Поисковая строка"""
#         search_bar = ft.TextField(label="Поиск", width=300, height=30, text_size=10, text_align=ft.TextAlign.LEFT)
#         search_btn = ft.IconButton(ft.icons.SEARCH, icon_size=25)
#
#         """Виджеты с названием инструментов"""
#         page.theme_mode = ft.ThemeMode.LIGHT
#         page.padding = 10
#         page.update()
#
#         # Список с названиями кнопок
#
#
#         buttons = []
#         # Создаем кнопки с названиями из списка
#         for i in range(len(self.button_names)):
#             # Если для кнопки есть изображение, то используем его, иначе задаём чёрный фон
#             if i < len(self.image_paths):
#                 print(self.image_paths[i])
#                 button = ft.Container(
#                     content=ft.Text(
#                         self.button_names[i],  # Название кнопки из списка
#                         size=20,
#                         weight=ft.FontWeight.BOLD,
#                         color=ft.colors.WHITE,
#                         text_align=ft.TextAlign.CENTER,
#                     ),
#                     width=200,
#                     height=200,
#                     alignment=ft.alignment.center,
#                     border_radius=ft.border_radius.all(10),
#                     on_click=lambda e, index=i + 1: print(f"{self.button_names[i]} нажата!"),
#                     # Используем название кнопки в событии
#                     ink=True,  # Плавный эффект при клике
#                     image_src_base64=self.image_paths[i],  # Задаем уникальное изображение для каждой кнопки,
#                     image_fit = ft.ImageFit.COVER
#                 )
#             else:
#                 button = ft.Container(
#                     content=ft.Text(
#                         self.button_names[i],  # Название кнопки из списка
#                         size=20,
#                         weight=ft.FontWeight.BOLD,
#                         color=ft.colors.WHITE,
#                         text_align=ft.TextAlign.CENTER,
#                     ),
#                     width=200,
#                     height=200,
#                     alignment=ft.alignment.center,
#                     border_radius=ft.border_radius.all(10),
#                     ink=True,  # Плавный эффект при клике
#                     bgcolor=ft.colors.BLACK  # Задаем чёрный фон, если изображения закончились
#                 )
#             buttons.append(button)
#
#         # Горизонтальный ряд кнопок с прокруткой
#         buttons_row = ft.Row(
#             controls=buttons,
#             spacing=20,
#             alignment=ft.MainAxisAlignment.START,
#             vertical_alignment=ft.CrossAxisAlignment.CENTER,
#             scroll="auto",  # Включить прокрутку
#
#         )
#
#
#         """Боковая панель"""
#         drawer = ft.NavigationDrawer(
#             # on_dismiss=handle_dismissal,
#             # on_change=handle_change,
#             controls=[
#                 ft.Container(height=12),
#                 ft.NavigationDrawerDestination(
#                     label="Item 1",
#                     icon=ft.icons.DOOR_BACK_DOOR_OUTLINED,
#                     selected_icon_content=ft.Icon(ft.icons.DOOR_BACK_DOOR),
#                 ),
#                 ft.Divider(thickness=2),
#                 ft.NavigationDrawerDestination(
#                     icon_content=ft.Icon(ft.icons.MAIL_OUTLINED),
#                     label="Item 2",
#                     selected_icon=ft.icons.MAIL,
#                 ),
#                 ft.NavigationDrawerDestination(
#                     icon_content=ft.Icon(ft.icons.PHONE_OUTLINED),
#                     label="Item 3",
#                     selected_icon=ft.icons.PHONE,
#                 ),
#             ],
#         )
#         home_button = ft.IconButton(ft.icons.MENU, on_click=lambda e: page.open(drawer))
#         """Размещение на экране"""
#
#         content = ft.Column([
#             ft.Row([
#                 ft.Container(
#                     home_button,
#                     alignment=ft.Alignment(-1, -1)
#                 ),
#                 ft.Container(
#                     profile,
#                     alignment=ft.Alignment(1, -1)
#                 )
#             ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
#             ),
#             # название магазина
#             ft.Row([
#                 title,
#             ], alignment=ft.MainAxisAlignment.CENTER,
#             ),
#             # поисковая строка и кнопка поиска
#             ft.Row([
#                 ft.Container(
#                     content=search_bar,
#                     alignment=ft.Alignment(0, 0)
#                 ),
#                 ft.Container(
#                     search_btn,
#                     alignment=ft.Alignment(1, -10)
#                 ),
#                 ], alignment=ft.MainAxisAlignment.CENTER
#             ),
#             # полоска разделитель
#             ft.Divider(color='black'),
#             # кнопки с категориями
#
#             ft.Row([
#             ft.Container(
#                 content=buttons_row,
#                 expand=True,
#                 alignment=ft.Alignment(0, 0)  # Центрируем контейнер
#             )
#             ])
#         ],
#         expand=True,
#         )
#
#         return ft.View("/main", controls=[content])

import flet as ft


class Main_page:
    def __init__(self, page):
        self.page = page
        self.back_ground_img = "C:\\Users\\user1387\\PycharmProjects\\BD_client\\Image\\Задний фон\\задний фон.jpg"
        self.image_paths = [
            "C:\\Users\\user1387\\PycharmProjects\\BD_client\\Image\\image_main_page\\1Струнные.jpg",
            "C:\\Users\\user1387\\PycharmProjects\\BD_client\\Image\\image_main_page\\2Духовые 2.jpg",
            "C:\\Users\\user1387\\PycharmProjects\\BD_client\\Image\\image_main_page\\3Ударные.jpg",
            "C:\\Users\\user1387\\PycharmProjects\\BD_client\\Image\\image_main_page\\4Клавишные.jpg",
            "C:\\Users\\user1387\\PycharmProjects\\BD_client\\Image\\image_main_page\\5Электро.jpg",
            "C:\\Users\\user1387\\PycharmProjects\\BD_client\\Image\\image_main_page\\6Аксесуары.jpg",
        ]
        self.button_names = [
            "Струнные",
            "Духовые",
            "Ударные",
            "Клавишные",
            "    Электро \n инструменты",
            "Аксессуары",
            "Производители",
        ]
        self.welcome_page()

    def welcome_page(self):
        """Функции для кнопок"""

        def button_clicked(e):
            pass

        """Назвние магазина"""
        self.page.controls.clear()
        self.page.title = "Music Store"
        self.page.bgcolor = ft.colors.LIGHT_BLUE_50
        title = ft.Text("Music Store", size=30, weight=ft.FontWeight.BOLD, color=ft.colors.PURPLE)

        """Кнопка для профиля"""
        self.page.title = "Text button with 'click' event"
        # icon_profile = ft.Icon(ft.icons.PROFILE)
        profile = ft.TextButton("Профиль", on_click=button_clicked)

        """Поисковая строка"""
        search_bar = ft.TextField(label="Поиск", width=300, height=30, text_size=10, text_align=ft.TextAlign.LEFT)
        search_btn = ft.IconButton(ft.icons.SEARCH, icon_size=25)

        """Виджеты с названием инструментов"""
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.padding = 10
        self.page.update()

        # Список с названиями кнопок


        buttons = []
        # Создаем кнопки с названиями из списка
        for i in range(len(self.button_names)):
            # Если для кнопки есть изображение, то используем его, иначе задаём чёрный фон
            if i < len(self.image_paths):
                button = ft.Container(
                    content=ft.Text(
                        self.button_names[i],  # Название кнопки из списка
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.WHITE,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    width=200,
                    height=200,
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(10),
                    on_click=lambda e, index=i + 1: print(f"{self.button_names[i]} нажата!"),
                    # Используем название кнопки в событии
                    ink=True,  # Плавный эффект при клике
                    image_src=self.image_paths[i]  # Задаем уникальное изображение для каждой кнопки
                )
            else:
                button = ft.Container(
                    content=ft.Text(
                        self.button_names[i],  # Название кнопки из списка
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.WHITE,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    width=200,
                    height=200,
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(10),
                    on_click=lambda e, index=i + 1: print(f"{self.button_names[i]} нажата!"),
                    ink=True,  # Плавный эффект при клике
                    bgcolor=ft.colors.BLACK  # Задаем чёрный фон, если изображения закончились
                )
            buttons.append(button)

        # Горизонтальный ряд кнопок с прокруткой
        buttons_row = ft.Row(
            controls=buttons,
            spacing=20,
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            scroll="auto",  # Включить прокрутку

        )


        """Боковая панель"""
        drawer = ft.NavigationDrawer(
            # on_dismiss=handle_dismissal,
            # on_change=handle_change,
            controls=[
                ft.Container(height=12),
                ft.NavigationDrawerDestination(
                    label="Item 1",
                    icon=ft.icons.DOOR_BACK_DOOR_OUTLINED,
                    selected_icon_content=ft.Icon(ft.icons.DOOR_BACK_DOOR),
                ),
                ft.Divider(thickness=2),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.MAIL_OUTLINED),
                    label="Item 2",
                    selected_icon=ft.icons.MAIL,
                ),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.PHONE_OUTLINED),
                    label="Item 3",
                    selected_icon=ft.icons.PHONE,
                ),
            ],
        )
        home_button = ft.IconButton(ft.icons.MENU, on_click=lambda e: self.page.open(drawer))
        """Размещение на экране"""
        self.page.add(
            ft.Row([
                ft.Container(
                    home_button,
                    alignment=ft.Alignment(-1, -1)
                ),
                ft.Container(
                    profile,
                    alignment=ft.Alignment(1, -1)
                )
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            # название магазина
            ft.Row([
                title,
            ], alignment=ft.MainAxisAlignment.CENTER,
            ),
            # поисковая строка и кнопка поиска
            ft.Row([
                ft.Container(
                    content=search_bar,
                    alignment=ft.Alignment(0, 0)
                ),
                ft.Container(
                    search_btn,
                    alignment=ft.Alignment(1, -10)
                ),
                ], alignment=ft.MainAxisAlignment.CENTER
            ),
            # полоска разделитель
            ft.Divider(color='black'),
            # кнопки с категориями

            ft.Row([
            ft.Container(
                content=buttons_row,
                expand=True,
                alignment=ft.Alignment(0, 0)  # Центрируем контейнер
            )
            ])
        )

def main(page):
    main_pg = Main_page(page)


if __name__ == "__main__":
    ft.app(target=main)
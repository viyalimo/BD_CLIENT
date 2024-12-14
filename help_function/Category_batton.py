from flet import *


class Category_batton:
    def __init__(self):
        self.color = Colors("black")


    def build_card(self, name, move: str, page: Page,photo=None):
        def next_page(muve):
            page.theme_mode = ThemeMode.DARK
            page.client_storage.set("muve", muve)
            page.go("/loading")

        if not photo:
            button = Container(
                content=Text(
                    name,  # Название кнопки из списка
                    size=20,
                    weight=FontWeight.BOLD,
                    color=colors.WHITE,
                    text_align=TextAlign.CENTER,
                ),
                width=300,
                height=200,
                alignment=alignment.center,
                border_radius=border_radius.all(10),
                on_click=lambda e: page.go(move),
                ink=True,  # Плавный эффект при клике
                bgcolor=self.color  # Задаем чёрный фон, если изображения закончились
            )
        else:
            button = Container(
                content=Text(
                    name,  # Название кнопки из списка
                    size=20,
                    weight=FontWeight.BOLD,
                    color=colors.WHITE,
                    text_align=TextAlign.CENTER,
                ),
                width=300,
                height=200,
                alignment=alignment.center,
                border_radius=border_radius.all(10),
                on_click=lambda e: next_page(move),
                ink=True,  # Плавный эффект при клике
                image_src_base64=photo,
                image_fit=ImageFit.COVER,
            )
        return button

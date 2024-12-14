import flet as ft
from flet_core import ThemeMode
from help_function.animated_box import SendData
from help_function.Navigation import Navigation


class ImageApp(Navigation):
    def __init__(self):
        # Загружаем изображения
        self.instruments_light = [
            self.get_image("drum_light", "png", "LIGHT"),
            self.get_image("electro_light", "png", "LIGHT"),
            self.get_image("fleit_light", "png", "LIGHT"),
            self.get_image("guitar_light", "png", "LIGHT"),
            self.get_image("piano_light", "png", "LIGHT"),
            self.get_image("pick_light", "png", "LIGHT"),
        ]
        self.instruments_dark = [
            self.get_image(r"drum_dark", "png", "DARK"),
            self.get_image(r"electro_dark", "png", "DARK"),
            self.get_image(r"fleit_dark", "png", "DARK"),
            self.get_image(r"guitar_dark", "png", "DARK"),
            self.get_image(r"piano_dark", "png", "DARK"),
            self.get_image(r"pick_dark", "png", "DARK"),
        ]
        self.current_index = 0
        super().__init__()

    def view(self, page: ft.Page, params=None, basket=None):
        page.theme_mode = ThemeMode.DARK
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
        instruments = self.instruments_dark if page.theme_mode == ThemeMode.DARK else self.instruments_light
        page.title = "Анимационная смена изображений с вращением"
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        muve = page.client_storage.get("muve")

        # Контейнер для изображения с анимацией вращения
        image_container = SendData(STILE_MODE="dark", PTH=muve,
                                      content=ft.Image(
                                          src=instruments[self.current_index],
                                          width=300,
                                          height=200,
                                      ),
                                      alignment=ft.alignment.center,
                                      rotate=ft.transform.Rotate(0, alignment=ft.alignment.center),
                                      animate_rotation=ft.animation.Animation(700, ft.AnimationCurve.BOUNCE_OUT))

        # Главный контейнер, растянутый на всю страницу
        main_container = ft.Container(
            content=image_container,
            alignment=ft.alignment.center,
            expand=True,
        )
        return ft.View("/loading/:muve", controls=[main_container])

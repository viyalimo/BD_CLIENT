import flet as ft
import requests
from flet_core.types import AppView


class Card_generate:
    def __init__(self, id_product: int, name: str, price: float, image: ft.Image, cutigories: str, total_buy: int, page: ft.Page, brand):
        # print("generate", id_product, name, price, image, cutigories, total_buy, page, brand)
        self.id_product = id_product
        self.name = name
        self.price = price
        self.image = image
        self.cutigories = cutigories
        self.total_buy = total_buy
        self.brand = brand
        self.card1 = None
        self.container1 = None
        self.card2 = None
        self.page = page
        self.generate_card()

    def update_colors(self):
        if self.page.theme_mode == ft.ThemeMode.LIGHT:
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

    def AnimateCardFunction(self, e):
        # self.icon_container_.visible = False
        # self.icon_container_.update()

        if e.data == 'true':
            for __ in range(0):
                self.card1.elevation += 1
                self.card1.update()

            self.container1.border = ft.border.all(4, ft.colors.BLUE)
            self.container1.update()

            # self.icon_container_.offset = ft.transform.Offset(0, -0.75)
            # self.icon_container_.opacity = 1
            # self.icon_container_.update()

        else:
            for __ in range(0):
                self.card1.elevation -= 1
                self.card1.update()

            self.container1.border = ft.border.all(2, self.update_colors()['card_border_color'])
            self.container1.update()

            # self.icon_container_.offset = ft.transform.Offset(0, 0.5)
            # self.icon_container_.opacity = 0
            # self.icon_container_.update()

    def generate_card(self):

        def next_page(muve):
            self.page.client_storage.set("muve", muve)
            self.page.go("/loading")

        # self.icon_container_ = ft.Container(
        #     visible=False,
        #     width=120,
        #     height=35,
        #     bgcolor=self.update_colors()["icon_background_color"],
        #     border=ft.border.all(2, color=self.update_colors()["border_color"]),
        #     border_radius=25,
        #     animate_opacity=200,
        #     offset=ft.transform.Offset(0, 0.25),
        #     animate_offset=ft.animation.Animation(duration=900, curve=ft.AnimationCurve.EASE),
        #     content=ft.Row(
        #         controls=[
        #             ft.Text("Выбрать", size=12, weight=ft.FontWeight.BOLD, color=self.update_colors()["text_color"]),
        #         ],
        #         alignment=ft.MainAxisAlignment.CENTER,
        #         vertical_alignment=ft.CrossAxisAlignment.CENTER,
        #     )
        # )

        self.container1 = ft.Container(
            width=200,
            height=350,
            bgcolor=self.update_colors()['bgcolor'],
            border_radius=12,
            on_hover=lambda e: self.AnimateCardFunction(e),
            on_click=lambda e: next_page(f'/cardinfo/:{int(self.id_product)}'),
            animate=ft.animation.Animation(600, 'ease'),
            border=ft.border.all(2, self.update_colors()['card_border_color']),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
                controls=[
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Container(
                                    content=ft.Image(
                                        src=self.image.src,
                                        fit=ft.ImageFit.FIT_HEIGHT,  # Растягиваем изображение по высоте
                                        width=180,  # Задаем ширину изображения
                                        height=175,  # Задаем высоту изображения
                                        border_radius=15,
                                        expand=True
                                    ),
                                    height=175,
                                    width=180,
                                    border_radius=17,
                                    border=ft.border.all(2, self.update_colors()["border_color"]),
                                )
                            ],
                            expand=True,
                        ),
                        expand=True,
                        padding=ft.padding.only(top=10),
                    ),
                    ft.Divider(2, color=self.update_colors()['text_color']),
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Column(
                                    controls=[
                                        ft.Text(f"{self.price} ₽", size=20, color=self.update_colors()['text_color']),
                                        ft.Text(self.name[:15], size=20, color=self.update_colors()['text_color']),
                                        ft.Text(f"Категория: {self.cutigories}", size=12,
                                                color=self.update_colors()['text_color']),
                                        ft.Text(f"Бренд: {self.brand}", size=12,
                                                color=self.update_colors()['text_color']),
                                        ft.Text(f'Проданно: {self.total_buy}+', size=13,
                                                color=self.update_colors()['text_color']),

                                    ],
                                    alignment=ft.MainAxisAlignment.START,
                                    expand=True,

                                )
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            expand=True,
                        ),

                        bgcolor=self.update_colors()['bgcolor'],
                        padding=ft.padding.only(left=10),
                        # border=ft.border.all(1, color=update_colors()['border_color_info']),
                        border_radius=10,
                        on_hover=lambda e: self.AnimateCardFunction(e),
                        height=150
                    ),
                ]
            )
        )

        self.card1 = ft.Card(
            elevation=0,
            content=ft.Container(
                content=ft.Column(
                    spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        self.container1,
                    ],
                )
            ),
        )

        self.card2 = ft.Container(ft.Column(
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.card1,
                # self.icon_container_
            ]
        )
        )


from flet import *
import requests
from flet_core.types import AppView

from help_function.Navigation import Navigation


class Card_Cart(Navigation):
    def __init__(self, id_product: int, name: str, price: float, image: Image, cutigories: str, total_buy: int,
                 page: Page, brand):
        # print("generate", id, name, price, image, cutigories, total_buy, page, brand)
        self.id_product = int(id_product)
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
        super().__init__()

    def update_colors(self):
        if self.page.theme_mode == ThemeMode.LIGHT:
            return {
                "bgcolor": colors.WHITE,
                "border_color": colors.BLACK,
                "icon_color": colors.BLACK,
                "text_color": colors.BLACK,
                "tab_color": colors.BLACK,
                "border_color_info": colors.BLACK12,
                "card_background_color": colors.BLACK12,
                "icon_background_color": colors.WHITE,
                "card_border_color": colors.BLACK,

            }
        else:
            return {
                "bgcolor": colors.BLACK,
                "border_color": colors.BLUE,
                "icon_color": colors.BLUE,
                "text_color": colors.BLUE,
                "tab_color": colors.BLUE,
                "border_color_info": colors.BLACK,
                "card_background_color": colors.BLACK,
                "icon_background_color": colors.BLACK,
                "card_border_color": colors.WHITE24,
            }

    def AnimateCardFunction(self, e):
        if e.data == 'true':
            for __ in range(0):
                self.card1.elevation += 1
                self.card1.update()

            self.container1.border = border.all(4, colors.BLUE)
            self.container1.update()
        else:
            for __ in range(0):
                self.card1.elevation -= 1
                self.card1.update()

            self.container1.border = border.all(2, self.update_colors()['card_border_color'])
            self.container1.update()

    def generate_card(self):

        def hower_btn_buy(e):
            if e.data == 'true':
                self.buy_btn.bgcolor = Colors.GREEN
                self.buy_btn.border_color = Colors.GREEN
                self.buy_btn.content.controls[0].controls[0].color = Colors.WHITE
            else:
                self.buy_btn.bgcolor = self.update_colors()["bgcolor"]
                self.buy_btn.border_color = self.update_colors()["text_color"]
                self.buy_btn.content.controls[0].controls[0].color = self.update_colors()["text_color"]
            self.buy_btn.update()
            self.page.update()

        def hower_btn_basket(e):
            if e.data == 'true':
                self.basket_btn.bgcolor = Colors.RED
                self.basket_btn.border_color = Colors.RED
                self.basket_btn.content.controls[0].controls[0].color = Colors.WHITE
            else:
                self.basket_btn.bgcolor = self.update_colors()["bgcolor"]
                self.basket_btn.border_color = self.update_colors()["text_color"]
                self.basket_btn.content.controls[0].controls[0].color = self.update_colors()["text_color"]
            self.basket_btn.update()
            self.page.update()

        def on_click_buy(e):
            key, user_name = self.page.client_storage.get("key")
            user_id = int(self.get_user_info(user_name, key)[0])
            result = self.create_order(user_id, self.id_product)
            if result:
                self.page.snack_bar = SnackBar(
                    content=Row([Text("Заказ создан", color='white')],
                                alignment=MainAxisAlignment.CENTER),
                    bgcolor=colors.GREEN,

                )
                self.page.snack_bar.open = True
                self.page.update()
                next_page("/cart")
            else:
                self.page.snack_bar = SnackBar(
                    content=Row([Text("Ошибка при оплате заказа", color='white')],
                                alignment=MainAxisAlignment.CENTER),
                    bgcolor=colors.RED,

                )
                self.page.snack_bar.open = True
                self.page.update()

        def on_click_bascket(e):
            key, user_name = self.page.client_storage.get("key")
            user_id = int(self.get_user_info(user_name, key)[0])
            result = self.remove_from_cart(user_id, self.id_product)
            if result:
                self.page.snack_bar = SnackBar(
                    content=Row([Text("Товар удалён из карзины!", color='white')],
                                alignment=MainAxisAlignment.CENTER),
                    bgcolor=colors.GREEN,

                )
                self.page.snack_bar.open = True
                self.page.update()
                next_page("/cart")
            else:
                self.page.snack_bar = SnackBar(
                    content=Row([Text("Ошибка при удалении товара", color='white')],
                                alignment=MainAxisAlignment.CENTER),
                    bgcolor=colors.RED,

                )
                self.page.snack_bar.open = True
                self.page.update()



        def next_page(muve):
            self.page.client_storage.set("muve", muve)
            self.page.go("/loading")

        self.buy_btn = Container(
            content=Row(
                controls=[
                    Column(
                        controls=[
                            Icon(Icons.CREDIT_CARD, size=16, color=self.update_colors()["text_color"]),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    )
                ],
                alignment=MainAxisAlignment.CENTER,
                expand=True,
            ),
            border=border.all(width=2, color=self.update_colors()["border_color"]),
            alignment=Alignment(0, 0),
            bgcolor=self.update_colors()["bgcolor"],
            on_hover=hower_btn_buy,
            on_click=lambda e: on_click_buy(e),
            padding=padding.only(left=1),
            margin=margin.only(left=1, bottom=1),
            expand=True,
            width=146,
            height=30,
        )
        """basket"""
        self.basket_btn = Container(
            content=Row(
                controls=[
                    Column(
                        controls=[
                            Icon(Icons.DELETE, size=16, color=self.update_colors()["text_color"]),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    )
                ],
                alignment=MainAxisAlignment.CENTER,
                expand=True,
            ),
            border=border.all(width=2, color=self.update_colors()["border_color"]),
            alignment=Alignment(0, 0),
            bgcolor=self.update_colors()["bgcolor"],
            expand=True,
            on_hover=hower_btn_basket,
            on_click=lambda e: on_click_bascket(e),
            padding=padding.only(right=1),
            margin=margin.only(right=1, bottom=1),
            width=200,
            height=30,
        )
        self.container1 = Container(
            width=200,
            height=350,
            bgcolor=self.update_colors()['bgcolor'],
            border_radius=12,
            animate=animation.Animation(600, 'ease'),
            border=border.all(2, self.update_colors()['card_border_color']),
            content=Column(
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=0,
                controls=[
                    Container(
                        content=Column(
                            controls=[
                                Container(
                                    content=Image(
                                        src=self.image.src,
                                        fit=ImageFit.FIT_HEIGHT,  # Растягиваем изображение по высоте
                                        width=180,  # Задаем ширину изображения
                                        height=175,  # Задаем высоту изображения
                                        border_radius=15,
                                        expand=True
                                    ),
                                    height=175,
                                    width=180,
                                    border_radius=17,
                                    border=border.all(2, self.update_colors()["border_color"]),
                                )
                            ],
                            expand=True,
                        ),
                        expand=True,
                        padding=padding.only(top=10),
                        on_hover=lambda e: self.AnimateCardFunction(e),
                        on_click=lambda e: next_page(f'/cardinfo/:{int(self.id_product)}'),
                    ),
                    Divider(2, color=self.update_colors()['text_color']),
                    Container(
                        content=Row(
                            controls=[
                                Column(
                                    controls=[
                                        Text(self.name[:15], size=20, color=self.update_colors()['text_color']),
                                        Text(f"{self.price} ₽", size=15, color=self.update_colors()['text_color']),
                                        Text(f"Бренд: {self.brand}", size=12,
                                             color=self.update_colors()['text_color']),
                                        Text(f'Проданно: {self.total_buy}+', size=13,
                                             color=self.update_colors()['text_color']),
                                    ],
                                    alignment=MainAxisAlignment.START,
                                    expand=True,
                                ),

                            ],
                            alignment=MainAxisAlignment.START,
                            expand=True,
                        ),

                        bgcolor=self.update_colors()['bgcolor'],
                        padding=padding.only(left=10),
                        # border=border.all(1, color=update_colors()['border_color_info']),
                        border_radius=10,
                        on_hover=lambda e: self.AnimateCardFunction(e),
                        on_click=lambda e: next_page(f'/cardinfo/:{int(self.id_product)}'),
                        height=120
                    ),
                    Container(
                        content=Column(controls=[
                            Row(controls=[self.buy_btn, self.basket_btn],
                                alignment=MainAxisAlignment.CENTER,
                                spacing=0

                                )
                        ],
                            alignment=MainAxisAlignment.END,
                        ),
                        padding=padding.only(bottom=3),
                    )
                ]
            )
        )

        self.card1 = Card(
            elevation=0,
            content=Container(
                content=Column(
                    spacing=0,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        self.container1,
                    ],
                )
            ),
        )

        self.card2 = Container(Column(
            spacing=0,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                self.card1,
                # self.icon_container_
            ]
        )
        )

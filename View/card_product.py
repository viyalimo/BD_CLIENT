from flet import *
from flet_route import Params, Basket
from help_function.Navigation import Navigation
from help_function.Card_generate import Card_generate

class Card_product(Navigation):
    def __init__(self):
        self.id = None
        self.name = None
        self.category = None
        self.brand = None
        self.price = None
        self.quantity = None
        self.color = None
        self.image_base64 = None
        self.warehouse = None
        self.instruments_light = [
            self.get_image(r"drum_light", "png", "LIGHT"),
            self.get_image(r"electro_light", "png", "LIGHT"),
            self.get_image(r"fleit_light", "png", "LIGHT"),
            self.get_image(r"guitar_light", "png", "LIGHT"),
            self.get_image(r"piano_light", "png", "LIGHT"),
            self.get_image(r"pick_light", "png", "LIGHT"),
        ]
        self.instruments_dark = [
            self.get_image(r"drum_dark", "png", "DARK"),
            self.get_image(r"electro_dark", "png", "DARK"),
            self.get_image(r"fleit_dark", "png", "DARK"),
            self.get_image(r"guitar_dark", "png", "DARK"),
            self.get_image(r"piano_dark", "png", "DARK"),
            self.get_image(r"pick_dark", "png", "DARK"),
        ]
        super().__init__()


    def view(self, page: Page, params: Params, basket: Basket):
        page.theme_mode = ThemeMode.DARK
        self.id = int(params.get("id")[1:])
        self.name, self.category, self.brand, self.price, self.quantity, self.color, self.image_base64, self.warehouse = self.get_product_id(self.id)[1:]
        key, user_name = page.client_storage.get("key")
        self.user_id = int(self.get_user_info(user_name, key)[0])


        def next_page(muve):
            page.theme_mode = ThemeMode.DARK
            page.client_storage.set("muve", muve)
            page.go("/loading")

        def profile_muve(e):
            if page.client_storage.get("key") == None:
                next_page("/login")
            else:
                next_page("/profile")

        def cart_muve(e):
            if page.client_storage.get("key") == None:
                next_page("/login")
            else:
                next_page("/cart")

        def image_from_base64(base64_str: str):
            return Image(src=f"data:image/jpeg;base64,{base64_str}", width=800, height=800)

        def update_colors():
            if page.theme_mode == ThemeMode.LIGHT:
                return {
                    "bgcolor": Colors.WHITE,
                    "border_color": Colors.BLACK,
                    "icon_color": Colors.BLACK,
                    "text_color": Colors.BLACK,
                    "tab_color": Colors.BLACK,
                    "border_color_info": Colors.BLACK12,
                    "card_background_color": Colors.BLACK12,
                    "icon_background_color": Colors.WHITE,
                    "card_border_color": Colors.BLACK,

                }
            else:
                return {
                    "bgcolor": Colors.BLACK,
                    "border_color": Colors.BLUE,
                    "icon_color": Colors.BLUE,
                    "text_color": Colors.BLUE,
                    "tab_color": Colors.BLUE,
                    "border_color_info": Colors.BLACK,
                    "card_background_color": Colors.BLACK,
                    "icon_background_color": Colors.BLACK,
                    "card_border_color": Colors.WHITE24,
                }

        def update_size():
            return {
                "icon_rectangle_size": 20,
                "divider_size": 5,
                "Menu_zag_text_size": 20,
                "Menu_other_text_size": 18,
                "Title_size": 35,
            }

        def update_images():
            controls = []
            instruments = self.instruments_dark if page.theme_mode == ThemeMode.DARK else self.instruments_light
            rows, cols = 20, 50
            for row in range(rows):
                row_controls = []
                for col in range(cols):
                    if (row + col) % 2 == 0:
                        instrument_image = instruments[(row * cols + col) % len(instruments)]
                        row_controls.append(
                            Image(
                                src="data:image/png;base64," + instrument_image,
                                width=20,
                                height=20,
                                fit=ImageFit.CONTAIN,
                            )
                        )
                    else:
                        row_controls.append(Container(width=50, height=50))
                controls.append(Row(row_controls, alignment=MainAxisAlignment.CENTER))
            return Column(controls, alignment=MainAxisAlignment.CENTER)

        def animate_menu(e):
            Menu_content.offset = transform.Offset(0, 0) if Menu_content.offset == transform.Offset(-2,
                                                                                                    0) else transform.Offset(
                -2, 0)
            Menu_content.update()

        def hower_btn_buy(e):
            if e.data == 'true':
                buy_btn.bgcolor = Colors.RED
            else:
                buy_btn.bgcolor = update_colors()["bgcolor"]
            buy_btn.update()
            page.update()

        def hower_btn_basket(e):
            if e.data == 'true':
                basket_btn.bgcolor = Colors.RED
            else:
                basket_btn.bgcolor = update_colors()["bgcolor"]
            basket_btn.update()
            page.update()

        def on_click_bascet(e):
            result = self.add_to_cart(self.user_id, self.id)
            if result == True:
                page.snack_bar = SnackBar(
                    content=Row([Text("Товар добавлен в корзину", color='white')],
                                alignment=MainAxisAlignment.CENTER),
                    bgcolor=colors.GREEN,

                )
                page.snack_bar.open = True
                page.update()
            elif result == False:
                page.snack_bar = SnackBar(
                    content=Row([Text("Ошибка при добавлении товара в корзину!", color='white')],
                                alignment=MainAxisAlignment.CENTER),
                    bgcolor=colors.RED,

                )
                page.snack_bar.open = True
                page.update()
            else:
                page.snack_bar = SnackBar(
                    content=Row([Text("Товара пока нет вналичии(", color='white')],
                                alignment=MainAxisAlignment.CENTER),
                    bgcolor=colors.RED,

                )
                page.snack_bar.open = True
                page.update()

        def on_click_buy(e):
            result = self.create_direct_order(self.user_id, self.id)
            if result == True:
                page.snack_bar = SnackBar(
                    content=Row([Text("Заказ оформлен", color='white')],
                                alignment=MainAxisAlignment.CENTER),
                    bgcolor=colors.GREEN,

                )
                page.snack_bar.open = True
                page.update()
            elif result == False:
                page.snack_bar = SnackBar(
                    content=Row([Text("Ошибка при оформлении заказа!", color='white')],
                                alignment=MainAxisAlignment.CENTER),
                    bgcolor=colors.RED,

                )
                page.snack_bar.open = True
                page.update()
            else:
                page.snack_bar = SnackBar(
                    content=Row([Text("Товара пока нет вналичии(", color='white')],
                                alignment=MainAxisAlignment.CENTER),
                    bgcolor=colors.RED,

                )
                page.snack_bar.open = True
                page.update()

        def style_revert(e):
            if page.theme_mode == ThemeMode.DARK:
                page.theme_mode = ThemeMode.LIGHT
                icon_but.icon = Icons.DARK_MODE_OUTLINED
                icon_but.icon_color = Colors.BLACK
            else:
                page.theme_mode = ThemeMode.DARK
                icon_but.icon = Icons.SUNNY
                icon_but.icon_color = Colors.BLUE

            colors = update_colors()

            # Обновление иконок в top_rectangle
            Cart_button.icon_color = colors["icon_color"]
            Profile_button.icon_color = colors["icon_color"]
            buy_btn.bgcolor = colors["bgcolor"]
            buy_btn.content.controls[0].controls[0].color = colors["text_color"]


            basket_btn.bgcolor = colors["bgcolor"]
            basket_btn.content.controls[0].controls[0].color = colors["text_color"]

            price_value.color = update_colors()["text_color"]
            """Характеристики"""
            specifications.controls[0].content.controls[0].controls[0].content.controls[0].color = colors["text_color"]
            specifications.controls[0].content.controls[0].controls[1].color = colors["text_color"]
            specifications.controls[0].content.controls[0].controls[2].color = colors["text_color"]
            specifications.controls[0].content.controls[0].controls[3].color = colors["text_color"]
            specifications.controls[0].content.controls[0].controls[4].color = colors["text_color"]
            specifications.controls[0].content.controls[0].controls[5].color = colors["text_color"]
            specifications.controls[0].content.controls[0].controls[6].color = colors["text_color"]
            """Menu"""
            Menu_but.icon_color = colors["icon_color"]
            Image_Product.content.controls[0].border=border.all(2, color=colors["border_color"])
            specifications.controls[0].border = border.all(2, color=colors["border_color"])

            buy_btn.border = border.all(2, color=colors["border_color"])

            basket_btn.border = border.all(2, color=colors["border_color"])

            buy_window.border = border.all(2, color=colors["border_color"])

            # Menu_content.controls[0].content.border = border.all(2, color=colors["border_color"])
            Menu_content.controls[0].border = border.all(2, color=colors["border_color"])

            show_conteiner.content.controls[0].controls[0].border = border.all(2, color=colors["border_color"])


            Menu_content.controls[0].bgcolor = update_colors()['bgcolor']
            """Обновление цветов в меню"""
            Menu_content.controls[0].bgcolor = update_colors()['bgcolor']
            # Menu_content.controls[0].border = border.all(2, update_colors()['border_color'])
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
            Menu_content.controls[0].content.controls[12].content.content.color = update_colors()['text_color']



            icon_back.content = update_images()
            show_conteiner.content.controls[0].controls[0].content.content.controls[1].color = colors["text_color"]
            upper_part.content.controls[2].color = colors["text_color"]

            """Обновление карточек"""
            for card_app in product_card:
                updated_colors = card_app.update_colors()
                card_app.container1.bgcolor = updated_colors["bgcolor"]
                card_app.container1.border = border.all(2, updated_colors["card_border_color"])
                #card_app.icon_container_.bgcolor = updated_colors["icon_background_color"]

                card_app.container1.content.controls[0].content.controls[0].border = border.all(2, updated_colors[
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
                #card_app.icon_container_.update()
                card_app.container1.update()

            """обновление контейнера с похожими товарами"""
            similar_product.color = update_colors()['text_color']
            show_conteiner.content.controls[0].controls[0].bgcolor = update_colors()['bgcolor']

            page.update()


        """Upper Content"""

        """Menu content"""
        Menu_content = Row(
            controls=[
                Container(
                    content=Column(
                        controls=[
                            Container(
                                content=Text("Категории", size=update_size()["Menu_zag_text_size"],
                                             color=update_colors()["text_color"],),
                                padding=padding.only(top=10, left=10),
                            ),
                            Divider(height=2, color=update_colors()["text_color"]),
                            Container(
                                content=TextButton(
                                    content=Text("Струнные", size=update_size()["Menu_other_text_size"],
                                                 color=update_colors()["text_color"]),
                                    on_click=lambda e: next_page('/category/Струнные')),
                                padding=padding.only(left=10),
                            ),
                            Container(
                                content=TextButton(
                                    content=Text("Духовые", size=update_size()["Menu_other_text_size"],
                                                 color=update_colors()["text_color"]),
                                    on_click=lambda e: next_page('/category/Духовые')),
                                padding=padding.only(left=10),
                            ),
                            Container(
                                content=TextButton(
                                    content=Text("Ударные", size=update_size()["Menu_other_text_size"],
                                                 color=update_colors()["text_color"]),
                                    on_click=lambda e: next_page('/category/Ударные')),
                                padding=padding.only(left=10),
                            ),
                            Container(
                                content=TextButton(
                                    content=Text("Клавишные", size=update_size()["Menu_other_text_size"],
                                                 color=update_colors()["text_color"]),
                                    on_click=lambda e: next_page('/category/Клавишные')),
                                padding=padding.only(left=10),
                            ),
                            Container(
                                content=TextButton(
                                    content=Text("Электро инструменты", size=update_size()["Menu_other_text_size"],
                                                 color=update_colors()["text_color"]),
                                    on_click=lambda e: next_page('/category/Электроинструменты')),
                                padding=padding.only(left=10),
                            ),
                            Container(
                                content=TextButton(
                                    content=Text("Аксессуары", size=update_size()["Menu_other_text_size"],
                                                 color=update_colors()["text_color"]),
                                    on_click=lambda e: next_page('/category/Аксессуары')),
                                padding=padding.only(left=10),
                            ),
                            Container(
                                content=TextButton(
                                    content=Text("Производители", size=update_size()["Menu_other_text_size"],
                                                 color=update_colors()["text_color"]),
                                    on_click=lambda e: next_page('/Производители')),
                                padding=padding.only(left=10),
                            ),
                            Divider(height=2, color=update_colors()["text_color"]),
                            Container(
                                content=TextButton(
                                    content=Text("Главная", size=update_size()["Menu_zag_text_size"],
                                                 color=update_colors()["text_color"]),
                                    on_click=lambda e: next_page('/')),
                                padding=padding.only(left=5),
                            ),
                            Container(
                                content=TextButton(
                                    content=Text("Лента товаров", size=update_size()["Menu_zag_text_size"],
                                                 color=update_colors()["text_color"]),
                                    on_click=lambda e: next_page('/productsfeed')),
                                padding=padding.only(left=5),
                            ),
                            Container(
                                content=TextButton(
                                    content=Text("Расширенный поиск", size=update_size()["Menu_zag_text_size"],
                                                    color=update_colors()["text_color"]),
                                    on_click=lambda e: next_page('/search')),
                                padding=padding.only(left=5),
                            ),
                        ],
                        # scroll=ScrollMode.ALWAYS
                    ),
                    expand=1,
                    border_radius=15,
                    alignment=Alignment(-1, 1),
                    border=border.all(width=2, color=update_colors()["border_color"]),
                    bgcolor=update_colors()["bgcolor"],
                ),
                Container(
                    Container(
                        on_click=animate_menu,
                    ),
                    expand=5
                ),
            ],
            expand=True,
            width=page.width,
            height=page.height - 15,
            offset=transform.Offset(-2, 0),
            animate_offset=animation.Animation(300),
        )
        """Menu btn"""
        Menu_but = IconButton(icon=Icons.MENU,
                              icon_color=update_colors()["icon_color"],
                              icon_size=update_size()["icon_rectangle_size"],
                              on_click=animate_menu)
        """style btn"""
        icon_but = IconButton(icon=Icons.SUNNY, on_click=style_revert, icon_color=update_colors()["icon_color"],
                              icon_size=update_size()['icon_rectangle_size'])
        """cart_batton"""
        Cart_button = IconButton(icon=Icons.SHOPPING_CART, icon_color=update_colors()["icon_color"],
                                 icon_size=update_size()['icon_rectangle_size'],
                                 on_click=lambda e: cart_muve(e))
        """profile"""
        Profile_button = IconButton(icon=Icons.PERSON, icon_color=update_colors()["icon_color"],
                                    icon_size=update_size()['icon_rectangle_size'],
                                    on_click=profile_muve)
        """top rectangle"""
        top_rectangle = Container(
            content=Row(
                [
                    Menu_but,
                    Row(
                        [icon_but, Cart_button, Profile_button],
                        alignment=MainAxisAlignment.END,
                        spacing=10,
                    ),
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
        )
        """buy"""
        buy_btn = Container(
            content=Row(
                controls=[
                    Column(
                        controls=[
                            Text("Купить", size=13, color=update_colors()["text_color"], text_align=TextAlign.CENTER),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    )
                ],
                alignment=MainAxisAlignment.CENTER,
                expand=True,
            ),
            border=border.all(width=2, color=update_colors()["border_color"]),
            alignment=Alignment(0, 0),
            bgcolor=update_colors()["bgcolor"],
            on_hover=hower_btn_buy,
            on_click=lambda e: on_click_buy(e),
            padding=padding.only(left=1),
            margin=margin.only(left=1, bottom=1),
            expand=True,
            width=146,
            height=50,
        )
        """basket"""
        basket_btn = Container(
            content=Row(
                controls=[
                    Column(
                        controls=[
                            Text("В корзину", size=13, color=update_colors()["text_color"]),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    )
                ],
                alignment=MainAxisAlignment.CENTER,
                expand=True,
            ),
            border=border.all(width=2, color=update_colors()["border_color"]),
            alignment=Alignment(0, 0),
            bgcolor=update_colors()["bgcolor"],
            expand=True,
            on_hover=hower_btn_basket,
            on_click=lambda e: on_click_bascet(e),
            padding=padding.only(right=1),
            margin=margin.only(right=1, bottom=1),
            width=146,
            height=50,
        )
        price_value = Text(f"{str(self.price)} ₽", size=30, color=update_colors()["text_color"])
        btn_row = Row(
            controls=[
                buy_btn,
                basket_btn,
            ],
            spacing=2,
            expand=True,
        )
        """buy window"""
        buy_window = Container(
            content=Row(
                controls=[
                    Column(
                        [
                            Container(
                                content=price_value,
                                # padding=padding.only(bottom=40),
                                alignment=Alignment(0, 0),
                                expand=2,
                            ),
                            Container(
                                content=btn_row,
                                alignment=Alignment(0, 1),
                                expand=1,
                            ),

                        ],
                        alignment=MainAxisAlignment.CENTER,
                        expand=True,
                    )
                ],
                alignment=MainAxisAlignment.CENTER,
                expand=True,
            ),
            border=border.all(width=2, color=update_colors()["border_color"]),
            width=300,
            height=150,
        )
        """specifications window"""
        specifications = Column(controls=[Container(
            content=Row(
                controls=[Column(
                    controls=[
                        Container(
                            content=Row(
                                controls=[Text("Характеристики", size=30, color=update_colors()["text_color"],
                                               text_align=TextAlign.CENTER, )
                                          ],
                                alignment=MainAxisAlignment.CENTER,
                                expand=True
                            ),
                            alignment=Alignment(0, 0),
                            height=55,
                            width=330,
                        ),
                        Text(f"название товара: {self.name}", size=15, color=update_colors()["text_color"]),
                        Text(f"категория: {self.category}", size=15, color=update_colors()["text_color"]),
                        Text(f"брэнд: {self.brand}", size=15, color=update_colors()["text_color"]),
                        Text(f"количество покупок: {self.quantity}", size=15, color=update_colors()["text_color"]),
                        Text(f"цвет: {self.color}", size=15, color=update_colors()["text_color"]),
                        Text(f"осталось: {self.warehouse}", size=15, color=update_colors()["text_color"]),
                    ],
                    alignment=MainAxisAlignment.START,
                ),
                ],
                expand=True
            ),
            border=border.all(2, color=update_colors()["border_color"]),
            border_radius=15,
            alignment=Alignment(-1, -1),
            padding=padding.only(left=10),
            height=300,
            width=350,
        )
        ],
            alignment=MainAxisAlignment.START,
        )
        """Image product"""
        Image_Product = Container(content=Row(
            controls=[Container(
                content=Image(
                    src_base64=self.image_base64,
                    # fit=ImageFit.,  # Растягиваем изображение по высоте
                    width=400,  # Задаем ширину изображения
                    height=400,  # Задаем высоту изображения
                    border_radius=15,
                    expand=True
                ),

                border=border.all(width=2, color=update_colors()["border_color"]),
                border_radius=15,
                alignment=Alignment(0, 0),
                width=400,
                height=400,
            )
            ],
            alignment=MainAxisAlignment.START,
            expand=True,
        ),
            padding=padding.only(left=400),
        )
        """product inf"""
        product_inf = Container(
            content=Row(
                controls=[
                    Image_Product,
                    specifications,
                    Column(
                        controls=[
                            buy_window
                        ],
                        alignment=MainAxisAlignment.START,
                        expand=True,
                    ),
                ],
                expand=True
            ),
            expand=True,
            width=page.width,
            height=400,
            # border=border.all(width=2, color=update_colors()["border_color"]),
        )
        """uppper part"""
        upper_part = Container(
            content=Column(
                [
                    top_rectangle,
                    product_inf,
                    Divider(2, color=update_colors()["border_color"]),
                ]
            )
        )

        """Under part"""

        """background"""
        icon_back = Container(content=update_images(), expand=True)

        products = self.get_products_categoryes(self.category)

        # Для каждого товара создаем карточку
        product_card = []
        if products:
            for product in products:
                id_product = product[0]
                name = product[1]
                category = product[2]
                brand = product[3]
                price_prod = product[4]
                quantity = product[5]
                color = product[6]
                image_base64 = product[7]
                warehouse = product[8]

                app = Card_generate(id_product, name, price_prod, image_from_base64(image_base64), category, quantity, page, brand)
                product_card.append(app)
        else:
            pass


        """Product row"""
        product_row = Row(
            controls=[card.card2 for card in product_card],
            spacing=20,
            alignment=MainAxisAlignment.START,
            vertical_alignment=CrossAxisAlignment.CENTER,
        )
        """similar products"""
        similar_product = Text("Похожие товары", color=update_colors()["text_color"], size=update_size()["Title_size"])
        show_conteiner = Container(
            content=Column(
                controls=[
                    Row(controls=[
                        Container(
                            content=Container(
                                content=Column(
                                    controls=[
                                        similar_product,
                                        Divider(height=2, color=update_colors()["text_color"]),
                                        Row(
                                            controls=[Container(content=product_row, height=215,
                                                                alignment=Alignment(0, -1))],
                                            scroll=ScrollMode.AUTO,
                                        ),
                                    ],
                                    expand=True,
                                ),
                                padding=padding.only(left=10, right=10, top=10, bottom=10),
                            ),
                            border=border.all(width=2, color=update_colors()["border_color"]),
                            border_radius=10,
                            alignment=Alignment(0, 0),
                            height=470,
                            width=page.width - 300,
                            bgcolor=update_colors()["bgcolor"],
                        ),
                    ],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                ],
                spacing=10,
                scroll=ScrollMode.ALWAYS,
            ),
            width=page.width,
            height=page.height / 1.42,
            # padding=padding.only(bottom=10),
            # border=border.all(width=2, color='white'),
        )

        downer_part = Container(
            content=Column(
                [
                    Stack(
                        [
                            icon_back,
                            show_conteiner,
                        ]
                    )
                ]
            )
        )

        """Content"""
        content = Stack(
            [
                Column(
                    [
                        upper_part, downer_part,
                    ]
                ),
                Menu_content
            ]
        )

        return View("/cardinfo/id", controls=[content])

from flet import *
from help_function.manufactures_card import Manufactures_Card
from flet_route import Params, Basket
from help_function.Navigation import Navigation

class ManufacturePage(Navigation):
    def __init__(self):
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

        def next_page(muve):
            page.client_storage.set("muve", muve)
            page.go("/loading")

        def image_from_base64(base64_str: str):
            return Image(src=f"data:image/jpeg;base64,{base64_str}", width=200, height=200)

        def update_colors():
            if page.theme_mode == ThemeMode.LIGHT:
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

        def update_size():
            return {
                "icon_rectangle_size": 20,
                "divider_size": 5,
                "Menu_zag_text_size": 20,
                "Menu_other_text_size": 18,
                "Title_size": 35,
            }

        def animate_menu(e):
            Menu_content.offset = transform.Offset(0, 0) if Menu_content.offset == transform.Offset(-2, 0) else transform.Offset(
                -2, 0)
            Menu_content.update()

        def style_revert(e):
            if page.theme_mode == ThemeMode.DARK:
                page.theme_mode = ThemeMode.LIGHT
                icon_but.icon = icons.DARK_MODE_OUTLINED
                icon_but.icon_color = Colors.BLACK
            else:
                page.theme_mode = ThemeMode.DARK
                icon_but.icon = icons.SUNNY
                icon_but.icon_color = Colors.BLUE

            colors = update_colors()

            icon_back.content = update_images()

            """обновление названия и полоски разделителя"""
            Category_title.color = colors["text_color"]
            divider.color = colors['text_color']

            # Обновление иконок в top_rectangle
            Cart_button.icon_color = colors["icon_color"]
            Profile_button.icon_color = colors["icon_color"]

            # обновление меню
            Menu_but.icon_color = colors["icon_color"]

            Menu_content.controls[0].bgcolor=update_colors()['bgcolor']
            Menu_content.controls[0].border=update_colors()['border_color']
            """Обновление цветов в меню"""
            Menu_content.controls[0].bgcolor = update_colors()['bgcolor']
            Menu_content.controls[0].border = border.all(2, update_colors()['border_color'])
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

            page.update()

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


        """Верхняя часть"""
        Menu_content = Row(
            controls=[
                Container(
                    content=Column(
                        controls=[
                            Container(
                                content=Text("Категории", size=update_size()["Menu_zag_text_size"],
                                             color=update_colors()["text_color"]),
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
                                padding=padding.only(left=10),
                            ),
                            Container(
                                content=TextButton(
                                    content=Text("Лента товаров", size=update_size()["Menu_zag_text_size"],
                                                    color=update_colors()["text_color"]),
                                    on_click=lambda e: next_page('/')),
                                padding=padding.only(left=10),
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

        Menu_but = IconButton(icon=icons.MENU,
                              icon_color=update_colors()["icon_color"],
                              icon_size=update_size()["icon_rectangle_size"],
                              on_click=animate_menu)
        icon_but = IconButton(icon=icons.SUNNY, on_click=style_revert, icon_color=update_colors()["icon_color"],
                              icon_size=update_size()['icon_rectangle_size'])
        Cart_button = IconButton(icon=icons.SHOPPING_CART, icon_color=update_colors()["icon_color"],
                                 icon_size=update_size()['icon_rectangle_size'])
        Profile_button = IconButton(icon=icons.PERSON, icon_color=update_colors()["icon_color"],
                                    icon_size=update_size()['icon_rectangle_size'])

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
        Category_title = Text("Производители", size=70, weight=FontWeight.BOLD, color=update_colors()["text_color"],)
        divider = Divider(height=update_size()["divider_size"], color=update_colors()["border_color"])
        first_part = Column(
            [
                top_rectangle,
                Container(content=Category_title, alignment=Alignment(0, 0), padding=padding.only(top=20)),
                Container(content=divider, alignment=Alignment(0, 0), padding=padding.only(top=20)),
            ]
        )
        """Нижняя часть"""
        icon_back = Container(content=update_images(), expand=True)

        "Создание карточек с товарами"

        manufacture = self.get_all_manufacturers()
        print(manufacture)
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
                row = Row(
                    controls=[
                        manufacturer_cards[i],
                        manufacturer_cards[i + 1]
                    ],
                    alignment=MainAxisAlignment.CENTER,
                    spacing=20,
                )
            else:
                # Если последняя карточка без пары
                row = Row(
                    controls=[manufacturer_cards[i]],
                    alignment=MainAxisAlignment.CENTER,
                    spacing=20,
                )
            rows.append(row)

        show_conteiner = Container(
            content=Column(
                controls=[
                    Container(
                        content=Column(
                            controls=rows,
                            alignment=MainAxisAlignment.CENTER,
                        ),
                        alignment=Alignment(0, 0),
                        expand=True,
                    )
                ],
                spacing=10,
                scroll=ScrollMode.ALWAYS,
            ),
            width=page.width,
            height=page.height / 1.42,
            # padding=padding.only(bottom=10),
            # border=border.all(width=2, color='white'),
        )
        """соединение всех элементов страницы"""
        return View("/Производители", controls=[
            Stack([
                Column(
                    controls=[
                        first_part,
                        Stack([
                            icon_back,
                            show_conteiner,
                        ])
                    ]
                ),
                Menu_content,
            ]
            ),
        ]
                    )

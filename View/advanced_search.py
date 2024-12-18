from flet_route import Params, Basket
from flet import *
from help_function.Navigation import Navigation
from help_function.Card_generate import Card_generate


# Страница расширенного поиска
class AdvancedSearchPage(Navigation):
    def __init__(self):
        super().__init__()
        self.name = None
        self.category = None
        self.min_price = None
        self.max_price = None
        self.manufacturer = None
        self.color = None
        self.sort_by = None
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

    def view(self, page: Page, params: Params, basket: Basket):
        page.theme_mode = ThemeMode.DARK
        product_id = basket.get("advance_id")
        list_search = basket.get("state_filter")
        if list_search:
            self.name, self.category, self.min_price, self.max_price, self.manufacturer, self.color, self.sort_by = list_search

        def create_dropdown_options(options_list):
            return [dropdown.Option(option) for option in options_list]

        """верхняя часть"""

        def image_from_base64(base64_str: str):
            return Image(src=f"data:image/jpeg;base64,{base64_str}", width=200, height=200)

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

        def animate_menu(e):
            Menu_content.offset = transform.Offset(0, 0) if Menu_content.offset == transform.Offset(-2,
                                                                                                    0) else transform.Offset(
                -2, 0)
            Menu_content.update()

        def update_size():
            return {
                "icon_rectangle_size": 20,
                "divider_size": 5,
                "Menu_zag_text_size": 20,
                "Menu_other_text_size": 18,
                "Title_size": 35,
            }

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

            # Обновление иконок в top_rectangle
            Cart_button.icon_color = colors["icon_color"]
            Profile_button.icon_color = colors["icon_color"]

            # обновление меню
            Menu_but.icon_color = colors["icon_color"]

            # Menu_content.controls[0].bgcolor=update_colors()['bgcolor']
            # Menu_content.controls[0].border=update_colors()['border_color']
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
            Menu_content.controls[0].content.controls[12].content.content.color = update_colors()['text_color']

            name_textfield.cursor_color=update_colors()["text_color"]
            name_textfield.color=update_colors()["text_color"]
            name_textfield.fill_color=update_colors()["bgcolor"]
            name_textfield.border_color=update_colors()["border_color"]
            name_textfield.label_style=TextStyle(color=update_colors()["text_color"])

            min_price_field.cursor_color = update_colors()["text_color"]
            min_price_field.color = update_colors()["text_color"]
            min_price_field.fill_color = update_colors()["bgcolor"]
            min_price_field.border_color = update_colors()["border_color"]
            min_price_field.label_style = TextStyle(color=update_colors()["text_color"])

            max_price_field.cursor_color = update_colors()["text_color"]
            max_price_field.color = update_colors()["text_color"]
            max_price_field.fill_color = update_colors()["bgcolor"]
            max_price_field.border_color = update_colors()["border_color"]
            max_price_field.label_style = TextStyle(color=update_colors()["text_color"])

            color_field.cursor_color = update_colors()["text_color"]
            color_field.color = update_colors()["text_color"]
            color_field.fill_color = update_colors()["bgcolor"]
            color_field.border_color = update_colors()["border_color"]
            color_field.label_style = TextStyle(color=update_colors()["text_color"])

            category_dropdown.bgcolor = update_colors()["bgcolor"]
            category_dropdown.border_color = update_colors()["border_color"]
            category_dropdown.color = update_colors()["text_color"]
            category_dropdown.label_style = TextStyle(color=update_colors()["text_color"])

            manufacturer_dropdown.bgcolor = update_colors()["bgcolor"]
            manufacturer_dropdown.border_color = update_colors()["border_color"]
            manufacturer_dropdown.color = update_colors()["text_color"]
            manufacturer_dropdown.label_style = TextStyle(color=update_colors()["text_color"])

            sorted_dropdown.bgcolor = update_colors()["bgcolor"]
            sorted_dropdown.border_color = update_colors()["border_color"]
            sorted_dropdown.color = update_colors()["text_color"]
            sorted_dropdown.label_style = TextStyle(color=update_colors()["text_color"])

            search_button.icon_color = colors["text_color"]
            Label.color = colors["text_color"]

            icon_back.content = update_images()
            for card_app in product_card:
                updated_colors = card_app.update_colors()
                card_app.container1.bgcolor = updated_colors["bgcolor"]
                card_app.container1.border = border.all(2, updated_colors["card_border_color"])
                # card_app.icon_container_.bgcolor = updated_colors["icon_background_color"]

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
                # card_app.icon_container_.update()
                card_app.container1.update()


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

        def create_card_rows(cards, max_cards_per_row=8):
            rows = []
            for i in range(0, len(cards), max_cards_per_row):
                card_row = cards[i:i + max_cards_per_row]  # Берем срез карточек
                row = Row(
                    controls=[card.card2 for card in card_row],  # Добавляем карточки в строку
                    spacing=20,
                    alignment=MainAxisAlignment.START,
                    vertical_alignment=CrossAxisAlignment.CENTER,
                )
                rows.append(row)
            return rows

        def research(e):
            name = name_textfield.value if name_textfield.value else None
            category = category_dropdown.value if category_dropdown.value else None
            min_price = min_price_field.value if min_price_field.value else None
            max_price = max_price_field.value if max_price_field.value else None
            manufacturer = manufacturer_dropdown.value if manufacturer_dropdown.value else None
            color = color_field.value if color_field.value else None
            sorted = sorted_dropdown.value if sorted_dropdown.value else None
            prod_id = []
            for i in self.search_product(name, category, min_price, max_price, manufacturer, color, sorted):
                prod_id.append(i[0])
            basket.advance_id = prod_id
            list_filter = [name, category, min_price, max_price, manufacturer, color, sorted]
            basket.state_filter = list_filter
            next_page("/search")


        Menu_content = Row(
            controls=[
                Container(
                    content=Column(
                        [
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
                                    on_click=lambda e: next_page("/category/Струнные")),
                                padding=padding.only(left=10),
                            ),
                            Container(
                                content=TextButton(
                                    content=Text("Духовые", size=update_size()["Menu_other_text_size"],
                                                 color=update_colors()["text_color"]),
                                    on_click=lambda e: next_page("/category/Духовые")),
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

        Menu_but = IconButton(icon=icons.MENU,
                              icon_color=update_colors()["icon_color"],
                              icon_size=update_size()["icon_rectangle_size"],
                              on_click=animate_menu, )
        # Верхний прямоугольник
        icon_but = IconButton(icon=icons.SUNNY, on_click=style_revert, icon_color=update_colors()["icon_color"],
                              icon_size=update_size()['icon_rectangle_size'])
        Cart_button = IconButton(icon=icons.SHOPPING_CART, icon_color=update_colors()["icon_color"],
                                 icon_size=update_size()['icon_rectangle_size'],
                                 on_click=lambda e: cart_muve(e))
        Profile_button = IconButton(icon=icons.PERSON, icon_color=update_colors()["icon_color"],
                                    icon_size=update_size()['icon_rectangle_size'], on_click=profile_muve)

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

        name_textfield = TextField(label="Поиск по названию товара", width=400, value=self.name,
                                   cursor_color=update_colors()["text_color"],
                                   color=update_colors()["text_color"],
                                   fill_color=update_colors()["bgcolor"],
                                   border_color=update_colors()["border_color"],
                                   label_style=TextStyle(color=update_colors()["text_color"],))
        name_search = Container(
            content=name_textfield,
            alignment=Alignment(0, -1)
        )
        category_dropdown = Dropdown(
            label="Категория",
            options=[
                dropdown.Option("None", " "),
                dropdown.Option("Клавишные"),
                dropdown.Option("Струнные"),
                dropdown.Option("Духовые"),
                dropdown.Option("Ударные"),
                dropdown.Option("Аксессуары")
            ],
            value=self.category,
            bgcolor=update_colors()["bgcolor"],
            border_color=update_colors()["border_color"],
            color=update_colors()["text_color"],
            label_style=TextStyle(color=update_colors()["text_color"],),

        )
        category_search = Container(
            content=category_dropdown,
            alignment=Alignment(-1, -1)
        )
        min_price_field = TextField(label="Минимальная цена", input_filter=NumbersOnlyInputFilter(), value=self.min_price,
                                    cursor_color=update_colors()["text_color"],
                                    color=update_colors()["text_color"],
                                    fill_color=update_colors()["bgcolor"],
                                    border_color=update_colors()["border_color"],
                                    label_style=TextStyle(color=update_colors()["text_color"], )
                                    )
        min_price_search = Container(
            content=min_price_field,
            alignment=Alignment(-1, -1),
        )
        max_price_field = TextField(label="Максимальная цена", input_filter=NumbersOnlyInputFilter(), value=self.max_price,
                                    cursor_color=update_colors()["text_color"],
                                    color=update_colors()["text_color"],
                                    fill_color=update_colors()["bgcolor"],
                                    border_color=update_colors()["border_color"],
                                    label_style=TextStyle(color=update_colors()["text_color"], )
                                    )
        max_price_search = Container(
            content=max_price_field,
            alignment=Alignment(-1, -1),
        )
        manufacturer_name = []
        manufacturer_name.append(" ")
        for i in self.get_all_manufacturers():
            manufacturer_name.append(i[1])
        manufacturer_dropdown = Dropdown(
            label="Производитель",
            options=create_dropdown_options(manufacturer_name),
            value=self.manufacturer,
            bgcolor=update_colors()["bgcolor"],
            border_color=update_colors()["border_color"],
            color=update_colors()["text_color"],
            label_style=TextStyle(color=update_colors()["text_color"], ),
        )
        manufacturer_search = Container(
            content=manufacturer_dropdown,
            alignment=Alignment(-1, -1)
        )
        color_field = TextField(label="Цвет", value=self.color,
                                cursor_color=update_colors()["text_color"],
                                color=update_colors()["text_color"],
                                fill_color=update_colors()["bgcolor"],
                                border_color=update_colors()["border_color"],
                                label_style=TextStyle(color=update_colors()["text_color"], )
                                )
        color_search = Container(
            content=color_field,
            alignment=Alignment(-1, -1),
        )
        sorted_dropdown = Dropdown(
            label="Сортировка",
            options=[
                dropdown.Option("None", " "),
                dropdown.Option("price", "Цена по возрастанию"),
                dropdown.Option('popularity', "по популярности"),
                dropdown.Option('new', "по новизне товара"),
            ],
            value=self.sort_by,
            bgcolor=update_colors()["bgcolor"],
            border_color=update_colors()["border_color"],
            color=update_colors()["text_color"],
            label_style=TextStyle(color=update_colors()["text_color"]),
        )
        sorted_search = Container(
            content=sorted_dropdown,
            alignment=Alignment(-1, -1),
        )
        search_button = ElevatedButton(text="Искать", on_click=lambda e: research(e), width=400)

        Label = Text("Расширенный поиск", size=50, color = update_colors()["text_color"])
        Label_container = Container(
            content=Label,
            alignment=Alignment(0, 0),
            padding=padding.only(top=30),
            expand=True,
        )
        divider = Divider(height=2, color=update_colors()["text_color"])
        """Нижняя часть"""
        """Нижняя часть"""
        icon_back = Container(content=update_images(), expand=True)

        "Создание карточек с товарами"
        products = []
        product_card = []
        prroduct_row = []
        if product_id:
            for i in product_id:
                products.append(self.get_product_id(int(i)))
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

                    app = Card_generate(id_product, name, price, image_from_base64(image_base64), category, quantity,
                                        page, brand)

                    product_card.append(app)
                product_row = create_card_rows(product_card)
            else:
                product_row = []
        else:
            product_row = []

        card_container = Container(
            content=Column(
                controls=[
                    Row(
                        controls=[
                            Container(
                                content=Column(
                                    controls=product_row
                                ),
                                padding=padding.only(left=50, right=50),
                                expand=True,
                            ),

                        ],
                        scroll=ScrollMode.AUTO,
                    )
                ],
                scroll=ScrollMode.ALWAYS
            ),
            width=page.width,
            height=page.height / 1.36,
        )
        content = Container(
            content=Column(
                controls=[
                    top_rectangle,
                    Label_container,
                    Container(
                        content=Row(
                            controls=[
                                name_search,
                            ],
                            alignment=MainAxisAlignment.CENTER
                        ),
                        alignment=Alignment(0, 0),
                        expand=True,
                    ),
                    Container(
                        content=Row(
                            controls=[
                                category_search,
                                min_price_search,
                                max_price_search,
                            ],
                            alignment=MainAxisAlignment.CENTER,
                        ),
                        alignment=Alignment(0, 0),
                    ),
                    Container(
                        content=Row(
                            controls=[
                                manufacturer_search,
                                color_search,
                                sorted_search,
                            ],
                            alignment=MainAxisAlignment.CENTER,
                        ),
                        alignment=Alignment(0, 0)
                    ),
                    Row(
                        controls=[
                            search_button,
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                    divider,
                    Stack(
                        [
                            icon_back,
                            card_container,
                        ]
                    )
                ]
            )
        )

        return View("/search", controls=[
            Stack(
                [
                    content,
                    Menu_content
                ]
            )
        ]
                    )

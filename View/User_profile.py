from flet import *
from flet_route import Params, Basket
from help_function.Navigation import Navigation
import base64
import aiohttp
import asyncio
from help_function.Admin_control import Admin_control
from help_function.Crypt import Crypt


class UserPage(Navigation):
    def __init__(self):
        super().__init__()
        self.action = None

    def view(self, page: Page, params: Params, basket: Basket):

        page.theme_mode = ThemeMode.DARK
        self.key, self.user_name = page.client_storage.get("key")
        user_info = self.get_user_info(self.user_name, self.key)
        self.id = user_info[0]
        self.name = user_info[1]
        self.number = user_info[2]
        self.role = user_info[3]
        self.photo = user_info[4]

        def next_page(muve):
            page.client_storage.set("muve", muve)
            page.go("/loading")

        def cart_muve(e):
            if page.client_storage.get("key") == None:
                next_page("/login")
            else:
                next_page("/cart")

        async def fetch_image_base64(image_url):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(image_url) as response:
                        if response.status == 200:
                            image_bytes = await response.read()
                            return base64.b64encode(image_bytes).decode("utf-8")
                        else:
                            print(f"Ошибка при загрузке изображения: {response.status}")
                            return None
            except Exception as e:
                print(f"Ошибка при загрузке изображения: {e}")
                return None

        # Ссылки на элементы интерфейса
        photo_display = Ref[Container]()
        user_info_display = Ref[Column]()  # Ссылка для обновления информации пользователя

        # Функция для загрузки и отображения изображения по URL
        async def load_photo_by_url(url):
            try:
                # Конвертируем изображение в Base64
                base64_image = await fetch_image_base64(url)
                if base64_image:
                    self.photo = base64_image
                    # Обновляем контейнер с фотографией
                    photo_display.current.content = Image(
                        src_base64=base64_image,
                        width=200,
                        height=200,
                        fit=ImageFit.COVER,
                    )
                    page.update()

                    # Скрываем поле для ввода URL и очищаем его
                    url_input_container.visible = False
                    url_input_field.value = ""  # Очищаем поле ввода
                    result = self.update_photo(base64_image, self.key, self.id)
                    if result:
                        page.snack_bar = SnackBar(
                            content=Row([Text(f"Вы успешно изменили фото профиля!", color='white')],
                                        alignment=MainAxisAlignment.CENTER),
                            bgcolor=Colors.GREEN,
                        )
                        page.snack_bar.open = True
                    else:
                        page.snack_bar = SnackBar(
                            content=Row([Text(f"Что пошло не так при загрузке изображения!", color='white')],
                                        alignment=MainAxisAlignment.CENTER),
                            bgcolor=Colors.RED,
                        )
                        page.snack_bar.open = True
                    page.update()
                else:
                    page.snack_bar = SnackBar(
                        content=Row([Text("Ошибка при загрузке по указанному URL!", color='white')],
                                    alignment=MainAxisAlignment.CENTER),
                        bgcolor=Colors.RED,
                    )
                    page.snack_bar.open = True
                    page.update()
            except Exception as e:
                page.snack_bar = SnackBar(
                    content=Row([Text(f"Ошибка при обработке URL: {e}", color='white')],
                                alignment=MainAxisAlignment.CENTER),
                    bgcolor=Colors.RED,
                )
                page.snack_bar.open = True
                page.update()

        def cancel_action(e):
            url_input_container.visible = False
            url_input_field.value = ""
            page.update()

        # Функция обработки нажатия на кнопку "Добавить фото"

        def show_url_input(action):
            if action == "password":
                page.close(dlg_password)
                url_input_field.label = "Новый пароль"
                self.action = "password"
            elif action == "phone":
                url_input_field.label = "Новый номер телефона"
                self.action = "phone"
            elif action == "photo":
                url_input_field.label = "Введите URL изображения"
                self.action = "photo"
            url_input_container.visible = True
            page.update()

        def log_out(e):
            result = self.LOG_OUT(self.key, self.id)
            if result:
                page.snack_bar = SnackBar(
                    content=Row([Text("Вы успешно вышли из аккаунта!", color='white')],
                                alignment=MainAxisAlignment.CENTER),
                    bgcolor=colors.GREEN,

                )
                page.snack_bar.open = True
                page.update()
                page.client_storage.remove("key")
                next_page("/login")
            else:
                page.snack_bar = SnackBar(
                    content=Row([Text("Что-то пошло не так!", color='white')],
                                alignment=MainAxisAlignment.CENTER),
                    bgcolor=colors.RED,

                )
                page.snack_bar.open = True
                page.update()

        # Функция обработки нажатия на кнопку "Загрузить по URL"
        def upload_photo_by_url(e):
            url = url_input_field.value  # Получаем значение из TextField
            if url:
                asyncio.run(load_photo_by_url(url))
            else:
                page.snack_bar = SnackBar(
                    content=Row([Text("Введите корректный URL!", color='white')],
                                alignment=MainAxisAlignment.CENTER),
                    bgcolor=Colors.RED,
                )
                page.snack_bar.open = True
                page.update()

        def post_phone_namber(number):
            if self.update_phone(number, self.key, self.id):
                page.snack_bar = SnackBar(
                    content=Row([Text("Вы успешно сменили номер телефона!", color='white')],
                                alignment=MainAxisAlignment.CENTER),
                    bgcolor=colors.GREEN,
                )
                page.snack_bar.open = True
                phone_text.value = f"Телефон: {number}"
            else:
                page.snack_bar = SnackBar(
                    content=Row([Text("Произошла ошибка при смене номера телефона!", color='white')],
                                alignment=MainAxisAlignment.CENTER),
                    bgcolor=colors.RED,
                )
                page.snack_bar.open = True
            url_input_field.value = ''
            cancel_action(None)

        def upload_phone_number(e):
            number = url_input_field.value
            if number:
                if not number:
                    page.snack_bar = SnackBar(
                        content=Row([
                            Text('Введите номер телефона!', color='white')
                        ], alignment=MainAxisAlignment.CENTER
                        ),
                        bgcolor=colors.RED,
                    )
                    page.snack_bar.open = True
                    page.update()
                    return
                else:
                    try:
                        if isinstance(int(number), int):
                            page.update()
                            pass
                        else:
                            if not (number[0] == "+" and isinstance(
                                    int(number[1:]),
                                    int)):
                                page.snack_bar = SnackBar(
                                    content=Row([
                                        Text('Некоректный символ в номере!', color='white')
                                    ], alignment=MainAxisAlignment.CENTER
                                    ),
                                    bgcolor=colors.RED,
                                )
                                page.snack_bar.open = True
                                page.update()
                                return
                    except Exception:
                        page.snack_bar = SnackBar(
                            content=Row([
                                Text('Некоректный символ в номере!', color='white')
                            ], alignment=MainAxisAlignment.CENTER
                            ),
                            bgcolor=colors.RED,
                        )
                        page.snack_bar.open = True
                        page.update()
                        return
            else:
                page.snack_bar = SnackBar(
                    content=Row([Text("Введите номер телефона!", color='white')],
                                alignment=MainAxisAlignment.CENTER),
                    bgcolor=Colors.RED,
                )
                page.snack_bar.open = True
                page.update()
                return
            post_phone_namber(number)

        def upload_password(e):
            password = url_input_field.value
            if password:
                result = self.update_password(password, self.key, self.id)
                if result:
                    page.snack_bar = SnackBar(
                        content=Row([Text("Вы успешно сменили пароль!", color='white')],
                                    alignment=MainAxisAlignment.CENTER),
                        bgcolor=Colors.GREEN,
                    )
                    page.snack_bar.open = True
                    page.update()
                else:
                    page.snack_bar = SnackBar(
                        content=Row([Text("Ошибка при смене пароля!", color='white')],
                                    alignment=MainAxisAlignment.CENTER),
                        bgcolor=Colors.RED,
                    )
                    page.snack_bar.open = True
                    page.update()
                url_input_field.value = ""
                cancel_action(e)
                page.update()
            else:
                page.snack_bar = SnackBar(
                    content=Row([Text("Введите пароль!", color='white')],
                                alignment=MainAxisAlignment.CENTER),
                    bgcolor=Colors.RED,
                )
                page.snack_bar.open = True
                page.update()

        def settings_muve():
            if self.get_shop_state(self.role):
                page.snack_bar = SnackBar(
                    content=Row([Text("Особый режим не включен!", color='white')],
                                alignment=MainAxisAlignment.CENTER),
                    bgcolor=colors.RED,

                )
                page.snack_bar.open = True
                page.update()
            else:
                next_page("/settings_admin")

        def dialog_window(value):
            if value == "password":
                page.open(dlg_password)
            elif value == "delete":
                page.open(dlg_delete)
            elif value == "settings":
                settings_muve()
            else:
                page.open(dlg_logout)

        def action_button(e):
            if self.action == "photo":
                upload_photo_by_url(e)
            elif self.action == "phone":
                upload_phone_number(e)
            elif self.action == "password":
                upload_password(e)

        # Функции для изменений информации
        def delete_account(e):
            result = self.DELETE_ACCOUNT(self.key, self.id)
            if result:
                page.snack_bar = SnackBar(
                    content=Row([Text(f"Вы удалили аккаунт {self.name}(", color='white')],
                                alignment=MainAxisAlignment.CENTER),
                    bgcolor=Colors.GREEN,
                )
                page.snack_bar.open = True
                page.update()
                page.client_storage.remove("key")
                next_page("/signup")
            else:
                page.snack_bar = SnackBar(
                    content=Row([Text(f"Ошибка при удалении аккаунта {self.name})", color='white')],
                                alignment=MainAxisAlignment.CENTER),
                    bgcolor=Colors.RED,
                )
                page.snack_bar.open = True
                page.update()


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
            Menu_content.offset = transform.Offset(0, 0) if Menu_content.offset == transform.Offset(-2,
                                                                                                    0) else transform.Offset(
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

            # Обновление иконок в top_rectangle
            Cart_button.icon_color = colors["icon_color"]
            Profile_button.icon_color = colors["icon_color"]

            # обновление меню
            Menu_but.icon_color = colors["icon_color"]

            Menu_content.controls[0].bgcolor = update_colors()['bgcolor']
            Menu_content.controls[0].border = update_colors()['border_color']
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

            page.update()

        def toggle_mode(e):
            page.close(page.update_status)
            state = self.get_shop_state(self.role)
            if state == False:
                text = Text("Обычный", size=15)
                row_up_btn.controls = [round, text]
                thumb_container.bgcolor = Colors.RED
                result = self.update_shop_state(self.id)
                if isinstance(result, bool):
                    page.snack_bar = SnackBar(
                        content=Row([Text(f"Сайт работает в ОБЫЧНОМ режиме!", color='white')],
                                    alignment=MainAxisAlignment.CENTER),
                        bgcolor=colors.RED,
                    )
                    page.snack_bar.open = True
                else:
                    page.snack_bar = SnackBar(
                        content=Row([Text(f"{result}", color='white')],
                                    alignment=MainAxisAlignment.CENTER),
                        bgcolor=colors.RED,
                    )
                    page.snack_bar.open = True
                page.update()

            elif state == True:
                text = Text("Особый", size=15)
                row_up_btn.controls = [text, round]
                thumb_container.bgcolor = Colors.GREEN
                result = self.update_shop_state(self.id)
                if isinstance(result, bool):
                    page.snack_bar = SnackBar(
                        content=Row([Text(f"Сайт работает в ОСОБОМ режиме!", color='white')],
                                    alignment=MainAxisAlignment.CENTER),
                        bgcolor=colors.GREEN,

                    )
                    page.snack_bar.open = True
                    page.update()
                else:
                    page.snack_bar = SnackBar(
                        content=Row([Text(f"{result}", color='white')],
                                    alignment=MainAxisAlignment.CENTER),
                        bgcolor=colors.RED,
                    )
                    page.snack_bar.open = True
                    page.update()
            else:
                thumb_container.alignment = alignment.center_right
                thumb_container.bgcolor = Colors.GREEN
                page.snack_bar = SnackBar(
                    content=Row([Text(f"{state}", color='white')],
                                alignment=MainAxisAlignment.CENTER),
                    bgcolor=colors.GREEN,

                )
                page.snack_bar.open = True
                page.update()
                self.LOG_OUT(self.key, self.id)
                next_page("/login")


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
                              on_click=animate_menu)
        icon_but = IconButton(icon=icons.SUNNY, on_click=style_revert, icon_color=update_colors()["icon_color"],
                              icon_size=update_size()['icon_rectangle_size'])
        Cart_button = IconButton(icon=icons.SHOPPING_CART, icon_color=update_colors()["icon_color"],
                                 icon_size=update_size()['icon_rectangle_size'],
                                 on_click=lambda e: cart_muve(e)
                                 )
        Profile_button = IconButton(icon=icons.PERSON, icon_color=update_colors()["icon_color"],
                                    icon_size=update_size()['icon_rectangle_size'])
        log_out_btn = IconButton(icon=icons.LOGOUT, on_click=lambda e: dialog_window("logout"),
                                 icon_color=Colors.GREEN, icon_size=update_size()['icon_rectangle_size'])
        if self.role == "admin":
            delete_acc = IconButton(icon=Icons.SETTINGS, on_click=lambda e: dialog_window("settings"), icon_size=update_size()['icon_rectangle_size'], icon_color=Colors.RED)
        else:
            delete_acc = IconButton(icon=Icons.DELETE, on_click=lambda e: dialog_window("delete"), icon_size=update_size()['icon_rectangle_size'], icon_color=Colors.RED)

        round = Container(
            width=25,
            height=20,
            bgcolor=colors.WHITE,
            border_radius=12.5,
        )

        text = Text("Обычный", size=15) if self.get_shop_state(self.role) else Text("Особый", size=15)

        # Контейнер для переключателя
        row_up_btn = Row(
            controls=[round, text] if self.get_shop_state(self.role) else [text, round],
            alignment=MainAxisAlignment.SPACE_AROUND,
            vertical_alignment=CrossAxisAlignment.CENTER,
        )

        thumb_container = Container(
            width=100,
            height=25,
            bgcolor=Colors.RED if self.get_shop_state(self.role) else Colors.GREEN,
            border_radius=20,
            content=row_up_btn,
            on_click=lambda e: page.open(page.update_status),
            visible=False if self.role != "admin" else True,
        )

        top_rectangle = Container(
            content=Row(
                [
                    Menu_but,
                    Container(content=thumb_container, alignment=Alignment(0.1, 0), expand=True),
                    Row(
                        [icon_but, Cart_button, log_out_btn, delete_acc],
                        alignment=MainAxisAlignment.END,
                        spacing=10,
                    ),
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
        )

        first_part = Column(
            [
                top_rectangle,
            ]
        )

        """Нижняя часть"""
        if self.photo == "None":
            photo_container = Container(
                ref=photo_display,
                content=Icon(Icons.PERSON, size=100, color=Colors.GREY),
                width=200,
                height=200,
                bgcolor=Colors.GREY_300,
                alignment=alignment.center,
                border_radius=10,
            )
        else:
            photo_container = Container(
                ref=photo_display,
                image_src_base64=self.photo,
                image_fit=ImageFit.CONTAIN,
                width=200,
                height=200,
                bgcolor=Colors.GREY_300,
                alignment=alignment.center,
                border_radius=10,
            )

        password_but = ElevatedButton("Сменить пароль", on_click=lambda e: dialog_window("password"))
        phone_but = ElevatedButton("Сменить номер", on_click=lambda e: show_url_input("phone"))
        photo_but = ElevatedButton("Сменить фото", on_click=lambda e: show_url_input("photo"))
        close_but = ElevatedButton("Отмена", on_click=cancel_action)
        submit_but = ElevatedButton("Подтвердить", on_click=action_button)
        phone_text = Text(f"Телефон: {self.number}", size=16)

        profile_page = Column(
            [
                Text("Ваши данные", size=30),
                Divider(),

                # Квадратное окно для фотографии
                photo_container,

                # Личная информация пользователя
                Column(
                    ref=user_info_display,
                    controls=[
                        Text(f"Логин: {self.name}", size=16),
                        phone_text,
                    ],
                ),

                # Кнопки управления профилем
                Divider(),
                Text("Управление профилем:", size=18),
                Row(
                    [
                        photo_but,
                        phone_but,
                        password_but,
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
            ],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
        )
        url_input_field = TextField(width=400)

        url_input_container = Container(
            visible=False,
            content=Column(
                controls=[
                    # Поле для ввода URL
                    Container(
                        content=url_input_field,
                        alignment=Alignment(0, 0),
                    ),
                    Row(
                        controls=[
                            submit_but,
                            close_but,
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
        )

        dlg_password = AlertDialog(
            modal=True,
            content=Text("Вы действительно хотите сменить пароль!", size=20),
            actions=[
                TextButton("Да", on_click=lambda e: show_url_input("password")),
                TextButton("Нет", on_click=lambda e: page.close(dlg_password)),
            ],
            actions_alignment=MainAxisAlignment.END,
        )

        dlg_delete = AlertDialog(
            modal=True,
            content=Text("Вы действительно хотите удалить аккаунт!", size=20),
            actions=[
                TextButton("Да", on_click=lambda e: delete_account(e)),
                TextButton("Нет", on_click=lambda e: page.close(dlg_delete)),
            ],
            actions_alignment=MainAxisAlignment.END,
        )

        dlg_logout = AlertDialog(
            modal=True,
            content=Text("Вы действительно хотите выйти из аккаунта!", size=20),
            actions=[
                TextButton("Да", on_click=lambda e: log_out(e)),
                TextButton("Нет", on_click=lambda e: page.close(dlg_logout)),
            ],
            actions_alignment=MainAxisAlignment.END,
        )
        page.update_status = AlertDialog(
            modal=True,
            content=Text("Переключить режим?", size=20),
            actions=[
                TextButton("Да", on_click=lambda e: toggle_mode(e)),
                TextButton("Нет", on_click=lambda e: page.close(dlg_logout)),
            ],
            actions_alignment=MainAxisAlignment.END,
        )

        """соединение всех элементов страницы"""
        return View("/profile", controls=[
            Stack([
                Column(
                    controls=[
                        first_part,
                        profile_page,
                        url_input_container,
                    ]
                ),
                Menu_content,
            ]
            ),
        ]
                    )


"""
page.snack_bar = SnackBar(
                    content=Row([Text("Вы успешно вошли!", color='white')],
                                   alignment=MainAxisAlignment.CENTER),
                    bgcolor=colors.GREEN,

                )
page.snack_bar.open = True
"""

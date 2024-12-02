import flet as ft
from flet_route import Params, Basket
import base64
import io
import requests
from functools import lru_cache


class SignupPage:
    @lru_cache
    def get_image(self, name, style=None):
        if style:
            request = requests.get(
                f"http://127.0.0.1:8000/images/{style}/{name}.png")
            image = io.BytesIO(request.content)
            base_64_image = base64.b64encode(image.read()).decode()
            return base_64_image
        else:
            request = requests.get(
                f"http://127.0.0.1:8000/images/{name}.jpg")
            image = io.BytesIO(request.content)
            base_64_image = base64.b64encode(image.read()).decode()
            return base_64_image

    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.theme_mode = ft.ThemeMode.LIGHT
        name = ft.Ref[ft.TextField]()
        phone_number = ft.Ref[ft.TextField]()
        password = ft.Ref[ft.TextField]()
        re_enter_password = ft.Ref[ft.TextField]()
        page.theme_mode = ft.ThemeMode.DARK
        back_image = self.get_image("Dark")

        def btn_click(e):
            if not name.current.value:
                page.snack_bar = ft.SnackBar(
                    content=ft.Row([
                        ft.Text('Введите имя!', color='white')
                    ], alignment=ft.MainAxisAlignment.CENTER
                    ),
                    bgcolor=ft.colors.RED,
                )
                page.snack_bar.open = True
                name.current.focus()
                page.update()
                return
            if not phone_number.current.value:
                page.snack_bar = ft.SnackBar(
                    content=ft.Row([
                        ft.Text('Введите номер телефона!', color='white')
                    ], alignment=ft.MainAxisAlignment.CENTER
                    ),
                    bgcolor=ft.colors.RED,
                )
                page.snack_bar.open = True
                phone_number.current.focus()
                page.update()
                return
            else:
                try:
                    if isinstance(int(phone_number.current.value), int):
                        phone_number.current.focus()
                        page.update()
                        pass
                    else:
                        if not (phone_number.current.value[0] == "+" and isinstance(int(phone_number.current.value[1:]),
                                                                                    int)):
                            page.snack_bar = ft.SnackBar(
                                content=ft.Row([
                                    ft.Text('Некоректный символ в номере!', color='white')
                                ], alignment=ft.MainAxisAlignment.CENTER
                                ),
                                bgcolor=ft.colors.RED,
                            )
                            page.snack_bar.open = True
                            page.update()
                            return
                except Exception:
                    page.snack_bar = ft.SnackBar(
                        content=ft.Row([
                            ft.Text('Некоректный символ в номере!', color='white')
                        ], alignment=ft.MainAxisAlignment.CENTER
                        ),
                        bgcolor=ft.colors.RED,
                    )
                    page.snack_bar.open = True
                    phone_number.current.focus()
                    page.update()
                    return
            if not password.current.value:
                page.snack_bar = ft.SnackBar(
                    content=ft.Row([
                        ft.Text('Введите пароль!', color='white')
                    ], alignment=ft.MainAxisAlignment.CENTER
                    ),
                    bgcolor=ft.colors.RED,
                )
                page.snack_bar.open = True
                password.current.focus()
                page.update()
                return
            if not re_enter_password.current.value:
                page.snack_bar = ft.SnackBar(
                    content=ft.Row([
                        ft.Text('Повторно введите пароль!', color='white')
                    ], alignment=ft.MainAxisAlignment.CENTER
                    ),
                    bgcolor=ft.colors.RED,
                )
                page.snack_bar.open = True
                re_enter_password.current.focus()
                page.update()
                return

            responce = requests.post('http://127.0.0.1:8000/register', json={
                "username": name.current.value,
                "password": password.current.value,
                "phone_number": str(phone_number.current.value),
            })

            if responce.text[1:-1] == "Пользователь успешно зарегистрирован":
                page.snack_bar = ft.SnackBar(
                    content=ft.Row([
                        ft.Text('Вы успешно зарегестрировались!', color='white')
                    ], alignment=ft.MainAxisAlignment.CENTER
                    ),
                    bgcolor=ft.colors.GREEN,
                )
                page.snack_bar.open = True
                page.go('/main')
            else:
                page.snack_bar = ft.SnackBar(
                    content=ft.Row([
                        ft.Text(f"{responce.text[1:-1]}", color='white')
                    ], alignment=ft.MainAxisAlignment.CENTER
                    ),
                    bgcolor=ft.colors.RED,
                )
                page.snack_bar.open = True
            name.current.value = ""
            phone_number.current.value = ""
            password.current.value = ""
            re_enter_password.current.value = ""
            # self.page.update()
            name.current.focus()

        # Списки изображений для светлой и тёмной темы
        instruments_light = [
            self.get_image(r"drum_light", "LIGHT"),
            self.get_image(r"electro_light", "LIGHT"),
            self.get_image(r"fleit_light", "LIGHT"),
            self.get_image(r"guitar_light", "LIGHT"),
            self.get_image(r"piano_light", "LIGHT"),
            self.get_image(r"pick_light", "LIGHT"),
        ]
        instruments_dark = [
            self.get_image(r"drum_dark", "DARK"),
            self.get_image(r"electro_dark", "DARK"),
            self.get_image(r"fleit_dark", "DARK"),
            self.get_image(r"guitar_dark", "DARK"),
            self.get_image(r"piano_dark", "DARK"),
            self.get_image(r"pick_dark", "DARK"),
        ]

        def update_images():
            controls = []
            instruments = instruments_dark if page.theme_mode == ft.ThemeMode.DARK else instruments_light
            rows = 20
            cols = 10

            for row in range(rows):
                row_controls = []
                for col in range(cols):
                    if (row + col) % 2 == 0:  # Чередуем размещение иконок
                        instrument_image = instruments[(row * cols + col) % len(instruments)]
                        row_controls.append(
                            ft.Image(src="data:image/png;base64," + instrument_image, width=50, height=50,
                                     fit=ft.ImageFit.CONTAIN))
                    else:
                        row_controls.append(ft.Container(width=50, height=50))
                controls.append(ft.Row(row_controls, alignment=ft.MainAxisAlignment.CENTER))

            page.controls.clear()
            return ft.Column(controls, alignment=ft.MainAxisAlignment.CENTER)

        left_back = update_images()

        main_Container = ft.Row([
            ft.Column([
                ft.Container(ft.Row([
                    ft.Column(
                        [
                            ft.Text("Регистрация", size=30, color=ft.colors.BLUE),
                            ft.TextField(ref=name,
                                         label="Имя",
                                         autofocus=True,
                                         # bgcolor=ft.colors.BLACK,  # Цвет фона
                                         cursor_color=ft.colors.BLUE,  # Цвет курсора
                                         width=300,
                                         border_radius=12,  # Скругление углов (можно настроить радиус)
                                         text_style=ft.TextStyle(color=ft.colors.BLUE),
                                         border_color=ft.colors.BLUE,
                                         ),

                            ft.TextField(ref=phone_number,
                                         label="Номер телефона",
                                         width=300,
                                         # bgcolor=ft.colors.BLACK,
                                         cursor_color=ft.colors.BLUE,
                                         border_radius=12,
                                         text_style=ft.TextStyle(color=ft.colors.BLUE),
                                         border_color=ft.colors.BLUE,
                                         ),
                            ft.TextField(ref=password,
                                         label="Пароль",
                                         password=True,
                                         can_reveal_password=True,
                                         # bgcolor=ft.colors.BLACK,
                                         cursor_color=ft.colors.BLUE,
                                         border_radius=12,
                                         width=300,
                                         text_style=ft.TextStyle(color=ft.colors.BLUE),
                                         border_color=ft.colors.BLUE,
                                         ),
                            ft.TextField(
                                ref=re_enter_password,
                                label="Введите пароль ещё раз!",
                                password=True,
                                can_reveal_password=True,
                                # bgcolor=ft.colors.BLACK,
                                cursor_color=ft.colors.BLUE,
                                border_radius=12,
                                width=300,
                                text_style=ft.TextStyle(color=ft.colors.BLUE),
                                border_color=ft.colors.BLUE,
                            ),
                            ft.ElevatedButton("Зарегистрироваться!",
                                              on_click=btn_click,
                                              width=200,
                                              style=ft.ButtonStyle(
                                                  surface_tint_color=ft.colors.BLUE,  # Цвет фона при наведении
                                                  side=ft.BorderSide(color=ft.colors.BLUE, width=1),  # Синяя обводка
                                                  shape=ft.RoundedRectangleBorder(
                                                      radius=12  # Радиус скругления углов
                                                  ),
                                              ),
                                              ),
                            ft.TextButton(text="Войти!",
                                          style=ft.ButtonStyle(
                                              color=ft.colors.BLUE,
                                          ),
                                          on_click=lambda _: page.go('/')),

                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                    )

                ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True
                ),
                    height=500,
                    width=400,
                    border=ft.border.all(1, ft.colors.BLUE),
                    border_radius=10,
                    padding=20,
                    blur=ft.Blur(10, 10),
                )
            ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ],
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True
        )

        main_con = ft.Row([
            ft.Container(expand=2, width=500, alignment=ft.alignment.top_left,
                         content=left_back),
            ft.Container(image_src_base64=back_image, expand=4, image_fit=ft.ImageFit.COVER, border_radius=12)
        ], expand=True)

        def style_revert(e):
            nonlocal back_image
            if page.theme_mode == ft.ThemeMode.DARK:
                page.theme_mode = ft.ThemeMode.LIGHT
                back_image = self.get_image("Light")
                icon_but.icon = ft.icons.DARK_MODE_OUTLINED
            else:
                page.theme_mode = ft.ThemeMode.DARK
                back_image = self.get_image("Dark")
                icon_but.icon = ft.icons.SUNNY

            main_con.controls[0].content = update_images()
            main_con.controls[1].image_src_base64 = back_image
            page.update()

        icon_but = ft.IconButton(icon=ft.icons.SUNNY, on_click=style_revert)
        style_mod = ft.Row([ft.Container(icon_but,
                                         alignment=ft.Alignment(0, -1))],
                           expand=True,
                           alignment=ft.MainAxisAlignment.END)

        content = ft.Stack(controls=[main_con, main_Container, style_mod], expand=True)  # , main_Container, style_mod

        return ft.View("/", controls=[content])

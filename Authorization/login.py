import flet as ft
from flet_route import Params, Basket
import requests
from help_function.Navigation import Navigation
import json

class LoginPage(Navigation):
    def __init__(self):
        super().__init__()


    def view(self, page: ft.Page, params: Params, basket: Basket):
        name = ft.Ref[ft.TextField]()
        password = ft.Ref[ft.TextField]()
        page.theme_mode = ft.ThemeMode.DARK
        back_image = self.get_image("Dark", "jpg")


        def btn_click(e):
            if not name.current.value:
                page.snack_bar = ft.SnackBar(
                    content=ft.Row([ft.Text("Введите имя!", color='white')], alignment=ft.MainAxisAlignment.CENTER),
                    bgcolor=ft.colors.RED,
                )
                page.snack_bar.open = True
                name.current.focus()
                page.update()
                return
            if not password.current.value:
                page.snack_bar = ft.SnackBar(
                    content=ft.Row([ft.Text("Введите пароль!", color='white')], alignment=ft.MainAxisAlignment.CENTER),
                    bgcolor=ft.colors.RED,
                )
                page.snack_bar.open = True
                password.current.focus()
                page.update()
                return
            responce = requests.post('http://localhost:30000/login', json={
                "username": name.current.value,
                "password": password.current.value
            })
            responce = json.loads(responce.content.decode('utf-8'))
            if responce[0] == "key":
                page.snack_bar = ft.SnackBar(
                    content=ft.Row([ft.Text("Вы успешно вошли!", color='white')],
                                   alignment=ft.MainAxisAlignment.CENTER),
                    bgcolor=ft.colors.GREEN,

                )
                page.client_storage.set("key", [responce[1], name.current.value])
                page.snack_bar.open = True
                next_page('/profile')
            else:
                page.snack_bar = ft.SnackBar(
                    content=ft.Row([ft.Text(f"{responce}", color='white')],
                                   alignment=ft.MainAxisAlignment.CENTER),
                    bgcolor=ft.colors.RED,
                )
                page.snack_bar.open = True
            name.current.value = ""
            password.current.value = ""
            page.update()
            name.current.focus()

        def next_page(muve):
            page.theme_mode = ft.ThemeMode.DARK
            page.client_storage.set("muve", muve)
            page.go("/loading")

        # Списки изображений для светлой и тёмной темы
        instruments_light = [
            self.get_image(r"drum_light", "png", "LIGHT"),
            self.get_image(r"electro_light", "png", "LIGHT"),
            self.get_image(r"fleit_light", "png", "LIGHT"),
            self.get_image(r"guitar_light", "png", "LIGHT"),
            self.get_image(r"piano_light", "png", "LIGHT"),
            self.get_image(r"pick_light", "png", "LIGHT"),
        ]
        instruments_dark = [
            self.get_image(r"drum_dark", "png", "DARK"),
            self.get_image(r"electro_dark", "png", "DARK"),
            self.get_image(r"fleit_dark", "png", "DARK"),
            self.get_image(r"guitar_dark", "png", "DARK"),
            self.get_image(r"piano_dark", "png", "DARK"),
            self.get_image(r"pick_dark", "png", "DARK"),
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

        # Описание авторизационной части
        main_Container = ft.Row([
            ft.Column([
                ft.Container(ft.Row([
                    ft.Column([
                        ft.Text("Авторизация", size=30, color=ft.colors.BLUE),
                        ft.TextField(ref=name, label="Имя", autofocus=True, cursor_color=ft.colors.BLUE, width=300,
                                     border_radius=12, text_style=ft.TextStyle(color=ft.colors.BLUE),
                                     border_color=ft.colors.BLUE),
                        ft.TextField(ref=password, label="Пароль", password=True, can_reveal_password=True,
                                     cursor_color=ft.colors.BLUE, border_radius=12, width=300,
                                     text_style=ft.TextStyle(color=ft.colors.BLUE), border_color=ft.colors.BLUE),
                        ft.ElevatedButton("Войти!", on_click=btn_click, width=200,
                                          style=ft.ButtonStyle(surface_tint_color=ft.colors.BLUE,
                                                               side=ft.BorderSide(color=ft.colors.BLUE, width=1),
                                                               shape=ft.RoundedRectangleBorder(radius=12))),
                        ft.TextButton(text="Зарегистрироваться", style=ft.ButtonStyle(color=ft.colors.BLUE),
                                      on_click=lambda _: next_page('/signup')),
                        ft.TextButton(text="на главную", style=ft.ButtonStyle(color=ft.colors.BLUE),
                                      on_click=lambda _: next_page('/')),
                    ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                ], alignment=ft.MainAxisAlignment.CENTER, expand=True), height=500, width=400,
                    border=ft.border.all(1, ft.colors.BLUE), border_radius=10, padding=20, blur=ft.Blur(10, 10))
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        ], alignment=ft.MainAxisAlignment.CENTER, expand=True)

        main_con = ft.Row([
            ft.Container(expand=2, width=500, alignment=ft.alignment.top_left,
                         content=left_back),
            ft.Container(image_src_base64=back_image, expand=4, image_fit=ft.ImageFit.COVER, border_radius=12)
        ], expand=True)

        def style_revert(e):
            nonlocal back_image
            if page.theme_mode == ft.ThemeMode.DARK:
                page.theme_mode = ft.ThemeMode.LIGHT
                back_image = self.get_image("Light", "jpg")
                icon_but.icon = ft.icons.DARK_MODE_OUTLINED
            else:
                page.theme_mode = ft.ThemeMode.DARK
                back_image = self.get_image("Dark", "jpg")
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

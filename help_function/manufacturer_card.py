import flet as ft
from flet.core.colors import Colors

from help_function.Admin_control import AdminDEF
from help_function.Navigation import Navigation


class ManufacturerCard(Navigation):
    def __init__(self, page, id, name, photo, items_count, admin: AdminDEF):
        self.page = page
        self.id = id
        self.name = name
        self.photo = photo
        self.items_count = items_count
        self.admin_panel = admin
        super().__init__()

    def build(self):

        def next_page(muve):
            self.page.client_storage.set("muve", muve)
            self.page.go("/loading")

        def delete_manufacturer(e):
            if self.admin_panel.delete_manufacturer(self.id):
                self.page.snack_bar = ft.SnackBar(
                    content=ft.Row([ft.Text(f"Производитель с id {self.id} удалён!", color='white')],
                                   alignment=ft.MainAxisAlignment.CENTER),
                    bgcolor=ft.colors.GREEN,

                )
                self.page.snack_bar.open = True
                self.page.update()
                next_page("/settings_admin")
            else:
                self.page.snack_bar = ft.SnackBar(
                    content=ft.Row([ft.Text("Что-то пошло не так!", color='white')],
                                   alignment=ft.MainAxisAlignment.CENTER),
                    bgcolor=ft.colors.RED,

                )
                self.page.snack_bar.open = True
                self.page.update()

        def update_manufacturer(e):
            name = name_field.value
            if self.admin_panel.update_manufacturer(manufacture_id=self.id, manufacturer_name=name):
                self.page.snack_bar = ft.SnackBar(
                    content=ft.Row([ft.Text(f"Производитель с id {self.id} изменён", color='white')],
                                   alignment=ft.MainAxisAlignment.CENTER),
                    bgcolor=ft.colors.GREEN,

                )
                self.page.snack_bar.open = True
                self.page.update()
                next_page("/settings_admin")
            else:
                self.page.snack_bar = ft.SnackBar(
                    content=ft.Row([ft.Text("Что-то пошло не так!", color='white')],
                                   alignment=ft.MainAxisAlignment.CENTER),
                    bgcolor=ft.colors.RED,

                )
                self.page.snack_bar.open = True
                self.page.update()

        cancel_button = ft.ElevatedButton(
            text="Удалить",
            # on_click=cancel_order,
            bgcolor=ft.colors.RED,
            color="white",
            visible=True,
            on_click=delete_manufacturer,
        )

        photo_button = ft.ElevatedButton(text="Изменить", on_click=update_manufacturer,)

        name_field = ft.TextField(value=self.name, width=100, text_style=ft.TextStyle(color=ft.Colors.BLUE))

        # Полоска заказа
        order_strip = ft.Container(
            content=ft.Row(
                [
                    ft.Text(f"id: {self.id}", size=16, weight="bold", color=Colors.BLUE),
                    ft.Text(f"name:", size=16, weight="bold", color=Colors.BLUE),
                    name_field,
                    photo_button,
                    ft.Text(f"items_count: {self.items_count}", size=16, weight="bold", color=Colors.BLUE),
                    cancel_button,
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                spacing=10,
            ),
            padding=10,
            bgcolor=ft.colors.WHITE,
            border_radius=5,
            margin=ft.margin.all(10),
            border=ft.border.all(2),
        )
        return order_strip

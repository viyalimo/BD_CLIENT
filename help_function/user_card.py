import flet as ft
from flet.core.colors import Colors

from help_function.Admin_control import AdminDEF
from help_function.Navigation import Navigation


class UserCard(Navigation):
    def __init__(self, page, user_id, name, password, number, role, photo, token, admin_panel: AdminDEF):
        self.page = page
        self.user_id = user_id
        self.name = name
        self.password = password
        self.number = number
        self.role = role
        self.photo = photo
        self.token = token
        self.admin_panel = admin_panel
        super().__init__()

    def build(self):

        def next_page(muve):
            self.page.client_storage.set("muve", muve)
            self.page.go("/loading")

        def block_user(e):
            self.admin_panel.block_account(self.user_id)
            self.page.snack_bar = ft.SnackBar(
                content=ft.Row([ft.Text(f"Пользователь {self.name} заблокирован!", color='white')],
                            alignment=ft.MainAxisAlignment.CENTER),
                bgcolor=ft.colors.GREEN,

            )
            self.page.snack_bar.open = True
            self.page.update()
            next_page("/settings_admin")

        def delete_account(e):
            self.admin_panel.delete_account(self.user_id)
            self.page.snack_bar = ft.SnackBar(
                content=ft.Row([ft.Text(f"Пользователь {self.name} удалён!", color='white')],
                               alignment=ft.MainAxisAlignment.CENTER),
                bgcolor=ft.colors.GREEN,

            )
            self.page.snack_bar.open = True
            self.page.update()
            next_page("/settings_admin")

        cancel_button = ft.ElevatedButton(
            text="Удалить",
            # on_click=cancel_order,
            bgcolor=ft.colors.RED,
            color="white",
            visible=True,
            on_click=lambda e: delete_account(e),
            )

        photo_button = ft.ElevatedButton(text="фото")

        block_btn = ft.ElevatedButton("Заблокировать", on_click=lambda e: block_user(e))

        # Полоска заказа
        order_strip = ft.Container(
            content=ft.Row(
                [
                    ft.Text(f"id: {self.user_id}", size=16, weight="bold", color=Colors.BLUE),
                    ft.Text(f"name: {self.name}", size=16, weight="bold", color=Colors.BLUE),
                    ft.Text(f"phone: {self.number}", size=16, weight="bold", color=Colors.BLUE),
                    ft.Text(f"role: {self.role}", size=16, weight="bold", color=Colors.BLUE),
                    ft.Text(f"token: {self.token}", size=16, weight="bold", color=Colors.BLUE),
                    block_btn,
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

import flet as ft
from flet.core.colors import Colors
from help_function.Navigation import Navigation


class CartCard(Navigation):
    def __init__(self, page, id, cart_id, product_id, total, buy):
        self.page = page
        self.id = id
        self.cart_id = cart_id
        self.product_id = product_id
        self.total = total
        self.buy = buy
        super().__init__()

    def build(self):


        cancel_button = ft.ElevatedButton(
            text="Настройки",
            # on_click=cancel_order,
            bgcolor=ft.colors.RED,
            color="white",
            visible=True)


        # Полоска заказа
        order_strip = ft.Container(
            content=ft.Row(
                [
                    ft.Text(f"id: {self.id}", size=16, weight="bold", color=Colors.BLUE),
                    ft.Text(f"cart_id: {self.cart_id}", size=16, weight="bold", color=Colors.BLUE),
                    ft.Text(f"product_id: {self.product_id}", size=16, weight="bold", color=Colors.BLUE),
                    ft.Text(f"total: {self.total}", size=16, weight="bold", color=Colors.BLUE),
                    ft.Text(f"оплачен: {self.buy}", size=16, weight="bold", color=Colors.BLUE),
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

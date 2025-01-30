import flet as ft
from flet.core.colors import Colors
from help_function.Navigation import Navigation


class OrderCard(Navigation):
    def __init__(self, page, id, product_id, user_id, order_date, delivery_date, price, status):
        self.page = page
        self.id = id
        self.product_id = product_id
        self.user_id = user_id
        self.order_date = order_date
        self.delivery_date = delivery_date
        self.price = price
        self.status = status
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
                    ft.Text(f"id товара: {self.product_id}", size=16, weight="bold", color=Colors.BLUE),
                    ft.Text(f"id клиента: {self.user_id}", size=16, weight="bold", color=Colors.BLUE),
                    ft.Text(f"заказан: {self.order_date}", size=16, weight="bold", color=Colors.BLUE),
                    ft.Text(f"дата доставки: {self.delivery_date}", size=16, weight="bold", color=Colors.BLUE),
                    ft.Text(f"цена: {self.price}", size=16, weight="bold", color=Colors.BLUE),
                    ft.Text(f"статус: {self.status}", size=16, weight="bold", color=Colors.BLUE),


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

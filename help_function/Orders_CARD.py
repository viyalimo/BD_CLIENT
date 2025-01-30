import flet as ft
from flet.core.colors import Colors
from help_function.Navigation import Navigation


class OrderCard(Navigation):
    def __init__(self, page, order_id, product_id, status, order_date, delivery_date, user_id, cancel_callback=None):
        self.order_id = order_id
        self.product_id = product_id
        self.status = status
        self.order_date = order_date
        self.delivery_date = delivery_date
        self.cancel_callback = cancel_callback
        self.product_name = self.get_product_id(int(product_id))[1]
        self.price = self.get_product_id(int(product_id))[4]
        self.user_id = user_id
        super().__init__()

    def build(self):
        # Метка статуса
        status_label = ft.Text(f"Статус: {self.status}", color=Colors.BLUE)

        # Функция для отмены заказа
        def cancel_order(e):
            if self.cancel_callback:
                self.cancel_callback(self.order_id)
            self.status = "canceled"
            status_label.value = f"Статус: {self.status}"
            status_label.color = "red"
            cancel_button.visible=False
            status_label.update()
            cancel_button.update()
            self.cancel_order(self.user_id, self.order_id)

        if self.cancel_callback == "c":
            status_label.color = "red"
            cancel_button = ft.ElevatedButton(
                text="Отменить заказ",
                on_click=cancel_order,
                bgcolor=ft.colors.RED,
                color="white",
                visible=False
            )
        elif self.cancel_callback == "d":
            status_label.color = "green"
            cancel_button = ft.ElevatedButton(
                text="Забрать заказ",
                bgcolor=ft.colors.GREEN,
                color="white",
                visible=False
            )
        else:
            cancel_button = ft.ElevatedButton(
                text="Отменить заказ",
                on_click=cancel_order,
                bgcolor=ft.colors.RED,
                color="white",
                visible=True
            )

        # Полоска заказа
        order_strip = ft.Container(
            content=ft.Row(
                [
                    ft.Text(f"Номер заказа {self.order_id}", size=16, weight="bold", color=Colors.BLUE),
                    ft.Text(f"Товар: {self.product_name}", color=Colors.BLUE),
                    ft.Text(f"Сумма: {self.price} руб.", color=Colors.BLUE),
                    ft.Text(f"Дата заказа: {self.order_date}", color=Colors.BLUE),
                    ft.Text(f"Дата доставки: {self.delivery_date}", color=Colors.BLUE),
                    status_label,
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


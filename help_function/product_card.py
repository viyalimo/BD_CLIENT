import flet as ft
from flet.core.colors import Colors

from help_function.Admin_control import AdminDEF
from help_function.Navigation import Navigation


class ProductCard(Navigation):
    def __init__(self, page, id, product_name, category, manufacturer_id,price,total_purchases,color,photo_base64, warehouse, admin_panel: AdminDEF):
        self.page = page
        self.id = id
        self.product_name = product_name
        self.category = category
        self.manufacturer_id = manufacturer_id
        self.price = price
        self.total_purchases = total_purchases
        self.color = color
        self.photo_base64 = photo_base64
        self.warehouse = warehouse
        self.admin_panel = admin_panel
        super().__init__()

    def build(self):
        def next_page(muve):
            self.page.client_storage.set("muve", muve)
            self.page.go("/loading")

        def delete_product(e):
            if self.admin_panel.delete_product(self.id):
                self.page.snack_bar = ft.SnackBar(
                    content=ft.Row([ft.Text(f"Товар с id {self.id} удалён!", color='white')],
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

        def update_product(e):
            name = product_fild.value
            category = category_fild.value
            manufacturer_id = manufacturer_fild.value
            price = price_fild.value
            color = color_fild.value
            warehouse = warehouse_fild.value
            if self.admin_panel.update_products(product_id=self.id, product_name=name, category=category, manufacturer_id=manufacturer_id, price=price,
                                             color=color, warehouse=warehouse):
                self.page.snack_bar = ft.SnackBar(
                    content=ft.Row([ft.Text(f"Товар с id {self.id} изменён", color='white')],
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
        on_click=lambda e: delete_product(e))

        photo_button = ft.ElevatedButton(text="фото")

        product_fild = ft.TextField(value=self.product_name, width=100, text_style=ft.TextStyle(color=ft.Colors.BLUE))
        category_fild = ft.TextField(value=self.category, width=100, text_style=ft.TextStyle(color=ft.Colors.BLUE))
        manufacturer_fild = ft.TextField(value=self.manufacturer_id, width=100, text_style=ft.TextStyle(color=ft.Colors.BLUE))
        price_fild = ft.TextField(value=self.price, width=100, text_style=ft.TextStyle(color=ft.Colors.BLUE))
        color_fild = ft.TextField(value=self.color, width=100, text_style=ft.TextStyle(color=ft.Colors.BLUE))
        warehouse_fild = ft.TextField(value=self.warehouse, width=100, text_style=ft.TextStyle(color=ft.Colors.BLUE))

        update_btn = ft.ElevatedButton("Изменить", on_click=lambda e: update_product(e))

        # Полоска заказа
        order_strip = ft.Container(
            content=ft.Row(
                [
                    ft.Text(f"id: {self.id}", size=16, weight="bold", color=Colors.BLUE),
                    ft.Text(f"имя:", size=16, weight="bold", color=Colors.BLUE),
                    product_fild,
                    ft.Text(f"категория:", size=16, weight="bold", color=Colors.BLUE),
                    category_fild,
                    ft.Text(f"id бренда:", size=16, weight="bold", color=Colors.BLUE),
                    manufacturer_fild,
                    ft.Text(f"цена:", size=16, weight="bold", color=Colors.BLUE),
                    price_fild,
                    ft.Text(f"покупателей: {self.total_purchases}", size=16, weight="bold", color=Colors.BLUE),
                    ft.Text(f"цвет:", size=16, weight="bold", color=Colors.BLUE),
                    color_fild,
                    ft.Text(f"на складе:", size=16, weight="bold", color=Colors.BLUE),
                    warehouse_fild,
                    update_btn,
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

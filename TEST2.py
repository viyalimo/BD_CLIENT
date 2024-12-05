import flet as ft

def main(page: ft.Page):
    # Функция для обработки событий изменения
    def handle_change(e):
        for i, destination in enumerate(drawer.controls):
            if isinstance(destination, ft.NavigationDrawerDestination) and destination.selected:
                print(f"Selected destination index: {i}, label: {destination.label}")

    # Функция для обработки закрытия
    def handle_dismissal(e):
        print("Drawer dismissed")

    # Создаем NavigationDrawer
    drawer = ft.NavigationDrawer(
        on_dismiss=handle_dismissal,
        on_change=handle_change,
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="Item 1",
                icon=ft.Icons.DOOR_BACK_DOOR_OUTLINED,
                selected_icon_content=ft.Icon(ft.Icons.DOOR_BACK_DOOR),
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.Icons.MAIL_OUTLINED),
                label="Item 2",
                selected_icon=ft.Icons.MAIL,
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.Icons.PHONE_OUTLINED),
                label="Item 3",
                selected_icon=ft.Icons.PHONE,
            ),
        ],
    )

    # Кнопка для открытия боковой панели
    open_drawer_button = ft.ElevatedButton(
        "Show drawer",
        on_click=lambda e: page.open(drawer)
    )

    # Добавляем элементы на страницу
    page.add(open_drawer_button)

# Запускаем приложение
ft.app(target=main)

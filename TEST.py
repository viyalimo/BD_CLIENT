
import flet as ft

def main(page: ft.Page):
    # Функция для обновления цветов прямоугольника и иконок
    def update_colors():
        if page.theme_mode == ft.ThemeMode.LIGHT:
            return {
                "bgcolor": ft.colors.WHITE,
                "border_color": ft.colors.BLACK,
                "icon_color": ft.colors.BLACK,
            }
        else:
            return {
                "bgcolor": ft.colors.BLACK,
                "border_color": ft.colors.BLUE,
                "icon_color": ft.colors.BLUE,
            }

    # Функция смены темы
    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT

        # Обновляем цвета
        colors = update_colors()
        top_rectangle.bgcolor = colors["bgcolor"]
        top_rectangle.border = ft.border.all(1, colors["border_color"])

        # Обновляем цвета иконок
        menu_button.icon_color = colors["icon_color"]
        theme_button.icon_color = colors["icon_color"]
        favorite_button.icon_color = colors["icon_color"]
        cart_button.icon_color = colors["icon_color"]
        profile_button.icon_color = colors["icon_color"]

        # Меняем иконку для кнопки темы
        theme_button.icon = (
            ft.icons.LIGHT_MODE
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.icons.DARK_MODE
        )

        page.update()

    # Начальные цвета
    colors = update_colors()

    # Иконки
    menu_button = ft.IconButton(icon=ft.icons.MENU, icon_color=colors["icon_color"])
    theme_button = ft.IconButton(
        icon=ft.icons.LIGHT_MODE
        if page.theme_mode == ft.ThemeMode.LIGHT
        else ft.icons.DARK_MODE,
        icon_color=colors["icon_color"],
        on_click=toggle_theme,
    )
    favorite_button = ft.IconButton(
        icon=ft.icons.FAVORITE, icon_color=colors["icon_color"]
    )
    cart_button = ft.IconButton(
        icon=ft.icons.SHOPPING_CART, icon_color=colors["icon_color"]
    )
    profile_button = ft.IconButton(
        icon=ft.icons.PERSON_2, icon_color=colors["icon_color"]
    )

    # Прямоугольник
    top_rectangle = ft.Container(
        content=ft.Row(
            [
                menu_button,  # Кнопка меню слева
                ft.Container(content=theme_button, alignment=ft.Alignment(0, 0), expand=True),  # Смена темы в центре
                ft.Row(
                    [
                        favorite_button,
                        cart_button,
                        profile_button,
                    ],
                    alignment=ft.MainAxisAlignment.END,
                    spacing=10,
                ),  # Остальные кнопки справа
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        height=50,
        bgcolor=colors["bgcolor"],  # Фон
        border=ft.border.all(1, colors["border_color"]),  # Граница
        border_radius=ft.border_radius.all(10),  # Скругление
    )

    # Основной контент
    page.add(
        ft.Stack(
            [
                top_rectangle,  # Верхний прямоугольник
            ],
            expand=True,
        )
    )


ft.app(target=main)

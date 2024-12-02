import flet as ft

def main(page: ft.Page):
    def search_action(e):
        print(f"Ищем: {search_field.value}")  # Выводим введённый текст
        search_field.value = ""  # Очищаем поле ввода
        page.update()  # Обновляем интерфейс

    def clear_action(e):
        search_field.value = ""  # Очищаем поле ввода
        page.update()

    def handle_change(e):
        # Показываем или скрываем крестик, в зависимости от наличия текста
        clear_button.visible = bool(search_field.value.strip())
        page.update()

    # Кнопка для очистки текста (крестик внутри поля)
    clear_button = ft.IconButton(
        icon=ft.icons.CLOSE,  # Иконка крестика
        icon_size=12,
        icon_color=ft.colors.BLACK,  # Цвет иконки
        on_click=clear_action,  # Очищаем поле при нажатии
        visible=False,  # Показываем только если в поле есть текст
    )

    # Поле ввода с крестиком внутри
    search_field = ft.TextField(
        hint_text="Введите запрос",  # Текст-подсказка
        expand=True,  # Растягиваем поле ввода
        height=50,  # Высота текстового поля
        bgcolor=ft.colors.WHITE,  # Белый фон для текстового поля
        color=ft.colors.BLACK,  # Цвет текста
        text_style=ft.TextStyle(size=16),  # Размер текста
        text_align=ft.TextAlign.LEFT,  # Выравнивание текста по левому краю
        on_change=handle_change,  # Слушаем изменения текста
        border_radius=15,
        suffix=clear_button,  # Крестик внутри поля ввода
    )

    # Кнопка поиска
    search_button = ft.IconButton(
        icon=ft.icons.SEARCH,  # Иконка лупы
        icon_color=ft.colors.BLACK,  # Цвет иконки
        on_click=search_action,  # Действие при нажатии
    )

    # Контейнер с полем ввода и кнопкой поиска
    search_bar = ft.Container(
        content=ft.Row(
            [
                search_field,  # Поле ввода с крестиком
                search_button,  # Кнопка поиска справа
            ],
            spacing=5,  # Расстояние между полем ввода и кнопкой
            alignment=ft.MainAxisAlignment.START,  # Выравнивание по левому краю
        ),
        padding=ft.padding.all(0),  # Убираем внешние отступы
    )

    # Основной контент страницы
    page.add(
        ft.Column(
            [
                ft.Text("Поисковая строка с кнопками", size=20, weight=ft.FontWeight.BOLD),
                search_bar,
            ],
            alignment=ft.MainAxisAlignment.START,
            expand=True,
        )
    )

ft.app(target=main)

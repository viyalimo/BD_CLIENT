import flet as ft


def main(page):
    # Список изображений для светлой и тёмной темы
    instruments_light = [
        r"C:\Users\user1387\PycharmProjects\BD_client\Image\LIGHT_ICON\drum_light.png",
        r"C:\Users\user1387\PycharmProjects\BD_client\Image\LIGHT_ICON\electro_light.png",
        r"C:\Users\user1387\PycharmProjects\BD_client\Image\LIGHT_ICON\fleit_light.png",
        r"C:\Users\user1387\PycharmProjects\BD_client\Image\LIGHT_ICON\guitar_light.png",
        r"C:\Users\user1387\PycharmProjects\BD_client\Image\LIGHT_ICON\piano_light.png",
        r"C:\Users\user1387\PycharmProjects\BD_client\Image\LIGHT_ICON\pick_light.png",
    ]

    instruments_dark = [
        r"C:\Users\user1387\PycharmProjects\BD_client\Image\DARK_ICON\drum_dark.png",
        r"C:\Users\user1387\PycharmProjects\BD_client\Image\DARK_ICON\electro_dark.png",
        r"C:\Users\user1387\PycharmProjects\BD_client\Image\DARK_ICON\fleit_dark.png",
        r"C:\Users\user1387\PycharmProjects\BD_client\Image\DARK_ICON\guitar_dark.png",
        r"C:\Users\user1387\PycharmProjects\BD_client\Image\DARK_ICON\piano_dark.png",
        r"C:\Users\user1387\PycharmProjects\BD_client\Image\DARK_ICON\pick_dark.png",
    ]

    # Начальная тема - светлая
    current_theme = "light"

    def toggle_theme(e):
        nonlocal current_theme
        if current_theme == "light":
            current_theme = "dark"
            page.theme_mode = ft.ThemeMode.DARK  # Устанавливаем тёмную тему
        else:
            current_theme = "light"
            page.theme_mode = ft.ThemeMode.LIGHT  # Устанавливаем светлую тему
        update_images()  # Обновляем изображения при смене темы

    def update_images():
        # Инвертируем логику отображения изображений
        instruments = instruments_dark if current_theme == "dark" else instruments_light
        controls = []
        rows = 10  # Количество рядов
        cols = 10  # Количество колонок

        for row in range(rows):
            row_controls = []
            for col in range(cols):
                # Определяем, будет ли картинка на текущей позиции
                if (row + col) % 2 == 0:  # Шахматный порядок
                    instrument_image = instruments[(row * cols + col) % len(instruments)]  # Путь к изображению
                    row_controls.append(ft.Image(src=instrument_image, width=50, height=50, fit=ft.ImageFit.CONTAIN))
                else:
                    row_controls.append(ft.Container(width=50, height=50))  # Пустая ячейка
            controls.append(ft.Row(row_controls, alignment=ft.MainAxisAlignment.CENTER))

        # Очищаем страницу и добавляем кнопку и изображения
        page.controls.clear()
        page.add(theme_button)  # Добавляем кнопку
        page.add(ft.Column(controls, alignment=ft.MainAxisAlignment.CENTER))  # Добавляем изображения

    # Кнопка для переключения темы
    theme_button = ft.IconButton(ft.icons.SUNNY, on_click=toggle_theme)

    # Изначальная настройка страницы
    page.add(theme_button)  # Добавляем кнопку один раз при первом запуске
    update_images()  # Обновляем изображения для светлой темы


ft.app(target=main)

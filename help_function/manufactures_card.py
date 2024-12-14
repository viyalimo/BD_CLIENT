from flet import *
from help_function.Navigation import Navigation


class Manufactures_Card:
    def __init__(self, id: int, image: str, page: Page):
        self.container = None
        self.id = id
        self.image = image
        self.build_card()
        self.page = page

    def update_card_border(self, event):
        """
        Изменяет цвет границы карточки при наведении курсора.
        """
        if event.data == "true":  # Если курсор наведён
            self.container.border = border.all(4, colors.BLUE)  # Толщина и цвет границы при наведении
        else:  # Если курсор убран
            self.container.border = border.all(2, colors.BLACK)
        self.container.update()

    def build_card(self):
        def next_page(muve):
            self.page.theme_mode = ThemeMode.DARK
            self.page.client_storage.set("muve", muve)
            self.page.go("/loading")

        manufacturer_logo = self.image  # Логотип Base64

        # Создаем карточку производителя
        self.container = Container(
            content=Image(
                src_base64=manufacturer_logo,
                width=800,
                height=200,
                fit=ImageFit.COVER,
                border_radius=8
            ),
            width=800,
            height=200,
            alignment=alignment.center,
            border_radius=border_radius.all(10),
            border=border.all(2, colors.BLACK),  # Исходная граница
            on_hover=self.update_card_border,  # Обработка событий наведения
            on_click=lambda e: next_page(f'/manufacture/:{self.id}')
        )

        return self.container


# Точка входа для Flet
def main(page: Page):
    page.title = "Карточка производителя"
    page.theme_mode = ThemeMode.LIGHT

    # Получаем данные о производителях
    content = Navigation().get_all_manufacturers()
    print(content)

    # Создаем карточки для каждого производителя
    card_containers = []  # Список контейнеров для добавления на страницу
    for inf in content:
        id = inf[0]
        image = inf[2]

        # Создаем карточку
        card_builder = Manufactures_Card(id, image)
        card_containers.append(card_builder.container)  # Добавляем сам контейнер

    # Добавляем карточки на страницу в виде колонки
    page.add(Column(controls=card_containers, spacing=20, alignment=MainAxisAlignment.CENTER))


# Запуск приложения
if __name__ == "__main__":
    app(target=main, view=AppView.WEB_BROWSER)

import flet as ft
from help_function.router import Router


def main(page: ft.Page):

    LG = Router(page)


if __name__ == "__main__":
    ft.app(target=main,
           view=ft.AppView.WEB_BROWSER,
           # host="192.168.0.105",
           # port=40000
           )

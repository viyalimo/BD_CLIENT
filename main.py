import flet as ft
from router import Router


def main(page: ft.Page):

    LG = Router(page)


if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)

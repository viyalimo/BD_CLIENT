import flet as ft
from help_function.router import Router
import socket

def main(page: ft.Page):
    LG = Router(page)


if __name__ == "__main__":
    print(f"http://{str(socket.gethostbyname(socket.gethostname()))}:40000/")
    ft.app(target=main,
           view=ft.AppView.WEB_BROWSER,
           host=str(socket.gethostbyname(socket.gethostname())),
           port=40000
           )

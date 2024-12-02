import flet as ft
from flet_route import Routing, path
from Authorization.login import LoginPage
from Authorization.signup import SignupPage
from MAIN_PAGE.main_page import Main_page

class Router:
    def __init__(self, page: ft.Page):
        self.app_routes = [
            path(url='/', clear=False, view=Main_page().view),
            path(url='/login', clear=True, view=LoginPage().view),
            path(url='/signup', clear=False, view=SignupPage().view),
        ]
        self.page = page

        Routing(
            page=self.page,
            app_routes=self.app_routes,
        )
        self.page.go(self.page.route)

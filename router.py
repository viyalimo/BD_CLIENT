import flet as ft
from flet_route import Routing, path
from Authorization.login import LoginPage
from Authorization.signup import SignupPage
from MAIN_PAGE.main_page import Main_page

class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.app_routes = [
            path(url='/', clear=True, view=LoginPage().view),
            path(url='/signup', clear=False, view=SignupPage().view),
            #path(url='/main', clear=False, view=Main_page().view),
        ]

        Routing(
            page=self.page,
            app_routes=self.app_routes,
        )
        self.page.go(self.page.route)

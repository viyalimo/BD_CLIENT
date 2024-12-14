import flet as ft
from flet_route import Routing, path
from Authorization.login import LoginPage
from Authorization.signup import SignupPage
from MAIN_PAGE.main_page import Main_page
from Category.Page_category import CategoryPage
from Category.Update_CON import ImageApp
from Category.card_product import Card_product



class Router:
    def __init__(self, page: ft.Page):
        self.app_routes = [
            path(url='/', clear=True, view=Main_page().view),
            path(url='/login', clear=False, view=LoginPage().view),
            path(url='/signup', clear=False, view=SignupPage().view),
            path(url='/category/Струнные', clear=False, view=CategoryPage("Струнные").view),
            path(url='/category/Духовые', clear=False, view=CategoryPage("Духовые").view),
            path(url='/category/Ударные', clear=False, view=CategoryPage("Ударные").view),
            path(url='/category/Клавишные', clear=False, view=CategoryPage('Клавишные').view),
            path(url='/category/Электроинструменты', clear=False, view=CategoryPage('Электро инструменты').view),
            path(url='/category/Аксессуары', clear=False, view=CategoryPage('Аксессуары').view),
            path(url='/category/Производители', clear=False, view=CategoryPage('Производители').view),
            path(url='/loading', clear=False, view=ImageApp().view),
            path(url='/cardinfo/:id', clear=False, view=Card_product().view),
        ]
        self.page = page

        Routing(
            page=self.page,
            app_routes=self.app_routes,
        )
        self.page.go(self.page.route)

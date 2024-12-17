import flet as ft
from flet_route import Routing, path
from Authorization.login import LoginPage
from Authorization.signup import SignupPage
from View.main_page import Main_page
from View.Page_category import CategoryPage
from View.Update_CON import ImageApp
from View.card_product import Card_product
from View.manufacture_choose import ManufacturePage
from View.manufacture_product import ManufactureProd
from View.product_feed import ProductFeed
from View.User_profile import UserPage
from View.search_result import SimpleSearch

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
            path(url='/category/Аксессуары', clear=False, view=CategoryPage("Аксессуары").view),
            path(url='/Производители', clear=False, view=ManufacturePage().view),
            path(url='/loading', clear=False, view=ImageApp().view),
            path(url='/cardinfo/:id', clear=False, view=Card_product().view),
            path(url='/manufacture/:id', clear=False, view=ManufactureProd().view),
            path(url='/productsfeed', clear=False, view=ProductFeed().view),
            path(url='/profile', clear=False, view=UserPage().view),
            path(url='/search/:name', clear=False, view=SimpleSearch().view),
        ]
        self.page = page

        Routing(
            page=self.page,
            app_routes=self.app_routes,
        )
        self.page.go(self.page.route)
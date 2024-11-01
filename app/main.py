import flet as ft

from elements.menu_bar import MenuBar
from layouts.main_layout import PageLayout, MainLayout
from elements.hi_message import HiMessage
from elements.quote import Quote
from buttons.image_button import ImageButton
from layouts.form_layout import FormLayout
from pages.form_page import FormPage
from pages.sleep_form import SleepForm
from pages.tired_form import TiredForm
from pages.happy_form import HappyForm
from pages.day_form import DayForm
from pages.emoji_form import EmojiForm
from pages.stats import StatsPage
from styles.text import *
from backend.db import DatabaseController

class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.window.width = 375
        self.page.window.height = 812
        self.page.window.always_on_top = True

        self.page.bgcolor = "#0b0713"
        self.page.padding = 0
        self.page.spacing = 0

        self.init_backend()

        self.init_components()
        self.setup_event_handlers()
        self.page.go(self.page.route)

    def init_backend(self):
        print("Database connection open")
        self.db = DatabaseController()

    def init_components(self):
        self.home_button = ImageButton(
            image="ui/home.png",
            width=40,
            on_click=self.go_home
        )

        self.menubar = MenuBar(
            image="ui/menubar.png",
            calendar="ui/Calendar.png",
            calendar_onclick=self.calendar_onclick,
            chart="ui/BarChart.png",
            chart_onclick=self.chart_onclick,
            add="ui/Add.png",
            add_onclick=self.add_onclick
        )

        self.mainPage = PageLayout(
            content=ft.Column(
                controls=[
                    HiMessage(text_style=basic_header),
                    ft.Container(expand=True),
                    Quote(quote_style=quote_text, text_style=basic_text),
                ],
            ),
        )

        self.tiredForm = TiredForm(text_style1=wide_header, text_style2=form_text)
        self.sleepForm = SleepForm(text_style=form_text)
        self.happyForm = HappyForm(text_style1=wide_header, text_style2=form_text)
        self.dayForm = DayForm(text_style1=wide_header, text_style2=form_text)
        self.emojiForm = EmojiForm(
            text=ft.Text("Опиши свой день", style=wide_text, size=25),
            text2=ft.Row(
                controls=[
                    ft.Text("одной", style=wide_text, size=25),
                    ft.Text("эмоцией", style=wide_text, size=25, color="#c9a6ff")
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

        self.formPage = FormLayout(
            forms=[self.sleepForm, self.tiredForm, self.happyForm, self.dayForm, self.emojiForm],
            end_event=self.end_form
        )

        self.statsPage = StatsPage(home_button=self.home_button)

        self.mainLayout = MainLayout(page=self.mainPage, menu_bar=self.menubar)

        self.mainScreen = ft.Container(
            self.mainLayout,
            gradient=ft.LinearGradient(
                colors=["#000000", "#140C20"],
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
            ),
            expand=True,
            alignment=ft.alignment.top_left
        )

        self.formScreen = ft.Container(
            self.formPage,
            gradient=ft.LinearGradient(
                colors=["#000000", "#140C20"],
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
            ),
            expand=True,
            alignment=ft.alignment.top_left
        )

    def setup_event_handlers(self):
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop

    def go_home(self, _):
        self.page.go("/")

    def calendar_onclick(self, _):
        self.page.go("/calendar")
        print("calendar")

    def chart_onclick(self, _):
        self.page.go("/stats")
        print("chart")

    def add_onclick(self, _):
        self.page.go("/new")
        print("add")

    def end_form(self):
        print(self.sleepForm.get_input_data())
        print(self.emojiForm.get_input_data())
        self.db.add_record(
            self.sleepForm.get_input_data(),
            self.tiredForm.get_input_data(),
            self.happyForm.get_input_data(),
            self.dayForm.get_input_data(),
            self.emojiForm.get_input_data(),
            )
        self.formPage.reset()
        self.page.go("/")

    def route_change(self, route):
        self.page.views.clear()
        self.page.views.append(
            ft.View(
                "/",
                [self.mainScreen],
                padding=0
            )
        )
        print(route)
        print(self.page.route)

        if self.page.route == "/":
            self.mainLayout.set_page_no_update(self.mainPage)

        if self.page.route == "/new":
            self.page.views.append(
                ft.View(
                    "/new",
                    [self.formScreen],
                    padding=0
                )
            )

        if self.page.route == "/calendar":
            self.mainLayout.set_page_no_update(ft.Column(
                [
                    self.home_button,
                    ft.Text("Coming soon...", style=wide_header),
                    ft.Container(expand=True, alignment=ft.alignment.center)
                ],
                expand=True
            ))

        if self.page.route == "/stats":
            self.mainLayout.set_page_no_update(self.statsPage)

        self.page.update()

    def view_pop(self, view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)

    def close(self):
        try:
            self.db.connection.close()
            print("Database connection closed.")
        except AttributeError:
            print("DB not initialized skipping connection close...")

def main(page: ft.Page):
    app = App(page)

    print("asdad")

ft.app(main, assets_dir="assets")

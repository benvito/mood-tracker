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

def main(page: ft.Page):
    page.window.width = 375
    page.window.height = 812
    page.window.always_on_top = True

    page.bgcolor = "#0b0713"
    page.padding = 0
    page.spacing = 0

    def go_home(_):
        page.go("/")

    home_button = ImageButton(
        image="ui/home.png",
        width=40,
        on_click=go_home
    )

    def calendar_onclick(_):
        page.go("/calendar")
        print("calendar")

    def chart_onclick(_):
        page.go("/stats")
        print("chart")

    def add_onclick(_):
        page.go("/new")
        print("add")

    menubar = MenuBar(
                    image="ui/menubar.png",
                    calendar="ui/Calendar.png",
                    calendar_onclick=calendar_onclick,
                    chart="ui/BarChart.png",
                    chart_onclick=chart_onclick,
                    add="ui/Add.png",
                    add_onclick=add_onclick
                )

    mainPage = PageLayout(
                    content=ft.Column(
                            
                        controls=[

                            HiMessage(
                                text_style=basic_header,
                            ),

                            ft.Container(
                                expand=True
                            ),

                            Quote(
                                quote_style=quote_text,
                                text_style=basic_text,
                            )

                        ],
                    ), 
                )

    mainLayout = MainLayout(
        page=mainPage,
        menu_bar=menubar,
    )


        
    tiredForm = TiredForm(
        text_style1=wide_header,
        text_style2=form_text
    )

    sleepForm = SleepForm(
        text_style=form_text
    )

    happyForm = HappyForm(
        text_style1=wide_header,
        text_style2=form_text
    )

    dayFrom = DayForm(
        text_style1=wide_header,
        text_style2=form_text
    )

    emojiForm = EmojiForm(
        text=ft.Text(
            "Опиши свой день",
            style=wide_text,
            size=25
        ),
        text2=ft.Row(
            controls=[
                ft.Text(
                    "одной",
                    style=wide_text,
                    size=25,
                ),

                ft.Text(
                    "эмоцией",
                    style=wide_text,
                    size=25,
                    color="#c9a6ff"
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    def end_form():
        print(sleepForm.get_input_data())
        print(emojiForm.get_input_data())
        formPage.reset()
        page.go("/")
   
    formPage = FormLayout(
        forms=[sleepForm, tiredForm, happyForm, dayFrom, emojiForm], 
        end_event=end_form
        )
    

    statsPage = StatsPage(
        home_button=home_button
    )

    # mainLayout.set_page_no_update(statsPage)
    mainScreen = ft.Container(
            mainLayout,
            gradient=ft.LinearGradient(
                colors=["#000000", "#140C20"],
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
            ),
            expand=True,
            alignment=ft.alignment.top_left
        )

    formScreen = ft.Container(
            formPage,
            gradient=ft.LinearGradient(
                colors=["#000000", "#140C20"],
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
            ),
            expand=True,
            alignment=ft.alignment.top_left
        )

    

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    mainScreen
                ],
                padding=0
            )
        )
        print(route)
        print(page.route)    

        if page.route == "/":
            mainLayout.set_page_no_update(mainPage)

        if page.route == "/new":
            page.views.append(
                ft.View(
                    "/new",
                    [
                        formScreen
                    ],
                    padding=0
                )
            )

        if page.route == "/calendar":
            mainLayout.set_page_no_update(ft.Column(
                [
                    home_button,
                    ft.Text("Coming soon...", style=wide_header),
                    ft.Container(expand=True, alignment=ft.alignment.center)
                ],
                expand=True
            ))

        if page.route == "/stats":
            mainLayout.set_page_no_update(statsPage)

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)


ft.app(main, assets_dir="assets")


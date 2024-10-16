import flet as ft

from elements.menu_bar import MenuBar
from layouts.main_layout import PageLayout
from elements.hi_message import HiMessage
from elements.quote import Quote
from buttons.image_button import ImageButton
from layouts.form_layout import FormLayout
from pages.form_page import FormPage

def main(page: ft.Page):
    page.window.width = 375
    page.window.height = 812
    page.window.always_on_top = True

    page.bgcolor = "#0b0713"
    page.padding = 0
    page.spacing = 0

    basic_header = ft.TextStyle(
        color="white",
        weight=ft.FontWeight.W_400,
        size=25
    )

    wide_header = ft.TextStyle(
        color="white",
        weight=ft.FontWeight.W_600,
        size=25
    )

    basic_text = ft.TextStyle(
        color="white",
        weight=ft.FontWeight.W_400,
        size=17
    )

    wide_text = ft.TextStyle(
        color="white",
        weight=ft.FontWeight.W_600,
        size=17
    )

    quote_text = ft.TextStyle(
        color="white",
        weight=ft.FontWeight.W_600,
        size=25,
        letter_spacing=0.5,
        italic=True
    )

    form_text = ft.TextStyle(
        color="white",
        weight=ft.FontWeight.W_800,
        size=35
    )

    def calendar_onclick(_):
        print("calendar")

    def chart_onclick(_):
        print("chart")

    def add_onclick(_):
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

    currentPage = ft.Column(


            controls=[


                
                mainPage,

                
                menubar


            ],

            expand=True,
            spacing=0
        )

    def nextForm(_):
        form = formPage.get_current_form()
        if form == sleepForm:
            formPage.set_form(tiredForm)
        
    tiredForm = FormPage(
        backImage=ft.Container(
                    content=ft.Image(src="ui/tiredEmojis.png", scale=1),
                    margin=ft.margin.only(bottom=50),
                ),
        text=ft.Container(
                                content=ft.Column(
                                    [
                                        ft.Text("Насколько", style=wide_header, text_align=ft.TextAlign.END),
                                        ft.Text(
                                            "ты устал?", 
                                            style=form_text,
                                            text_align=ft.TextAlign.END, 
                                            color="#c9a6ff"
                                            ),
                                    ],
                                    spacing=0,
                                    horizontal_alignment=ft.CrossAxisAlignment.END
                                ),
                                alignment=ft.alignment.center_right
                            ),
        sliderColor="#a276ff",
        minSlider=ft.Image(src="ui/unlike.png", width=25, height=25),
        maxSlider=ft.Image(src="ui/like.png", width=25, height=25),
        button=ImageButton(image="ui/next.png")
    )

    sleepForm = FormPage(
        backImage=ft.Container(
                    content=ft.Image(src="ui/sleepEmojis.png", scale=1.1),
                    margin=ft.margin.only(bottom=60),
                ),
        text=ft.Container(
                    ft.Text("Как ты\nспал?", style=form_text)
            ),
        sliderColor="#a276ff",
        minSlider=ft.Image(src="ui/unlike.png", width=25, height=25),
        maxSlider=ft.Image(src="ui/like.png", width=25, height=25),
        button=ImageButton(image="ui/next.png", on_click=nextForm)
    )
   
    formPage = FormLayout(init_form=sleepForm)

    currentPage = formPage

    page.add(
        
        
        ft.Container(
            currentPage,
            gradient=ft.LinearGradient(
                colors=["#000000", "#140C20"],
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
            ),
            expand=True,
            alignment=ft.alignment.top_left
        )

        

    )


ft.app(main, assets_dir="assets")

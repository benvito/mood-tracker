import flet as ft
from pages.form_page import FormPage
from buttons.image_button import ImageButton
from buttons.text_icon_button import TextIconButton
from styles.text import *

class DayForm(FormPage):
    def __init__(
        self,
        text_style1,
        text_style2,
    ):

        backImage=ft.Container(
                    content=ft.Image(src="ui/dayEmojis.png", scale=0.9),
                    margin=ft.margin.only(bottom=60, left=30),
                )
        text=ft.Container(
                                content=ft.Column(
                                    [
                                        ft.Text("Как прошел", style=text_style1, text_align=ft.TextAlign.END),
                                        ft.Text(
                                            "твой день?", 
                                            style=text_style2,
                                            text_align=ft.TextAlign.END, 
                                            color="#c9a6ff"
                                            ),
                                    ],
                                    spacing=0,
                                    horizontal_alignment=ft.CrossAxisAlignment.START
                                ),
                                alignment=ft.alignment.center_left
                            )
        sliderColor="#a276ff"
        minSlider=ft.Image(src="ui/unlike.png", width=25, height=25)
        maxSlider=ft.Image(src="ui/like.png", width=25, height=25)
        button=TextIconButton(
            icon=ft.Image(src="ui/right_arrow.png", width=10),
            width=150,
            height=50,
            text="Далее",
            text_style=wide_header
        )

        FormPage.__init__(self, backImage, text, minSlider, maxSlider, sliderColor, button)

    def get_info(self):
        return "DayForm"
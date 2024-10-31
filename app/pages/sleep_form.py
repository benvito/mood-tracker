import flet as ft
from pages.form_page import FormPage
from buttons.image_button import ImageButton
from buttons.text_icon_button import TextIconButton
from styles.text import *

class SleepForm(FormPage):
    def __init__(
        self,
        text_style,
    ):

        backImage=ft.Container(
               content=ft.Image(src="ui/sleepEmojis.png", scale=1.1),
               margin=ft.margin.only(bottom=60),
           )
        text=ft.Container(
                    ft.Text("Как ты\nспал?", style=text_style)
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
        return "SleepForm"
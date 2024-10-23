import flet as ft
from pages.form_page import FormPage
from buttons.image_button import ImageButton
from buttons.text_icon_button import TextIconButton
from styles.text import *

class HappyForm(FormPage):
    def __init__(
        self,
        text_style1,
        text_style2,
    ):

        backImage=ft.Container(
                    content=ft.Image(src="ui/happyEmojis.png", scale=1),
                    margin=ft.margin.only(bottom=50),
                )
        text=ft.Container(
                                content=ft.Column(
                                    [
                                        ft.Text("Насколько ты", style=text_style1, text_align=ft.TextAlign.END),
                                        ft.Text(
                                            "счастлив?", 
                                            style=text_style2,
                                            text_align=ft.TextAlign.END, 
                                            color="#fcffa6"
                                            ),
                                    ],
                                    spacing=0,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                ),
                                alignment=ft.alignment.center
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

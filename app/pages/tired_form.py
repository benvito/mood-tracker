import flet as ft
from pages.form_page import FormPage
from buttons.image_button import ImageButton
from buttons.text_icon_button import TextIconButton
from styles.text import *

class TiredForm(FormPage):
    def __init__(
        self,
        text_style1,
        text_style2,
        *args,
        **kwagrs,
    ):

        backImage=ft.Container(
                    content=ft.Image(src="ui/tiredEmojis.png", scale=1),
                    margin=ft.margin.only(bottom=50),
                )
        text=ft.Container(
                                content=ft.Column(
                                    [
                                        ft.Text("Насколько", style=text_style1, text_align=ft.TextAlign.END),
                                        ft.Text(
                                            "ты устал?", 
                                            style=text_style2,
                                            text_align=ft.TextAlign.END, 
                                            color="#c9a6ff"
                                            ),
                                    ],
                                    spacing=0,
                                    horizontal_alignment=ft.CrossAxisAlignment.END
                                ),
                                alignment=ft.alignment.center_right
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

        FormPage.__init__(
            *args, 
            **kwagrs,
            self=self, 
            backImage=backImage, 
            text=text, 
            minSlider=minSlider, 
            maxSlider=maxSlider, 
            sliderColor=sliderColor, 
            button=button, 
            )
        
    def get_info(self):
        return "TiredForm"
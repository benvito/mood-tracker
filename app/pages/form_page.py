import flet as ft
from layouts.main_layout import PageLayout
from buttons.image_button import ImageButton

class FormPage(ft.Stack):
    def __init__(
        self,
        backImage : ft.Control,
        text : ft.Control,
        minSlider : ft.Image,
        maxSlider : ft.Image,
        sliderColor : str,
        button : ImageButton,
        button_size : int = 50,
        *args,
        **kwagrs,
    ):
        super().__init__(*args, **kwagrs)


        self.expand = True
        self.backImage = backImage
        self.text = text

        self.button = button
        self.btn_container = ft.Container(
                                content=self.button,
                                height=button_size,
                                alignment=ft.alignment.center_right,
                                margin=ft.margin.only(top=40),
                            )

        self.slider = ft.Slider(
                                width=400,
                                active_color=sliderColor,
                                )

        self.controls = [
            self.backImage,

            PageLayout(
                content=ft.Column(

                    controls=[
                        text,
                        ft.Container(    
                            content=self.slider,
                        ),
                        ft.Row(
                            controls=[
                                minSlider,
                                maxSlider,
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        self.btn_container,
                    ],
                    alignment=ft.MainAxisAlignment.END,
                    spacing=0,
                ),
            )
        ]
        
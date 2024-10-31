import flet as ft
from layouts.main_layout import PageLayout
from buttons.image_button import ImageButton
from buttons.text_icon_button import TextIconButton

class FormPage(ft.Stack):
    def __init__(
        self,
        backImage : ft.Control = ft.Container(),
        text : ft.Control = ft.Text("Text"),
        minSlider : ft.Image = ft.Image(src="ui/unlike.png", width=25, height=25),
        maxSlider : ft.Image = ft.Image(src="ui/like.png", width=25, height=25),
        sliderColor : str = "#a276ff",
        button : TextIconButton = TextIconButton(),
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

    def get_button(self):
        return self.button

    def set_button_on_click(self, func):
        self.button.on_click = func

    def get_input_data(self):
        return self.slider.value

    def get_info(self):
        return "Basic Form Template"
        
        
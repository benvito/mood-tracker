import flet as ft
from pages.form_page import FormPage
from buttons.image_button import ImageButton

class SleepForm(ft.UserControl):
    def __init__(
        self,
        next_click,
        *args,
        **kwagrs,
    ):

        self.sleep_form = FormPage(
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
        button=ft.Container(
                                content=ImageButton(image="ui/next.png", on_click=self.nextForm),
                                height=50,
                                alignment=ft.alignment.center_right,
                                margin=ft.margin.only(top=40),
                            )
    )

        super().__init__(*args, **kwagrs)

    def nextForm(self, _):

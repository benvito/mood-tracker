import flet as ft
from layouts.main_layout import PageLayout
from styles.text import *
from buttons.text_icon_button import TextIconButton
from buttons.button_bar import ButtonBar

class StatsPage(PageLayout):
    def __init__(
            self, 
            *args, 
            **kwargs
    ):
        super().__init__(*args, **kwargs)

        self.content = ft.Column(


            controls=[

                ft.Container(
                    ft.Text(
                        "Статистика",
                        style=xtra_wide_header,
                        size=30
                    )
                ),

                ButtonBar(
                    buttons=[
                        TextIconButton(
                            text="Все время",
                            text_style=buttons_text,
                            border_radius=13,
                            height=35
                        ),

                        TextIconButton(
                            text="Неделя",
                            text_style=buttons_text,
                            border_radius=13,
                            height=35
                        ),
                    ],
                    init=0,
                    on_click=self.choose_time
                )

            ]

        )


    def choose_time(self, index):
        print("index: ", index)

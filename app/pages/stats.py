import flet as ft
from layouts.main_layout import PageLayout
from styles.text import *

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
                )

                

            ]

        )

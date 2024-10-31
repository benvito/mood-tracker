import flet as ft
from layouts.main_layout import PageLayout
from styles.text import *
from buttons.text_icon_button import TextIconButton
from buttons.button_bar import ButtonBar
from elements.tiles import *
from styles.gradients import *
from elements.my_tiles import *

class StatsPage(PageLayout):
    def __init__(
            self,
            home_button : ft.Control = None,
            *args, 
            **kwargs
    ):
        super().__init__(*args, **kwargs)

        self.button_bar = ButtonBar(
                    buttons=[
                        TextIconButton(
                            text="Все время",
                            text_style=buttons_text,
                            border_radius=13,
                            height=35,
                            selectable=True
                        ),

                        TextIconButton(
                            text="Неделя",
                            text_style=buttons_text,
                            border_radius=13,
                            height=35,
                            selectable=True
                        ),
                    ],
                    init=0,
                    on_click=self.choose_time
                )
        
        self.header = ft.Container(
                    ft.Text(
                        "Статистика",
                        style=xtra_wide_header,
                        size=30
                    )
                )

        self.tiles = Tiles(
                    h_space_around=True,
                    tiles_by_row=2,
                    tiles=[
                        FreqEmote(),
                        PercentHappy(),
                        DayAvg(),
                        TiredScore(),
                    ]
                )

        self.content = ft.Column(


            controls=[
                ft.Container(
                    home_button,
                ),

                ft.Container(
                    self.header,
                ),

                self.button_bar,

                ft.Container(
                    self.tiles,
                    margin=ft.margin.symmetric(vertical=15)
                )

            ],
            spacing=10

        )


    def choose_time(self, event, index):
        print("index: ", index)
        print("event: ", event)

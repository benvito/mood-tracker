import flet as ft
from layouts.main_layout import PageLayout
from styles.text import *
from buttons.text_icon_button import TextIconButton
from buttons.button_bar import ButtonBar
from elements.tiles import *
from styles.gradients import *
from elements.my_tiles import *
from backend.constants import *
from backend.db.entities import *
from backend.db import DatabaseController
from enum import Enum
import logging

class PeriodTime(Enum):
    ALL = 0
    WEEK = 1

class StatsPage(PageLayout):
    def __init__(
            self,
            home_button : ft.Control = None,
            db : DatabaseController = None,
            *args, 
            **kwargs
    ):
        super().__init__(*args, **kwargs)

        self.db = db
        self._period_time = PeriodTime.ALL

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

        self.freq_emote = FreqEmote()
        self.percent_happy = PercentHappy()
        self.day_avg = DayAvg()
        self.tired_score = TiredScore()

        self.tiles = Tiles(
                    h_space_around=True,
                    tiles_by_row=2,
                    tiles=[
                        self.freq_emote,
                        self.percent_happy,
                        self.day_avg,
                        self.tired_score
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

    @property
    def period_time(self):
        return self._period_time
    
    @period_time.setter
    def period_time(self, value):
        logging.info(f"Stats view period time changed to: {value}")
        self._period_time = value
        self.set_data()

    def choose_time(self, event, index):
        if index == 0:
            self.period_time = PeriodTime.ALL
        elif index == 1:
            self.period_time = PeriodTime.WEEK
            

    def set_data(self):
        if self.period_time == PeriodTime.ALL:
            data = self.db.aggregate_data()

            if data is None:
                return

            self.tired_score.set_data(data.avg_tired.score10())

            self.day_avg.set_data(data.avg_day.percent().to_int())

            self.percent_happy.set_data(data.avg_happy.percent().to_int()) 

            self.freq_emote.set_data(data.avg_emoji)  
            self.freq_emote.update()
        elif self.period_time == PeriodTime.WEEK:
            data = self.db.aggregate_weekly_data()

            if data is None:
                return

            self.tired_score.set_data(data.avg_tired.score10())

            self.day_avg.set_data(data.avg_day.percent().to_int())

            self.percent_happy.set_data(data.avg_happy.percent().to_int())  
             
            self.freq_emote.set_data(data.avg_emoji)
            self.freq_emote.update()

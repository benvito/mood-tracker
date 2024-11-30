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
from elements.calendar import CustomCalendar
import datetime

class PeriodTime(Enum):
    ALL = 0
    WEEK = 1

class CalenarPage(PageLayout):
    def __init__(
            self,
            home_button : ft.Control = None,
            db : DatabaseController = None,
            *args, 
            **kwargs
    ):
        super().__init__(*args, **kwargs)

        self.db = db
        
        self.header = ft.Container(
                    ft.Text(
                        "Календарь",
                        style=xtra_wide_header,
                        size=30
                    )
                )

 
        
        self.calendar = CustomCalendar(
            width=330,
            bgcolor=ft.colors.TRANSPARENT,
            hover_color=ft.colors.with_opacity(0.72, "#dfcefb"),
            font_color=ft.colors.WHITE,
            font_color_accent="#09050e",
            accent_color="#ddccf9",
            header_font_color="#ddccf9",
            border_radius=5,
            change_month=self.update_daily_data,
            daily_data=self.db.get_daily_average_scores(datetime.datetime.now().month, datetime.datetime.now().year)
            )

        self.content = ft.Column(


            controls=[
                ft.Container(
                    home_button,
                ),

                ft.Container(
                    self.header,
                ),

                ft.Container(
                    self.calendar
                )
    
            ],
            spacing=10

        )

    def update_daily_data(self, month, year):
        self.calendar.update_daily_data(self.db.get_daily_average_scores(month, year))


    def update_calendar_data(self):
        self.update_daily_data(self.calendar._current_month, self.calendar._current_year)

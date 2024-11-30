import flet as ft
from elements.tiles import *
from styles.text import *
from styles.gradients import *

class DayAvg(ContentTile):
    def __init__(
            self,
            *args,
            **kwargs
    ):
        text=ft.Text(
            "Твой средний день:",
            style=basic_text,
        )

        self._avg_day = 0

        self.number = ft.Text(
            self._avg_day,
            style=wide_text,
        )

        self.percent = ft.Text(
            "%",
            style=wide_text
        )

        self.wrap_num = ft.Container(
            ft.Row(
                [
                    self.number,
                    self.percent
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=1,
                opacity=0.8
            ),
            margin=ft.margin.only(left=10)
        )

        self.progress_bar_width = 130
        self.progress_width = (self._avg_day / 100) * self.progress_bar_width

        self.progress = ft.Container(
                        
                            bgcolor="green",
                            width=self.progress_width,
                            border_radius=10,
                            padding=0,
                            margin=0,
                        )

        self.progress_bar = ft.Container(
            content=
                ft.Stack(
                    controls=[
                        self.progress,
                            
                        self.wrap_num,
                    ],
                    
                ),
            padding=0,
            width=self.progress_bar_width,
            height=25,
            # alignment=ft.alignment.center,
            bgcolor="#1C1C1C",
            border_radius=10
        )
                                
        
        tile_content=[
            ft.Container(
                
                self.progress_bar,
                margin=ft.margin.only(top=40),
                alignment=ft.alignment.center,
            ),
        ]
        gradient=get_gradient(
                            "#B386FF", "#542B99", 
                            [ft.alignment.top_right, ft.alignment.bottom_left]
        )

        super().__init__(
            text=text,
            tile_content=tile_content,
            gradient=gradient,
            *args,
            **kwargs
        )

    @property
    def avg_day(self):
        return self._avg_day

    @avg_day.setter
    def avg_day(self, value):
        self._avg_day = value
        self.number.value = value
        self.progress_width = (self._avg_day / 100) * self.progress_bar_width
        self.progress.width = self.progress_width
        self.update()

    def set_data(self, data):
        self.avg_day = data
    
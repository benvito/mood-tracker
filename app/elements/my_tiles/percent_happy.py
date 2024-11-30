import flet as ft
from elements.tiles import *
from styles.text import *
from styles.gradients import *

class PercentHappy(ContentTile):
    def __init__(
            self,
            *args,
            **kwargs
    ):
        text=ft.Text(
            "Процент счастья:",
            style=basic_text,
        )

        self._percent_happy = 0

        self.number = ft.Text(
            self.percent_happy,
            style=stat_num_text,
        )

        self.percent = ft.Text(
            "%",
            style=percent_text,
        )
                                
        
        tile_content=[
            ft.Container(
                
                ft.Row(
                        [
                            self.number,

                            ft.Container(
                                self.percent,
                                rotate=0.3,
                            ),
                        ],
                    spacing=2,
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                ),
                margin=ft.margin.only(top=40),
                alignment=ft.alignment.center
            ),
        ]
        gradient=get_gradient(
                            "#B386FF", "#542B99", 
                            [ft.alignment.bottom_left, ft.alignment.top_right]
        )

        super().__init__(
            text=text,
            tile_content=tile_content,
            gradient=gradient,
            *args,
            **kwargs
        )

    @property
    def percent_happy(self):
        return self._percent_happy

    @percent_happy.setter
    def percent_happy(self, value):
        self._percent_happy = value
        self.number.value = value
        self.update()
    
    def set_data(self, data):
        self.percent_happy = data
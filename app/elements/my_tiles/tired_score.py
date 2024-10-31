import flet as ft
from elements.tiles import *
from styles.text import *
from styles.gradients import *

class TiredScore(ContentTile):
    def __init__(
            self,
            *args,
            **kwargs
    ):
        text=ft.Text(
            "В среднем ты устаешь на:",
            style=basic_text,
        )

        self._tired_score = 7
        self.max_score = 10

        self.number = ft.Text(
            self.tired_score,
            style=stat_num_text,
        )

        self.out_of_text = ft.Text(
            "из",
            style=wide_header,
        )

        self.max_score_text = ft.Text(
            self.max_score,
            style=stat_max_score,
        )
                                
        
        tile_content=[
            ft.Container(
                
                ft.Row(
                        [
                            self.number,

                            ft.Container(
                                self.out_of_text,
                                margin=ft.margin.only(bottom=5)
                            ),

                            ft.Container(
                                self.max_score_text,
                                margin=ft.margin.only(bottom=3)
                            ),
                        ],
                    spacing=7,
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.END
                ),
                margin=ft.margin.only(top=40),
                alignment=ft.alignment.center
            ),
        ]
        gradient=get_gradient(
                            "#B386FF", "#542B99", 
                            [ft.alignment.top_left, ft.alignment.bottom_right]
        )

        super().__init__(
            text=text,
            tile_content=tile_content,
            gradient=gradient,
            *args,
            **kwargs
        )

    @property
    def tired_score(self):
        return self._tired_score

    @tired_score.setter
    def tired_score(self, value):
        self._tired_score = value
        self.number.value = value
        self.update()
    
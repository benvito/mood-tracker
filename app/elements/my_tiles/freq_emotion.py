import flet as ft
from elements.tiles import *
from styles.text import *
from styles.gradients import *
from backend.constants import *
import logging

class FreqEmote(ContentTile):
    def __init__(
            self,
            *args,
            **kwargs
    ):
        text=ft.Text(
            "Самая частая эмоция:",
            style=basic_text,
        )

        self._top1 = EmojisFeelings.QUESTION.src
        self._top2 = EmojisFeelings.QUESTION.src

        self.top_1_img = ft.Image(
                            src=self._top1,
                            width=100,
                            rotate=-0.2
                            )

        self.top_2_img = ft.Image(
                                src=self._top2,
                                width=50,
                                rotate=0.2,
                                opacity=0.5,
                                )
                                
        
        tile_content=[
            ft.Container(
                
                ft.Row(
                        [
                            ft.Container(
                                self.top_2_img,
                                margin=ft.margin.only(top=40),
                            ),
                            self.top_1_img
                        ],
                    
                ),
                alignment=ft.alignment.bottom_center
            ),
        ]
        gradient=get_gradient(
            "#B386FF", "#542B99", 
            [ft.alignment.bottom_right, ft.alignment.top_left]
        )

        super().__init__(
            text=text,
            tile_content=tile_content,
            gradient=gradient,
            *args,
            **kwargs
        )

    @property
    def top1(self):
        return self._top1

    @top1.setter
    def top1(self, value):
        self._top1 = value
        self.top_1_img.src = value

    @property
    def top2(self):
        return self._top2

    @top2.setter
    def top2(self, value):
        self._top2 = value
        self.top_2_img.src = value

    def set_data(self, data : list):
        if len(data) == 2:
            self.top1 = EmojisFeelings.get_src_by_id(data[0])
            self.top2 = EmojisFeelings.get_src_by_id(data[1])
        elif len(data) == 1:
            logging.warning("Only one emotion found")
            self.top1 = EmojisFeelings.get_src_by_id(data[0])
            self.top2 = EmojisFeelings.QUESTION.src
        else:
            logging.warning("No emotion found")
            self.top1 = EmojisFeelings.QUESTION.src
            self.top2 = EmojisFeelings.QUESTION.src
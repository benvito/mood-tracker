import flet as ft
from typing import Callable

class ButtonBar(ft.Container):
    def __init__(
            self,
            buttons : list,
            init : int = 0,
            on_click : Callable = None,
            space_between : int = 15,
            *args,
            **kwargs,
    ):  
        super().__init__(*args, **kwargs)
        for i in range(len(buttons)):
            buttons[i].expand = 1
            buttons[i].on_click = on_click

        self.content = ft.Row(
            controls=buttons,
            spacing=space_between
        )

        self.padding = 0
        self.margin = 0

        # self.bgcolor = ft.colors.AMBER

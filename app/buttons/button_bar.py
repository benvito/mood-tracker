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
        self.click_func = on_click
        super().__init__(*args, **kwargs)
        for i in range(len(buttons)):
            buttons[i].expand = 1
            buttons[i].on_click = self.on_click_btn

            try:
                buttons[i].selected = i == init
            except:
                pass

        self.buttons = buttons
        self.content = ft.Row(
            controls=buttons,
            spacing=space_between
        )

        self.padding = 0
        self.margin = 0

    def on_click_btn(self, event):
        index = self.buttons.index(event.control)

        try:
            for i in range(len(self.buttons)):
                self.buttons[i].selected = False
        
            self.buttons[index].selected = True
        except:
            pass
        
        self.update()

        self.click_func(event, index) 
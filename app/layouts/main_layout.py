import flet as ft

class PageLayout(ft.Container):

    def __init__(
            self, 
            *args,
            **kwargs
            ):
        super().__init__(*args, **kwargs)
        self.alignment=ft.alignment.top_left
        self.margin=ft.margin.symmetric(horizontal=15, vertical=25)
        self.expand=True
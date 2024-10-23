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

class MainLayout(ft.Column):
    def __init__(
            self,
            page : ft.Control,
            menu_bar : ft.Control,
            *args,
            **kwargs
    ):
        self.current_page = page
        self.menu_bar = menu_bar
        super().__init__(*args, **kwargs)

        self.controls = [self.current_page, self.menu_bar]
        self.expand = True
        self.spacing = 0

    def set_page(self, page : ft.Control):
        self.current_page = page
        self.controls = [
            self.current_page,
            self.menu_bar,
        ]

        self.update()

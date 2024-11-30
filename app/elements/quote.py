import flet as ft


class Quote(ft.Container):
    def __init__(
            self, 
            quote : str = None,
            text_style : ft.TextStyle = None, 
            quote_style : ft.TextStyle = None, 
            *args, **kwargs
            ):
        super().__init__(*args, **kwargs)
        self.quote = ft.Text(
            quote, 
            style=quote_style,
            text_align=ft.TextAlign.START
            )
        self.content = ft.Column(
            [
                ft.Text("Цитата твоего дня", style=text_style),
                self.quote
            ]
        )


    def change_quote(self, quote):
        self.quote.value = quote
        self.update()
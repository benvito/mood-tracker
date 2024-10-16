import flet as ft

# ft.Container(
#                                 content=ft.Text("Hello World"),
#                                 height=100,
#                                 bgcolor="#1b0139",
#                                 alignment=ft.alignment.top_left,
#                             )

class HiMessage(ft.Container):
    def __init__(
            self,
            text_style : ft.TextStyle = None, 
            *args, 
            **kwargs
            ):
        super().__init__(*args, **kwargs)
        self.hi_text = ft.Text("Hi, <username>", style=text_style, size=25)
        self.emote_text = ft.Text("👋", size=25)
        self.content = ft.Column(
            [self.hi_text, self.emote_text],
            spacing=0
        )
        # self.height = 100
        self.alignment = ft.alignment.top_left
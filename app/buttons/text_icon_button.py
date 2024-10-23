import flet as ft

class TextIconButton(ft.ElevatedButton):
    def __init__(
            self,
            text : str = None,
            icon : ft.Image = None,
            text_style : ft.TextStyle = None,
            width : int = 50,
            height : int = 50,
            color : str = "#a276ff",
            border_radius : int = 50,
            spacing : int = 20,
            *args,
            **kwargs
    ):

        super().__init__(*args, **kwargs)

        if text is None:
            self.text = None
        else:
            self.text = ft.Text(text, style=text_style)
        
        if icon is None:
            self.icon = None
        else:
            self.icon = icon

        self.style = ft.ButtonStyle(
                color=ft.colors.TRANSPARENT,
                bgcolor=ft.colors.TRANSPARENT,
                overlay_color=ft.colors.TRANSPARENT,
                shadow_color=ft.colors.TRANSPARENT,
                surface_tint_color=ft.colors.TRANSPARENT,
                padding=0
            )

        self.in_items = []

        if self.text is not None:
            self.in_items.append(
                ft.Container(
                        self.text,
                        margin=ft.margin.only(bottom=5)
                    )
            )

        if self.icon is not None:
            self.in_items.append(
                ft.Container(
                        self.icon,
                )
            )

        self.content = ft.Container(
            content=ft.Row(
                [
                    *self.in_items
                ],
                spacing=spacing,
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            ),
            width=width,
            height=height,
            border_radius=border_radius,
            bgcolor=color,
            alignment=ft.alignment.center
        )

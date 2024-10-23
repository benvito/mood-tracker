import flet as ft
from styles.text import basic_text
from typing import Callable

class TextIconButton(ft.ElevatedButton):
    def __init__(
            self,
            text : str = None,
            icon : ft.Image = None,
            text_style : ft.TextStyle = basic_text,
            width : int = None,
            height : int = None,
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
            self.text = ft.Text(text, style=text_style, text_align=ft.TextAlign.CENTER)
        
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
                        margin=ft.margin.only(bottom=5),
                        alignment=ft.alignment.center
                    )
            )

        if self.icon is not None:
            self.in_items.append(
                ft.Container(
                        self.icon,
                        alignment=ft.alignment.center
                )
            )

        self.content = ft.Container(
            content=ft.Container(
                ft.Row(
                    [
                        *self.in_items
                    ],
                    spacing=spacing,
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                alignment=ft.alignment.center
            ),
            width=width,
            height=height,
            border_radius=border_radius,
            bgcolor=color,
            alignment=ft.alignment.center,
            padding=0,
            margin=0
        )

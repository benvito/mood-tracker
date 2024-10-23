import flet as ft

class ImageButton(ft.ElevatedButton):

    def __init__(
            self,
            image = '',
            *args,
            **kwargs
            ):

        super().__init__(*args, **kwargs)
        self.content = ft.Image(src=image)
        self.style = ft.ButtonStyle(
                color=ft.colors.TRANSPARENT,
                bgcolor=ft.colors.TRANSPARENT,
                overlay_color=ft.colors.TRANSPARENT,
                shadow_color=ft.colors.TRANSPARENT,
                surface_tint_color=ft.colors.TRANSPARENT,
                padding=0
            )
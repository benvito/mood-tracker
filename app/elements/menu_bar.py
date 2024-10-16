import flet as ft

from buttons.image_button import ImageButton

class MenuBar(ft.Container):
    def __init__(
            self, 
            image,
            calendar,
            calendar_onclick,
            chart,
            chart_onclick,
            add,
            add_onclick,
            *args,
            **kwargs,
            ):
        super().__init__(*args, **kwargs)

        calendar_button = ImageButton(
            image=calendar,
            width=50,
            height=50,
            on_click=calendar_onclick
        )

        chart_button = ImageButton(
            image=chart,
            width=50,
            height=50,
            on_click=chart_onclick
        )

        addbutton = ImageButton(
            image=add,
            width=70,
            height=70,
            on_click=add_onclick
        )

        self.alignment = ft.alignment.bottom_center
        self.content = ft.Stack(
            [
                ft.Container(
                    content=ft.Image(src=image),
                    
                ),
            
                ft.Container(
                    content=ft.Row(
                        [
                            chart_button,
                            calendar_button,
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    margin=ft.margin.symmetric(horizontal=42, vertical=5),
                    expand=True,
                ),
                
                ft.Container(
                    content=addbutton,
                    bottom=25
                )
            ],
            alignment=ft.alignment.bottom_center,
            expand=True,
            height = 96
        )

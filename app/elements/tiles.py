import flet as ft

class Tile(ft.Container):
    def __init__(
            self,
            width : int = 150,
            height : int = 150,
            gradient : ft.Control = ft.LinearGradient(
                                        begin=ft.alignment.bottom_right,
                                        end=ft.alignment.top_left,
                                        colors=[
                                            "#B386FF",
                                            "#542B99",
                                        ]
                                    ),
            border_radius : int = 15,
            *args,
            **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.width = width
        self.height = height
        self.gradient = gradient
        self.border_radius = border_radius

class TileContent(ft.Container):
    def __init__(
            self,
            content : ft.Control = None,
            right : int = 0,
            bottom : int = 0,
            top : int = 0,
            left : int = 0,
            alignment : ft.alignment = ft.alignment.center,
            *args,
            **kwargs,
    ):
        super().__init__(*args, **kwargs)



class ContentTile(Tile):
    def __init__(
            self,
            text : ft.Control = None,
            tile_content : list = None,
            *args, 
            **kwargs
    ):
        super().__init__(*args, **kwargs)

        self.text = text
        self.tile_content = tile_content
        self.content = ft.Container(

            content=ft.Stack(

                controls=[
                    ft.Container(
                        content=self.text,
                        alignment=ft.alignment.top_left,
                    ),
                    *self.tile_content
                ],
            ),
            margin=ft.margin.symmetric(horizontal=10, vertical=7),
        )

    def get_content(self):
        return self.tile_content

    def change_content(self, content):
        self.tile_content = content
        self.update()


class Tiles(ft.Column):
    def __init__(
            self,
            tiles : list = None,
            tiles_by_row : int = 2,
            h_spacing : int = 10,
            v_spacing : int = 10,
            h_space_around : bool = False,
            *args,
            **kwargs
    ):
        super().__init__(*args, **kwargs)

        self.tiles = tiles
        
        self.v_spacing = v_spacing
        self.h_spacing = h_spacing

        rows_alignment = ft.MainAxisAlignment.CENTER
        if h_space_around:
            self.h_spacing = 0
            rows_alignment = ft.MainAxisAlignment.SPACE_AROUND

        self.rows = []

        i_row = 0
        i_tiles = 0
        while i_tiles < len(tiles):
            row = ft.Row(
                controls=tiles[i_tiles:i_tiles+tiles_by_row], 
                spacing=h_spacing,
                alignment=rows_alignment,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
                )
            self.rows.append(row)
            i_row += 1
            i_tiles += tiles_by_row

        self.controls = self.rows

        self.spacing = v_spacing
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER


        
            
import flet as ft

def get_gradient(color1, color2, angle : list = [ft.alignment.bottom_center, ft.alignment.top_center]):

    gradient = ft.LinearGradient(
        colors=[
            color1,
            color2,
        ]
    )

    gradient.begin = angle[0]
    gradient.end = angle[1]

    return gradient

    

import flet as ft
from buttons.image_button import ImageButton

class ChooseOption(ft.Stack):
    def __init__(self, image_list):
        super().__init__()
        self.image_list = image_list
        self.current_index = 0
        self.total_images = len(image_list)
        self.image_size = 150
        self.side_opacity = 0.25
        self.center_alignment_offset = 1
        self.animation_duration = 400

        # Создаем элементы интерфейса
        self.left_button = ft.IconButton(
            icon=ft.icons.ARROW_LEFT,
            on_click=self.prev_image,
            icon_color=ft.colors.WHITE,
            scale=1.5
        )
        self.right_button = ft.IconButton(
            icon=ft.icons.ARROW_RIGHT,
            on_click=self.next_image,
            icon_color=ft.colors.WHITE,
            scale=1.5
        )

        # Контейнер для изображений (Row)
        self.image_row = ft.Row(
            controls=[],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        self.image_cont = ft.Container(
            content=self.image_row,
            alignment=ft.alignment.center,
        )

        # Контейнер с кнопками

        self.buttons = ft.Container(
        ft.Row(
            controls=[self.left_button, self.right_button],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=self.image_size * 1.40,
            opacity=0.5,
        ),
        height=self.image_size,
        alignment=ft.alignment.center
        )
        
        self.controls = [self.image_cont, self.buttons]
        self.alignment=ft.alignment.center
        self.update_image_controls()


    def create_image_control(self, img_data, is_center=False):
        return ft.Container(
            content=ft.Image(src=img_data["src"], fit=ft.ImageFit.CONTAIN),
            opacity=1.0 if is_center else self.side_opacity,
            alignment=ft.alignment.center,
            height=self.image_size if is_center else self.image_size // 2,
            width=self.image_size if is_center else self.image_size // 2,
        )

    def update_image_controls(self):
        """Обновляем отображаемые элементы"""
        self.image_row.controls.clear()

        for _ in range(self.center_alignment_offset - self.current_index):
            self.image_row.controls.append(ft.Container(width=self.image_size // 2))

        # Логика для отображения центрального и боковых изображений
        start_index = max(0, self.current_index - 1)
        end_index = min(self.total_images, self.current_index + 2)

        for i in range(start_index, end_index):
            is_center = (i == self.current_index)
            image_control = self.create_image_control(self.image_list[i], is_center)
            self.image_row.controls.append(image_control)

        for _ in range(self.center_alignment_offset - (self.total_images - self.current_index - 1)):
            self.image_row.controls.append(ft.Container(width=self.image_size // 2))

    def next_image(self, e=None):
        if self.current_index < self.total_images - 1:
            self.current_index += 1
        else:
            self.current_index = 0  # Зацикливание
        self.update_image_controls()
        self.image_row.update()

    def prev_image(self, e=None):
        if self.current_index > 0:
            self.current_index -= 1
        else:
            self.current_index = self.total_images - 1  # Зацикливание
        self.update_image_controls()
        self.image_row.update()

    def get_current_image_id(self):
        return self.image_list[self.current_index]["id"]

    def reset_current_index(self):
        self.current_index = 0
        self.update_image_controls()
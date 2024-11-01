import flet as ft
from buttons.image_button import ImageButton
from layouts.main_layout import PageLayout
from elements.choose_option import ChooseOption
from enum import Enum
from pages.form_page import FormPage
from buttons.text_icon_button import TextIconButton
from styles.text import *
from backend import EmojisFeelings

FEELING_LIST = [
    {
        "id": EmojisFeelings.LOVED.id,
        "src": EmojisFeelings.LOVED.src,
    },
    {
        "id": EmojisFeelings.FUNNY.id,
        "src": EmojisFeelings.FUNNY.src,
    },
    {
        "id": EmojisFeelings.ANGEL.id,
        "src": EmojisFeelings.ANGEL.src,
    },
    {
        "id": EmojisFeelings.CHILL.id,
        "src": EmojisFeelings.CHILL.src,
    },
    {
        "id": EmojisFeelings.COOL.id,
        "src": EmojisFeelings.COOL.src,
    },
    {
        "id": EmojisFeelings.YAMMY.id,
        "src": EmojisFeelings.YAMMY.src,
    },
    {
        "id": EmojisFeelings.OK.id,
        "src": EmojisFeelings.OK.src,
    },
    {
        "id": EmojisFeelings.WTF.id,
        "src": EmojisFeelings.WTF.src,
    },
    {
        "id": EmojisFeelings.SLEEPY.id,
        "src": EmojisFeelings.SLEEPY.src,
    },
    {
        "id": EmojisFeelings.NOCOMMENTS.id,
        "src": EmojisFeelings.NOCOMMENTS.src,
    },
    {
        "id": EmojisFeelings.DRUNK.id,
        "src": EmojisFeelings.DRUNK.src,
    },
    {
        "id": EmojisFeelings.DISCONTENT.id,
        "src": EmojisFeelings.DISCONTENT.src,
    },
    {
        "id": EmojisFeelings.PLSNO.id,
        "src": EmojisFeelings.PLSNO.src,
    },
    {
        "id": EmojisFeelings.SCARY.id,
        "src": EmojisFeelings.SCARY.src,
    },
    {
        "id": EmojisFeelings.TIRED.id,
        "src": EmojisFeelings.TIRED.src,
    },
    {
        "id": EmojisFeelings.BAD.id,
        "src": EmojisFeelings.BAD.src,
    },
    {
        "id": EmojisFeelings.FUCK.id,
        "src": EmojisFeelings.FUCK.src,
    },
]

    

class EmojiForm(FormPage):

    def __init__(
        self,
        text : ft.Control,
        text2 : ft.Control,
        button_size : int = 50,
        *args,
        **kwagrs,
    ):

        FormPage.__init__(
            self
        )

        self.text = text
        self.text2 = text2

        self.choose = ChooseOption(
            image_list=FEELING_LIST
        )

        self.button = TextIconButton(
            icon=ft.Image(src="ui/right_arrow.png", width=10),
            width=150,
            height=50,
            text="Далее",
            text_style=wide_header
        )
        self.btn_container = ft.Container(
                                content=self.button,
                                height=button_size,
                                alignment=ft.alignment.center_right,
                                margin=ft.margin.only(top=40),
                            )

        self.expand = True
        self.controls = [
            PageLayout(
                content=ft.Column(

                    controls=[
                        ft.Column(
                            controls=[
                                ft.Container(
                                    self.text,
                                    alignment=ft.alignment.center,
                                ),
                                self.choose,
                                ft.Container(
                                    self.text2,
                                    alignment=ft.alignment.center,
                                ),
                            ],
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        
                        self.btn_container

                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=30,
                ),
            )
        ]

    def get_input_data(self):
        return self.choose.get_current_image_id()

    def get_info(self):
        return "EmojiForm"
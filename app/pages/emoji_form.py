import flet as ft
from buttons.image_button import ImageButton
from layouts.main_layout import PageLayout
from elements.choose_option import ChooseOption
from enum import Enum
from pages.form_page import FormPage
from buttons.text_icon_button import TextIconButton
from styles.text import *

class EmojisFeelings(Enum):
    LOVED = "loved"
    FUNNY = "funny"
    ANGEL = "angel"
    CHILL = "chill"
    COOL = "cool"
    YAMMY = "yammy"
    OK = "ok"
    WTF = "wtf"
    SLEEPY = "sleepy"
    NOCOMMENTS = "nocomments"
    DRUNK = "drunk"
    DISCONTENT = "discontent"
    PLSNO = "plsno"
    SCARY = "scary"
    TIRED = "tired"
    BAD = "bad"
    FUCK = "fuck"

FEELING_LIST = [
        {
            "id": EmojisFeelings.LOVED.value,
            "src": "ui/feelings/loved.png",
        },
        {
            "id": EmojisFeelings.FUNNY.value,
            "src": "ui/feelings/funny.png",
        },
        {
            "id": EmojisFeelings.ANGEL.value,
            "src": "ui/feelings/angel.png",
        },
        {
            "id": EmojisFeelings.CHILL.value,
            "src": "ui/feelings/chill.png",
        },
        {
            "id": EmojisFeelings.COOL.value,
            "src": "ui/feelings/cool.png",
        },
        {
            "id": EmojisFeelings.YAMMY.value,
            "src": "ui/feelings/yammy.png",
        },
        {
            "id": EmojisFeelings.OK.value,
            "src": "ui/feelings/ok.png",
        },
        {
            "id": EmojisFeelings.WTF.value,
            "src": "ui/feelings/wtf.png",
        },
        {
            "id": EmojisFeelings.SLEEPY.value,
            "src": "ui/feelings/sleepy.png",
        },
        {
            "id": EmojisFeelings.NOCOMMENTS.value,
            "src": "ui/feelings/noComments.png",
        },
        {
            "id": EmojisFeelings.DRUNK.value,
            "src": "ui/feelings/drunk.png",
        },
        {
            "id": EmojisFeelings.DISCONTENT.value,
            "src": "ui/feelings/discontent.png",
        },
        {
            "id": EmojisFeelings.PLSNO.value,
            "src": "ui/feelings/plsNo.png",
        },
        {
            "id": EmojisFeelings.SCARY.value,
            "src": "ui/feelings/scary.png",
        },
        {
            "id": EmojisFeelings.TIRED.value,
            "src": "ui/feelings/tired.png",
        },
        {
            "id": EmojisFeelings.BAD.value,
            "src": "ui/feelings/bad.png",
        },
        {
            "id": EmojisFeelings.FUCK.value,
            "src": "ui/feelings/fuck.png",
        }
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
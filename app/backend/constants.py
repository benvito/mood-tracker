from enum import Enum


# Enum для смайлов
class EmojisFeelings(Enum):
    LOVED = ("loved", "ui/feelings/loved.png")
    FUNNY = ("funny", "ui/feelings/funny.png")
    ANGEL = ("angel", "ui/feelings/angel.png")
    CHILL = ("chill", "ui/feelings/chill.png")
    COOL = ("cool", "ui/feelings/cool.png")
    YAMMY = ("yammy", "ui/feelings/yammy.png")
    OK = ("ok", "ui/feelings/ok.png")
    WTF = ("wtf", "ui/feelings/wtf.png")
    SLEEPY = ("sleepy", "ui/feelings/sleepy.png")
    NOCOMMENTS = ("nocomments", "ui/feelings/noComments.png")
    DRUNK = ("drunk", "ui/feelings/drunk.png")
    DISCONTENT = ("discontent", "ui/feelings/discontent.png")
    PLSNO = ("plsno", "ui/feelings/plsNo.png")
    SCARY = ("scary", "ui/feelings/scary.png")
    TIRED = ("tired", "ui/feelings/tired.png")
    BAD = ("bad", "ui/feelings/bad.png")
    FUCK = ("fuck", "ui/feelings/fuck.png")

    def __init__(self, id, src):
        self.id = id
        self.src = src
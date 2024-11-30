from enum import Enum

AVG_DAY_KEY = "avg_day"
AVG_SLEEP_KEY = "avg_sleep"
AVG_HAPPY_KEY = "avg_happy"
AVG_TIRED_KEY = "avg_tired"
AVG_EMOJI_KEY = "avg_emoji"

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
    QUESTION = ("question", "ui/feelings/question.png")

    def __init__(self, id, src):
        self.id = id
        self.src = src

    @classmethod
    def get_src_by_id(cls, id):
        for emoji in cls:
            if emoji.id == id:
                return emoji.src
        raise ValueError(f"No emoji found with id '{id}'")
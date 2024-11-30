
class AvgScore(float):
    def __new__(cls, value):
        # Создаем объект float через __new__
        return super(AvgScore, cls).__new__(cls, value)

    def percent(self):
        # Возвращаем процентное представление числа
        return AvgScore(self * 100)

    def to_int(self):
        # Возвращаем целое число
        return int(self)

    def score10(self):
        # Возвращаем целое число от 0 до 10
        return int(self * 10)

    def __str__(self):
        # Возвращаем строковое представление числа
        return f"{self:.2f}"  # Два знака после запятой

    def __repr__(self):
        # Для repr выводим значение числа как оно есть
        return f"AvgScore({float(self):.2f})"


class Scores:
    def __init__(self,
                 avg_day: float,
                 avg_sleep: float,
                 avg_happy: float,
                 avg_tired: float,
                 avg_emoji: list):
        self.avg_day = AvgScore(avg_day)
        self.avg_sleep = AvgScore(avg_sleep)
        self.avg_happy = AvgScore(avg_happy)
        self.avg_tired = AvgScore(avg_tired)
        self.avg_emoji = avg_emoji
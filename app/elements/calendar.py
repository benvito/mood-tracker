import datetime, calendar
import flet
import copy


class CustomCalendar(flet.Container):
    _current_month = datetime.date.today().month
    _current_year = datetime.date.today().year
    _current_day = datetime.date.today().day
    _first_day_in_month, _last_day_in_month = calendar.monthrange(_current_year, _current_month)
    _day_of_week = {0: "ПН", 1: "ВТ", 2: "СР", 3: "ЧТ", 4: "ПТ", 5: "СБ", 6: "ВС"}
    _months = {1: "ЯНВАРЬ", 2: "ФЕВРАЛЬ", 3: "МАРТ", 4: "АПРЕЛЬ", 5: "МАЙ", 6: "ИЮНЬ",
               7: "ИЮЛЬ", 8: "АВГУСТ", 9: "СЕНТЯБРЬ", 10: "ОКТЯБРЬ", 11: "НОЯБРЬ", 12: "ДЕКАБРЬ"}

    def __init__(self, width: int, bgcolor="#e2e2e2",
                 font_color="#3c4457", font_color_accent="#ffffff",
                 accent_color="#108ef2", header_font_color="#d2334c",
                 hover_color="#eeeeee", border_radius=15,
                 day_radius=15,
                 day_inactive_color="#110F15",
                 change_month=lambda month, year: None,
                 daily_data=None
                 ):

        self.day_spacing = width * 0.02
        
        super().__init__(
            # ширина виджета задаётся пользователем
            width=width,
            # высота считается автоматом, заголовок = width / 7, строка = width / 8
            # весь календарь это таблица 2 заголовочные строки + 5 строк на даты, ~0.5 на отступы
            height=(width / 8 * 5 + width / 7 * 2.5) + (self.day_spacing * 5),
            border_radius=border_radius,
            padding=flet.padding.only(0, width * 0.08, 0, 0),
            bgcolor=bgcolor,
            alignment=flet.alignment.center
        )
        self.font_color = font_color
        self.header_font_color = header_font_color
        self.accent_color = accent_color
        self.hover_color = hover_color
        self.font_accent_color = font_color_accent
        self.font_size = width * 0.045
        self.day_radius = day_radius
        self.day_inactive_color = day_inactive_color
        self.daily_data = daily_data
        self.event_change_month = change_month

        self.content = self._draw_base()

    def update_daily_data(self, data):
        self.daily_data = data
        self._update_days_colors()

    def _get_day_color(self, avg_rating):
        if avg_rating == -1:
            background_color = self.day_inactive_color
        elif avg_rating >= 0 and avg_rating <= 0.15:
            background_color = "#ff4f16"
        elif avg_rating > 0.15 and avg_rating <= 0.30:
            background_color = "#ff8f16"
        elif avg_rating > 0.30 and avg_rating <= 0.45:
            background_color = "#ffbf16"
        elif avg_rating > 0.45 and avg_rating <= 0.60:
            background_color = "#fff016"
        elif avg_rating > 0.60 and avg_rating <= 0.75:
            background_color = "#b8c32c"
        elif avg_rating > 0.75 and avg_rating <= 0.90:
            background_color = "#aac72c"
        elif avg_rating > 0.90 and avg_rating <= 1:
            background_color = "#91cf2b"
        
        # Получаем цвет текста, контрастный, но похожий на фон
        text_color = self._adjust_brightness(background_color, 0.72)
        return background_color, text_color

    def _adjust_brightness(self, hex_color, factor):
        """
        Изменяет яркость цвета: делает светлее или темнее в зависимости от фона.
        :param hex_color: Цвет в формате HEX (например, "#ff4f16")
        :param factor: Коэффициент изменения яркости (-1.0 для затемнения, +1.0 для осветления)
        :return: Новый цвет в формате HEX
        """
        # Преобразуем HEX в RGB
        hex_color = hex_color.lstrip("#")
        r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)

        # Рассчитываем новый цвет, изменяя яркость
        def adjust(c, factor):
            return max(0, min(255, int(c + (255 - c) * factor if factor > 0 else c * (1 + factor))))

        if self._is_bright(r, g, b):
            # Если фон яркий, затемняем текст
            r, g, b = adjust(r, -factor), adjust(g, -factor), adjust(b, -factor)
        else:
            # Если фон тёмный, осветляем текст
            r, g, b = adjust(r, factor), adjust(g, factor), adjust(b, factor)

        # Преобразуем RGB обратно в HEX
        return f"#{r:02x}{g:02x}{b:02x}"

    def _is_bright(self, r, g, b):
        """
        Проверяет, является ли цвет ярким.
        :param r: Компонента красного (0-255)
        :param g: Компонента зелёного (0-255)
        :param b: Компонента синего (0-255)
        :return: True, если цвет яркий, иначе False
        """
        brightness = (r * 0.299 + g * 0.587 + b * 0.114) / 255
        return brightness > 0.5

    def _update_days_colors(self, custom_calendar=None):
        if custom_calendar is None:
            custom_calendar = self.content
        calend = custom_calendar.controls
            
        for row_id, row in enumerate(calend):
            # первые две строки это заголовки календаря
            if row_id < 2:
                continue
            for column_id, column in enumerate(row.controls):
                if row_id - 2 == 0 and column_id < self._first_day_in_month:
                    column.bgcolor = self.day_inactive_color
                else:
                    # если нам попалось '-' то скипаем
                    try:
                        isNum = int(column.content.value)
                    except ValueError:
                        column.bgcolor = self.day_inactive_color
                        continue

                    try:
                        day_rating = self.daily_data[f'{int(column.content.value):02}']
                    except KeyError:
                        day_rating = -1


                    column.bgcolor, column.content.color = self._get_day_color(day_rating)

    def _create_day_container(self):
        day_container = flet.Container(
            content=flet.Text(
                value="",
                text_align=flet.TextAlign.CENTER,
                weight=flet.FontWeight.W_500,
                size=self.font_size + 2,
                color=self.font_color
            ),
            width=(self.width - self.width * 0.05) / 8,
            height=self.width / 8,
            alignment=flet.alignment.center,
            # shape=flet.BoxShape.CIRCLE,
            bgcolor=self.day_inactive_color,
            on_hover=self._on_hover_date,
            border_radius=self.day_radius,
            data=""
        )

        return day_container
    def _draw_base(self):
        
        day_container = self._create_day_container()
        custom_calendar = flet.Column(
            controls=[
                # заголовок с названием месяца и годом, кнопками для перелистывания календаря
                flet.Row(
                    controls=[
                        flet.Container(flet.IconButton(
                            icon=flet.icons.KEYBOARD_ARROW_LEFT_SHARP,
                            height=self.width / 11,
                            width=self.width / 7,
                            icon_size=self.font_size,
                            padding=0,
                            icon_color=self.font_color,
                            data="left_flip",
                            on_click=self._flip_calendar
                        ),
                            height=self.width / 8,
                            alignment=flet.alignment.center
                        ),
                        flet.Container(flet.Text(
                            # value=str(self._months.get(self._current_month)) + " ",
                            value="",
                            spans=[
                                flet.TextSpan("",
                                              flet.TextStyle(weight=flet.FontWeight.BOLD))
                                ],
                            weight=flet.FontWeight.W_400,
                            color=self.font_color,
                            size=self.font_size + 2,
                            text_align=flet.alignment.center,
                        ),
                            height=self.width / 8,
                            alignment=flet.alignment.center
                        ),
                        flet.Container(flet.IconButton(
                            icon=flet.icons.KEYBOARD_ARROW_RIGHT_SHARP,
                            icon_size=self.font_size,
                            height=self.width / 10,
                            width=self.width / 7,
                            padding=0,
                            data="right_flip",
                            on_click=self._flip_calendar,
                            icon_color=self.font_color
                        ),
                            height=self.width / 8,
                            alignment=flet.alignment.center
                        ),
                    ],
                    alignment=flet.MainAxisAlignment.CENTER,
                    vertical_alignment=flet.CrossAxisAlignment.START,
                ),
                # заголовок с днями недели
                flet.Row(
                    controls=[
                        flet.Text(
                            value=self._day_of_week.get(i),
                            text_align=flet.TextAlign.CENTER,
                            width=(self.width - self.width * 0.08) / 7.8,
                            weight=flet.FontWeight.W_400,
                            size=self.font_size,
                            color=self.header_font_color,
                            height=self.width / 8,
                        ) for i in range(0, 7)
                    ],
                    alignment=flet.MainAxisAlignment.CENTER,
                    height=self.width / 10,
                    # убирает лишние отступы между элементами Row
                    spacing=self.day_spacing
                ),
                # пять строк на даты, создаём их и распаковываем в controls
                *[flet.Row(
                    controls=[self._create_day_container() for i in range(0, 7)],
                    alignment=flet.MainAxisAlignment.CENTER,
                    spacing=self.day_spacing
                ) for i in range(0, 5)],
            ],
            # убирает лишние отступы между элементами Column
            spacing=self.day_spacing,
        )
        self._fill_dates(custom_calendar)
        self._update_days_colors(custom_calendar)
        return custom_calendar

    def _fill_dates(self, custom_calendar):
        day_counter = 1
        self._first_day_in_month, self._last_day_in_month = calendar.monthrange(self._current_year, self._current_month)
        custom_calendar.controls[0].controls[1].content.value = self._months.get(self._current_month)
        custom_calendar.controls[0].controls[1].content.spans[0].text = " " + str(self._current_year)
        for row_id, row in enumerate(custom_calendar.controls):
            # первые две строки это заголовки календаря
            if row_id < 2:
                continue
            for column_id, column in enumerate(row.controls):
                if row_id - 2 == 0 and column_id < self._first_day_in_month:
                    column.content.value = "ꟷ"
                    column.content.weight=flet.FontWeight.W_200
                    column.bgcolor = self.day_inactive_color
                elif self._last_day_in_month >= day_counter:
                    column.content.value = str(day_counter)
                    column.content.weight = flet.FontWeight.W_500
                    if day_counter == self._current_day and self._current_month == CustomCalendar._current_month \
                            and self._current_year == CustomCalendar._current_year:
                        column.bgcolor = self.accent_color
                        column.content.color = self.font_color
                        column.data = "today"
                    else:
                        # column.bgcolor = self.bgcolor
                        column.bgcolor = flet.colors.AMBER
                        column.content.color = self.font_color
                        column.data = "just_a_day"
                    day_counter += 1
                else:
                    column.content.value = "ꟷ"
                    column.content.weight = flet.FontWeight.W_200
                    column.bgcolor = self.day_inactive_color

    def _on_hover_date(self, e: flet.ControlEvent):
        # Когда мышь на элементе e.data = "true"
        # e.control.bgcolor = self.hover_color if e.data == "true" and e.control.data != "today" else \
        #     (self.accent_color if e.control.data == "today" else self.bgcolor)
        # e.control.update()
        pass

    def _flip_calendar(self, e: flet.ControlEvent):
        if e.control.data == "left_flip":
            if self._current_month - 1 > 0:
                self._current_month = self._current_month - 1
            else:
                self._current_month = 12
                self._current_year = self._current_year - 1
        elif e.control.data == "right_flip":
            if self._current_month + 1 <= 12:
                self._current_month = self._current_month + 1
            else:
                self._current_month = 1
                self._current_year = self._current_year + 1
        self._fill_dates(self.content)
        self.event_change_month(self._current_month, self._current_year)
        self.content.update()

    @property
    def current_month(self):
        return self._current_month
    
    @property
    def current_year(self):
        return self._current_year
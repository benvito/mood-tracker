import sqlite3
from datetime import datetime
from backend import *
from backend.db import queries 
from backend.db.entities import *
import logging


class DatabaseController:
    def __init__(self, db_name='mood_tracker.db'):
        # if os.path.exists(db_name) == False:
        #     os.mkdir('data')
        self.connection = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.create_table()
        self.create_and_fill_quotes()
        self.create_and_fill_greetings()

    def create_and_fill_greetings(self):
        self.cursor.execute(queries.CREATE_TABLE_GREETINGS)
        self.cursor.execute(queries.INSERT_GREETINGS)
        self.connection.commit()

    def create_and_fill_quotes(self):
        self.cursor.execute(queries.CREATE_QUOTES_TABLE)
        self.cursor.execute(queries.INSERT_QUOTES)
        self.connection.commit()

    def create_table(self):
        self.cursor.execute(queries.CREATE_TABLE_QUERY)
        self.connection.commit()

    def add_record(self, sleep_quality, fatigue, happiness, daily_experience, emoji_id):
        date = datetime.now().isoformat()
        self.cursor.execute(queries.INSERT_RECORD_QUERY, (date, sleep_quality, fatigue, happiness, daily_experience, emoji_id))  # Используем импортированный запрос
        self.connection.commit()

    def aggregate_data(self) -> Scores:
        self.cursor.execute(queries.AGGREGATE_DATA_QUERY)
        data = self.cursor.fetchone()

        logging.info(f"Get aggregate data: {data}")

        # Если данных нет (например, за неделю не было записей)
        if not data or data[0] is None:
            logging.warning("No data found for the all period.")
            return None

        scores = Scores(
            avg_sleep=data[0],
            avg_tired=data[1],
            avg_happy=data[2],
            avg_day=data[3],
            avg_emoji=data[4].split(",")
        )

        return scores

    def aggregate_weekly_data(self) -> Scores:
        self.cursor.execute(queries.AGGREGATE_WEEKLY_DATA_QUERY)
        data = self.cursor.fetchone()

        logging.info(f"Get weekly aggregate data: {data}")

        # Если данных нет (например, за неделю не было записей)
        if not data or data[0] is None:
            logging.warning("No data found for the last week.")
            return None

        # Преобразуем результат в объект Scores
        scores = Scores(
            avg_sleep=data[0],
            avg_tired=data[1],
            avg_happy=data[2],
            avg_day=data[3],
            avg_emoji=data[4].split(",") if data[4] else []
        )

        return scores
    
    def get_daily_average_scores(self, month: int, year: int):
        query = queries.GET_AVG_DAYS_FOR_MONTH_YEAR
        month_str = f"{month:02}"
        year_str = str(year)

        self.cursor.execute(query, (month_str, year_str))
        results = self.cursor.fetchall()

        # Преобразуем результат в удобный формат
        daily_scores = {row[0]: row[1] for row in results}
        logging.info(f"Daily average scores for {month_str}/{year_str}: {daily_scores}")
        try:
            print(daily_scores["1"])
        except:
            pass
        return daily_scores

    def get_random_quote(self):
        self.cursor.execute(queries.GET_RANDOM_QUOTE)
        quote = self.cursor.fetchone()[0]
        logging.info(f"Get random quote: {quote}")
        return f'"{quote}"'

    def get_random_greeting(self):
        self.cursor.execute(queries.GET_RANDOM_GREETING)
        greeting = self.cursor.fetchone()[0]
        logging.info(f"Get random greeting: {greeting}")
        return greeting

    def close(self):
        self.connection.close()
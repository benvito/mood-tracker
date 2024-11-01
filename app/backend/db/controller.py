import sqlite3
from datetime import datetime
from backend import *
from backend.db import queries 


class DatabaseController:
    def __init__(self, db_name='./app/backend/db/data/mood_tracker.db'):
        self.connection = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute(queries.CREATE_TABLE_QUERY)
        self.connection.commit()

    def add_record(self, sleep_quality, fatigue, happiness, daily_experience, emoji_id):
        date = datetime.now().isoformat()
        self.cursor.execute(queries.INSERT_RECORD_QUERY, (date, sleep_quality, fatigue, happiness, daily_experience, emoji_id))  # Используем импортированный запрос
        self.connection.commit()

        self.cursor.execute(
            '''
            SELECT * FROM mood_records;
'''
        )
        print(self.cursor.fetchall())

    def aggregate_data(self):
        self.cursor.execute(queries.AGGREGATE_DATA_QUERY)
        return self.cursor.fetchone()

    def close(self):
        self.connection.close()
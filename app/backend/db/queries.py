# queries.py

CREATE_TABLE_QUERY = '''
    CREATE TABLE IF NOT EXISTS mood_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        sleep_quality INTEGER CHECK(sleep_quality BETWEEN 0 AND 100),
        fatigue INTEGER CHECK(fatigue BETWEEN 0 AND 100),
        happiness INTEGER CHECK(happiness BETWEEN 0 AND 100),
        daily_experience INTEGER CHECK(daily_experience BETWEEN 0 AND 100),
        emoji_id TEXT NOT NULL
    )
'''

INSERT_RECORD_QUERY = '''
    INSERT INTO mood_records (date, sleep_quality, fatigue, happiness, daily_experience, emoji_id)
    VALUES (?, ?, ?, ?, ?, ?)
'''

AGGREGATE_DATA_QUERY = '''
    SELECT 
        AVG(sleep_quality) AS avg_sleep_quality,
        AVG(fatigue) AS avg_fatigue,
        AVG(happiness) AS avg_happiness,
        AVG(daily_experience) AS avg_daily_experience
    FROM mood_records
'''

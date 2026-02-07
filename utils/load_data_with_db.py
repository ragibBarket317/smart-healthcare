import sqlite3
import os

class DataLoadWithDB:
    def __init__(self, data_path="database/smart_health.db"):
        self.data_path = data_path
        self.conn = sqlite3.connect(self.data_path)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetch_all(self, query, params=()):
        res = self.cursor.execute(query, params)
        rows = res.fetchall()
        return [dict(row) for row in rows]
    
    def fetch_one(self, query, params=()):
        res = self.cursor.execute(query, params)
        row = res.fetchone()
        return dict(row) if row else None

        
        
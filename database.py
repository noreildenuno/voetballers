import sqlite3
from pathlib import Path


class Database:
    def __init__(self, db_pad="data/voetballers.db"):
        Path("data").mkdir(exist_ok=True)
        self.verbinding = sqlite3.connect(db_pad)
        self.maken_tabellen()

    def maken_tabellen(self):
        cursor = self.verbinding.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS posities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                naam TEXT NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS spelers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                naam TEXT NOT NULL,
                leeftijd INTEGER,
                club TEXT,
                positie_id INTEGER,
                waarde INTEGER,
                FOREIGN KEY(positie_id) REFERENCES posities(id)
            )
        """)
        self.verbinding.commit()

    def krijg_verbinding(self):
        return self.verbinding

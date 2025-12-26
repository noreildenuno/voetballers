import sqlite3
from pathlib import Path


class Database:
    def __init__(self, db_pad="data/voetballers.db"):
        Path("data").mkdir(exist_ok=True)
        self.verbinding = sqlite3.connect(db_pad)
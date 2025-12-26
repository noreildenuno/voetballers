import sqlite3
from models import Speler, Positie

class Repository:
    def __init__(self, db_verbinding):
        self.verbinding = db_verbinding

    def init_standaard_posities(self):
        cursor = self.verbinding.cursor()
        cursor.execute("SELECT COUNT(*) FROM posities")
        if cursor.fetchone()[0] == 0:
            for pos in ["Keeper", "Verdediger", "Middenvelder", "Aanvaller"]:
                cursor.execute("INSERT INTO posities(naam) VALUES (?)", (pos,))
        self.verbinding.commit()

    def voeg_speler_toe(self, naam, leeftijd, club, positie_id, waarde):
        cursor = self.verbinding.cursor()
        cursor.execute(
            "INSERT INTO spelers(naam, leeftijd, club, positie_id, waarde) VALUES (?, ?, ?, ?, ?)",
            (naam, leeftijd, club, positie_id, waarde)
        )
        self.verbinding.commit()

    def krijg_alle_spelers(self):
        cursor = self.verbinding.cursor()
        cursor.execute("""
            SELECT id, naam, leeftijd, club, positie_id, waarde
            FROM spelers
        """)
        rijen = cursor.fetchall()
        return [Speler(*rij) for rij in rijen]

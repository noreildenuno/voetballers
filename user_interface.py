from repository import Repository
from models import Speler, Positie
import csv


class GebruikersInterface:
    def __init__(self, repo: Repository):
        self.repo = repo

    def menu(self):
        while True:
            print("\n--- Voetballers Manager ---")
            print("1. Voeg speler toe")
            print("2. Toon alle spelers")
            print("3. Zoek speler")
            print("4. Export CSV")
            print("5. Stoppen")

            keuze = input("Kies een optie: ")

            if keuze == "1":
                self.voeg_speler_ui()
            elif keuze == "2":
                self.toon_alle_spelers_ui()
            elif keuze == "3":
                self.zoek_speler_ui()
            elif keuze == "4":
                self.export_csv()
            elif keuze == "5":
                break
            else:
                print("Ongeldige keuze!")
                
    def voeg_speler_ui(self):
        naam = input("Naam: ")
        leeftijd = int(input("Leeftijd: "))
        club = input("Club: ")
        positie_id = int(input("Positie ID (1=Keeper, 2=Verdediger, 3=Middenvelder, 4=Aanvaller): "))
        waarde = int(input("Waarde (€): "))
        self.repo.voeg_speler_toe(naam, leeftijd, club, positie_id, waarde)
        print("Speler toegevoegd!")

    def toon_alle_spelers_ui(self):
        spelers = self.repo.krijg_alle_spelers()
        if not spelers:
            print("Geen spelers gevonden.")
        for s in spelers:
            print(s)



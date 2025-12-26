class Speler:
    def __init__(self, id, naam, leeftijd, club, positie_id, waarde):
        self.id = id
        self.naam = naam
        self.leeftijd = leeftijd
        self.club = club
        self.positie_id = positie_id
        self.waarde = waarde

    def __repr__(self):
        return f"Speler({self.id}, '{self.naam}', {self.leeftijd}, '{self.club}', positie_id={self.positie_id}, waarde={self.waarde})"
    
class Positie:
    def __init__(self, id, naam):
        self.id = id
        self.naam = naam

    def __repr__(self):
        return f"Positie({self.id}, '{self.naam}')"

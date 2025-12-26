\# Voetballers Manager

Dit is mijn Python-programma om een database van voetballers te beheren met behulp van SQLite.



\## Beschrijving

Met dit programma kun je:

\* \*\*Spelers beheren\*\*: Nieuwe spelers toevoegen aan de database.

\* \*\*Overzichten\*\*: Alle opgeslagen spelers bekijken.

\* \*\*Zoekfunctie\*\*: Spelers opzoeken op basis van hun naam.

\* \*\*Data Export\*\*: Spelers exporteren naar een CSV-bestand voor gebruik in Excel.



De gegevens worden veilig opgeslagen in een SQLite-database: `data/voetballers.db`.



\## Installatie

1\. Zorg dat Python 3.x geïnstalleerd is op je systeem.  

2\. (Optioneel) Maak een virtuele omgeving aan en activeer deze:

&nbsp;  ```bash

&nbsp;  python -m venv venv

&nbsp;  # Windows:

&nbsp;  venv\\Scripts\\activate

&nbsp;  # macOS/Linux:

&nbsp;  source venv/bin/activate



Let op: Er zijn geen extra libraries nodig; SQLite zit standaard in de Python Standard Library.



\## Gebruik

1. Open de projectmap in je terminal (rechtermuisknop in de map voetballers en open terminal).

2\. Start het hoofdprogramma:



&nbsp;  ```bash

&nbsp;  python main.py





Volg de instructies in het interactieve menu:



\[1] Voeg speler toe



\[2] Toon alle spelers



\[3] Zoek speler



\[4] Export CSV



\[5] Stoppen







Projectstructuur

main.py: Het startpunt van de applicatie.



database.py: Verantwoordelijk voor de initialisatie van de database.



models.py: Bevat de klassen Speler en Positie.



repository.py: De logica voor database-interactie (CRUD).



user\_interface.py: Beheert de menu-interactie met de gebruiker.



Auteur:

Nuno Noreilde (2CYB)


from database import Database
from repository import Repository
from user_interface import GebruikersInterface

def main():
    db = Database()
    repo = Repository(db.krijg_verbinding())
    ui = GebruikersInterface(repo)
    ui.menu()

if __name__ == "__main__":
    main()

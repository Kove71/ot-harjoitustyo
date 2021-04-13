import os

# Sisältää kovakoodatun polun tietokantaan. Omaa testaus- ja koodauskäyttöä varten tarkistaa jos nykyinen working dir on src-hakemistossa

if os.environ["PWD"] == "/home/kostives/ot-harjoitustyo/src":
    database_file_path = "../data/database.db"
else:
    database_file_path = "data/database.db"

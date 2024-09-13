import sqlite3
from pprint import pprint

conn = sqlite3.connect("newdatabase.db") #adatbázis létrehozása
curs = conn.cursor()  #ezzel tudjuk az sql parancsokat beírni az adatbázisba
curs.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")

curs.execute("INSERT INTO users VALUES ('John', 'abc123')")
#conn.commit()

curs.execute("SELECT * FROM users")
adatok = curs.fetchall()#vissza adja az adatokat a felhasznalok tablabol
pprint(adatok)

conn.close()
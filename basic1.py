import sqlite3
from pprint import pprint

conn = sqlite3.connect("database.db") #adatbázis létrehozása
curs = conn.cursor()  #ezzel tudjuk az sql parancsokat beírni az adatbázisba
curs.execute("CREATE TABLE IF NOT EXISTS felhasznalok (nev TEXT, kor INTEGER, nem TEXT, pontszam REAL)") #tábla létrehozása az adatbázisban
curs.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, age INTEGER, gender TEXT, score REAL)") #tábla létrehozása az adatbázisban
#curs.execute("INSERT INTO felhasznalok VALUES ('Erika', 28, 'no', 8.1)")
# curs.execute("INSERT INTO felhasznalok VALUES ('Evi', 32, 'no', 9.3)")
# curs.execute("INSERT INTO felhasznalok VALUES ('Zoli', 41, 'ferfi', 6.1)")
# curs.execute("INSERT INTO felhasznalok VALUES ('Pista', 22, 'ferfi', 7.1)")

# curs.execute("INSERT INTO users VALUES ('John', 21, 'man', 5.1)")
# curs.execute("INSERT INTO users VALUES ('Laura', 28, 'woman', 6.1)")
# curs.execute("INSERT INTO users VALUES ('Adam', 31, 'man', 7.1)")
# curs.execute("INSERT INTO users VALUES ('Kitty', 38, 'woman', 8.1)")


#curs.execute("SELECT nev, pontszam FROM felhasznalok WHERE ROWID=1")
#curs.execute("UPDATE felhasznalok SET nem=? WHERE nem=?",("nő", "no"))
#curs.execute("UPDATE felhasznalok SET nem=? WHERE nem=?",("férfi", "ferfi"))
# curs.execute("UPDATE users SET gender=? WHERE gender=?",("male", "man"))
# curs.execute("UPDATE users SET gender=? WHERE gender=?",("female", "woman"))
# conn.commit()

# curs.execute("INSERT INTO felhasznalok VALUES ('Istvan', 23, 'ferfi', 4.1)")
# conn.commit()

curs.execute("DELETE FROM felhasznalok WHERE pontszam < 7.1")
conn.commit()

curs.execute("SELECT * FROM felhasznalok")

adatok = curs.fetchall()#vissza adja az adatokat a felhasznalok tablabol
pprint(adatok)

#conn.commit() #adatbázisban elmenti a változást
conn.close()

import sqlite3
import Contents.cube_and_cards

def save(s: Contents.cube_and_cards.Cube):
    db = sqlite3.connect(f"src/entities/Saved_Cubes/{s.name}.db")
    db.isolation_level = None
    db.execute("CREATE TABLE Cards (id INTEGER PRIMARY KEY, name TEXT, cmc INTEGER, type TEXT);") #Alusta cube
    for i in s.collection:
        db.execute("INSERT INTO Cards (name, cmc, type) VALUES (?,?,?);",[i.name, i.cmc, i.type])

def load(s: str):
    path = 'src/entities/Saved_Cubes/'+s
    pass

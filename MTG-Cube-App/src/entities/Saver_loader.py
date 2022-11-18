
import sqlite3
import cube_and_cards

def save(s: cube_and_cards.Cube):
    db = sqlite3.connect(f"src/entities/Saved_Cubes/{s.name}.db")
    db.isolation_level = None
    db.execute("CREATE TABLE Cards (id INTEGER PRIMARY KEY, name TEXT, colors TEXT, color_identity TEXT, cmc INTEGER, mana_cost TEXT, type TEXT, keywords TEXT, oracle TEXT, image_uri TEXT);") #Alusta cube
    for i in s.collection:
        db.execute("INSERT INTO Cards (name, colors, color_identity, cmc, mana_cost, type, keywords, oracle, image_uri) VALUES (?,?,?,?,?,?,?,?,?);",[
                i.name,
                str(i.colors),
                str(i.color_id),
                i.cmc,
                str(i.mana_cost),
                i.type,
                str(i.keywords),
                i.text,
                i.img_uri
                ])

def load(s: str):
    path = 'src/entities/Saved_Cubes/'+s+".db"
    print(path)
    pass

#load("koff")

#db.execute("CREATE TABLE Cards (id INTEGER PRIMARY KEY, name TEXT, colors TEXT, color_identity TEXT, cmc INTEGER, mana_cost TEXT, type TEXT, keywords TEXT, oracle TEXT, image_uri TEXT );")
            
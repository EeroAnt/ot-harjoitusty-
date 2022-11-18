import sqlite3
import cube_and_cards
import Card_lists.Card_list_lister as lister

def save(s: cube_and_cards.Cube):
    db = sqlite3.connect(f"src/entities/Saved_Cubes/{s.name}.db")
    db.isolation_level = None
    db.execute("CREATE TABLE Cards (id INTEGER PRIMARY KEY, name TEXT, colors TEXT, color_identity TEXT, cmc INTEGER, mana_cost TEXT, type TEXT, keywords TEXT, oracle TEXT, image_uri TEXT, p/t TEXT);") #Alusta cube
    for i in s.collection:
        db.execute("INSERT INTO Cards (name, colors, color_identity, cmc, mana_cost, type, keywords, oracle, image_uri) VALUES (?,?,?,?,?,?,?,?,?,?);",[
                i.name,
                str(i.colors),
                str(i.color_id),
                i.cmc,
                str(i.mana_cost),
                i.type,
                str(i.keywords),
                i.text,
                i.img_uri,
                i.pt
                ])

def load(s: str):
    path = 'src/entities/Saved_Cubes/'+s+".db"
    db = sqlite3.connect(path)
    db.isolation_level = None
    list_of_cards = db.execute("SELECT * FROM Cards").fetchall()
    if list_of_cards == None:
        print("Tällä nimellä ei löytynyt Cubea")
    else:
        loaded_cube = cube_and_cards.Cube(s)
        for i in list_of_cards:
            loaded_cube.add_card(i[1])
        return loaded_cube

def load_from_list(name_of_cube, name_of_txt_file):
    cube_from_txt_file = cube_and_cards.Cube(name_of_cube)
    card_list = lister.lister(name_of_txt_file)
    for i in card_list:
        cube_from_txt_file.add_card(i)
    return cube_from_txt_file


#load("koff")

# db = sqlite3.connect(f"src/entities/fetched_cards/fetched_cards.db")
# db.isolation_level = None
# db.execute("CREATE TABLE Cards (id INTEGER PRIMARY KEY, name TEXT, colors TEXT, color_identity TEXT, cmc INTEGER, mana_cost TEXT, type TEXT, keywords TEXT, oracle TEXT, image_uri TEXT, p_t TEXT );")

# load("Pallo")
# load_from_list("testi","Testilista.txt")
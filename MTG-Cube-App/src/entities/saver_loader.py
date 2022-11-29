import sqlite3
from entities.cube_and_cards import Cube
import entities.card_lists.card_list_lister as lister
import os

def save(name_of_cube: Cube):
    if os.path.exists(f"src/entities/Saved_Cubes/{name_of_cube.name}.db"):
        os.remove(f"src/entities/Saved_Cubes/{name_of_cube.name}.db")
    d_b = sqlite3.connect(f"src/entities/Saved_Cubes/{name_of_cube.name}.db")
    d_b.isolation_level = None
    # Alusta cube
    d_b.execute(
        "CREATE TABLE Cards (id INTEGER PRIMARY KEY, name TEXT, colors TEXT, "+
        "color_identity TEXT, cmc INTEGER, mana_cost TEXT, type TEXT, keywords"+
        " TEXT, oracle TEXT, image_uri TEXT, p_t TEXT);")
    for i in name_of_cube.collection:
        d_b.execute(
            "INSERT INTO Cards (name, colors, color_identity, cmc, mana_cost, "+
            "type, keywords, oracle, image_uri, p_t) VALUES (?,?,?,?,?,?,?,?,?,?);"
            , [
            i.name,
            str(i.colors),
            str(i.color_id),
            i.cmc,
            str(i.mana_cost),
            i.type,
            str(i.keywords),
            i.text,
            i.img_uri,
            i.p_t
        ])


def load(name_of_cube: str):
    path = 'src/entities/Saved_Cubes/'+name_of_cube+".db"
    d_b = sqlite3.connect(path)
    d_b.isolation_level = None
    list_of_cards = d_b.execute("SELECT * FROM Cards").fetchall()
    if list_of_cards is None:
        print("Tällä nimellä ei löytynyt Cubea")
        return False
    loaded_cube = Cube(name_of_cube)
    for i in list_of_cards:
        print(i)
        loaded_cube.add_card(i[1])
    return loaded_cube


def load_from_list(name_of_cube, name_of_txt_file):
    cube_from_txt_file = Cube(name_of_cube)
    card_list = lister.lister(name_of_txt_file)
    for i in card_list:
        cube_from_txt_file.add_card(i)
    cards_failed = []
    for i in card_list:
        if i not in cube_from_txt_file.card_names:
            cards_failed.append(i)
    print("Kortit, joiden lisääminen ei onnistunut:\n")
    for i in cards_failed:
        print(i)
    return cube_from_txt_file


# load("koff")

# db = sqlite3.connect(f"src/entities/fetched_cards/fetched_cards.db")
# db.isolation_level = None
# db.execute("CREATE TABLE Cards (id INTEGER PRIMARY KEY, name TEXT, colors TEXT, "
#    +"color_identity TEXT, cmc INTEGER, mana_cost TEXT, type TEXT, keywords TEXT, "+
#    "oracle TEXT, image_uri TEXT, p_t TEXT );")

# load("Pallo")
# load_from_list("testi","Testilista.txt")

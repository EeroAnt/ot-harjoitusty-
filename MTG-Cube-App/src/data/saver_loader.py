import sqlite3
import os
from entities.cube import Cube
from entities.card import card_test
import card_list_text_files.card_list_text_file_handler as lister

def save(name_of_cube: Cube):
    if os.path.exists(f"src/data/Saved_Cubes/{name_of_cube.name}.db"):
        os.remove(f"src/data/Saved_Cubes/{name_of_cube.name}.db")
    d_b = sqlite3.connect(f"src/data/Saved_Cubes/{name_of_cube.name}.db")
    d_b.isolation_level = None
    # Alusta cube
    d_b.execute(
        "CREATE TABLE Cards (id INTEGER PRIMARY KEY, name TEXT, colors TEXT, "+
        "color_identity TEXT, cmc INTEGER, mana_cost TEXT, type TEXT, keywords"+
        " TEXT, oracle TEXT, image_uri TEXT, power TEXT, toughness TEXT);")
    for i in name_of_cube.collection:
        d_b.execute(
            "INSERT INTO Cards (name, colors, color_identity, cmc, mana_cost, "+
            "type, keywords, oracle, image_uri, power, toughness) VALUES (?,?,?,?,?,?,?,?,?,?,?);"
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
            i.power,
            i.toughness
        ])


def load(name_of_cube: str):
    path = 'src/data/Saved_Cubes/'+name_of_cube+".db"
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
    cards_to_be_added = []
    failed_cards = []
    for i in card_list:
        if card_test(i):
            cards_to_be_added.append(i)
        else:
            failed_cards.append(i)
    for i in cards_to_be_added:
        cube_from_txt_file.add_card(i)
    print("Kortit, joiden lisääminen ei onnistunut:\n")
    for i in failed_cards:
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

import sqlite3
import os
from entities.cube import Cube
from entities.card import card_test
import card_list_text_files.card_list_text_file_handler as lister

# save()-funktio luo .db-tiedoston tallennettavasta cubesta
def save(name_of_cube: Cube):
    if os.path.exists(f"src/data/Saved_Cubes/{name_of_cube.name}.db"):
        os.remove(f"src/data/Saved_Cubes/{name_of_cube.name}.db")
    d_b = sqlite3.connect(f"src/data/Saved_Cubes/{name_of_cube.name}.db")
    d_b.isolation_level = None
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

# Käyttäjältä pyydetään vahvistus, jos on tallentamassa jo olemassaolevan cuben päälle
def confirm_before_overwriting(cube):
    if os.path.exists(f"src/data/Saved_Cubes/{cube.name}.db"):
        confirmation = input(
            "Tällä nimellä on jo cube olemassa. Haluatko"+
            " varmasti tallentaa sen päälle? Y/n: ")
        if confirmation == "Y":
            print("Tallennettu")
            os.remove(f"src/data/Saved_Cubes/{cube.name}.db")
            save(cube)
            print("Tallennettu")
        else:
            print("Ei tallennettu")
    else:
        save(cube)
        print("Tallennettu")

# load()-funktiolla ladataan käsiteltäväksi aiemmin tallennettu cube .db-tiedostosta
# tai palautetaan False, jos cubea ei löydetä.
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
        loaded_cube.add_card(i[1])
    return loaded_cube

# load_from_list()-funktio luo cuben tekstitiedoston sisällöstä ja tulostaa
# rivit, joita ei tunnistettu korteiksi, ja kortit, jotka olivat valmiiksi cubessa
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
    if len(failed_cards) != 0:
        print("Kortit, joiden lisääminen ei onnistunut:\n")
        for i in failed_cards:
            print(i)
    return cube_from_txt_file

from entities.cube import Cube
from user_interface.cube_ui import cube_ui
import data.saver_loader as saver
import os
INITIAL_ACTIONS = {
    1: "luo uusi cube",
    2: "lataa vanha cube",
    3: "luo cube tiedostosta",
    0: "lopeta"
}

CUBE_ACTIONS = {
    1: "1 lisää kortti",
    2: "2 poista kortti",
    3: "3 printtaa cube tekstinä",
    4: "4 printtaa cube kuvina",
    5: "5 tallenna cube",
    6: "6 suodata cube",
    0: "0 lopeta"
}


def initialUI():
    while True:
        for i in INITIAL_ACTIONS:
            print(f"'{i}' : {INITIAL_ACTIONS[i]}")
        action = input("Anna komento: ")
        if action == "0":
            print("Heippa!")
            break
        if action == "1":
            name = input("Nimeä Cube: ")
            new_cube = Cube(name)
            cube_ui(new_cube)
        if action == "2":
            name = input("Ladattava Cube: ")
            cube_ui(saver.load(name))
        if action == "3":
            txt_file_name = input("Tiedostonimi, josta lista haetaan: ")
            if os.path.exists("src/card_list_text_files/"+txt_file_name):
                name_for_cube = input("Nimi luotavalle Cubelle: ")
                cube_ui(saver.load_from_list(name_for_cube, txt_file_name))
            else:
                print("Tällä nimellä ei löytynyt listaa. Sisällytithän '.txt' syötteeseen?"+"\n")

# os.remove("src/entities/Saved_Cubes/Pallo.db")

# kuutio = cube_and_cards.Cube("Pallo")
# kuutio.add_card("Black Lotus")
# kuutio.add_card("vampiric tutor")
# kuutio.add_card("island")
# kuutio.add_card("plains")
# kuutio.add_card("forest")
# print(kuutio.collection)
# saver.save(kuutio)
# for i in kuutio.collection:
#     print(i)
# lataus = load("Pallo")
# print(lataus)
# print(type(lataus))
# print(lataus.collection)
# for i in lataus.collection:
#     print(i)

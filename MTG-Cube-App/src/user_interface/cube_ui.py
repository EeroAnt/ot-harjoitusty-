from entities.cube import Cube
from entities.card import Card, card_test
from printer.printer import print_list_imgs, print_list_table
import os
from data.saver_loader import save
from user_interface.filter_ui import filter_ui

CUBE_ACTIONS = {
    1: "1 lisää kortti",
    2: "2 lisää kortit tiedostosta",
    3: "3 poista kortti",
    4: "3 printtaa cube tekstinä",
    5: "4 printtaa cube kuvina",
    6: "6 suodata cube",
    7: "7 tallenna cube",
    0: "0 lopeta"
}


def cube_ui(cube: Cube):
    while True:
        for i in CUBE_ACTIONS:
            print(f"'{i}' : {CUBE_ACTIONS[i]}")
        action = int(input("Anna komento: "))
        if action == 0:
            print("Palataan")
            break
        if action == 1:
            name = input("Kortin nimi: ")
            if card_test(name) == True:
                cube.add_card(name)
            else:
                print("Kortin nimellä haku ei onnistunut")
        if action == 2:
            name = input("Tiedoston nimi: ")
            cube.add_cards_from_list(name)
        if action == 3:
            name = input("Kortin nimi: ")
            cube.remove_card(name)
        if action == 4:
            name = input("Nimeä tuloste: ")
            print_list_table(cube, name)
        if action == 5:
            name = input("Nimeä tuloste: ")
            print_list_imgs(cube, name)
        if action == 6:
            cube = filter_ui(cube)
        if action == 7:
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

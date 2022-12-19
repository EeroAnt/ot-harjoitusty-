from entities.cube import Cube
from entities.card import card_test
from printer.printer import print_list_imgs, print_list_table
from data.saver_loader import confirm_before_overwriting
from user_interface.filter_ui import filter_ui

CUBE_ACTIONS = {
    1: "1 lisää kortti",
    2: "2 lisää kortit tiedostosta",
    3: "3 poista kortti",
    4: "4 printtaa cube tekstinä",
    5: "5 printtaa cube kuvina",
    6: "6 suodata cube",
    7: "7 tallenna cube",
    0: "0 lopeta"
}


def cube_ui(cube: Cube):
    while True:
        print(cube.name)
        if len(cube.collection) == 1:
            print("Cubessa on 1 kortti")
        else:
            print(f"Cubessa on {len(cube.collection)} korttia")
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
            confirm_before_overwriting(cube)

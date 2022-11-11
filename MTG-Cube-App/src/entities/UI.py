import cube_and_cards
import string
import requests
import json

INITIAL_ACTIONS = {
    1: "luo uusi cube",
    2: "lataa vanha cube",
    9: "toista komennot",
    0: "lopeta"
}

CUBE_ACTIONS = {
    "1": "1 lisää kortti",
    "2": "2 printtaa cube",
    "9": "9 toita komennot",
    "0": "0 lopeta"

}

def initialUI():
    for i in INITIAL_ACTIONS:
        print(f"'{i}' : {INITIAL_ACTIONS[i]}")
    while True:
        action = int(input("Anna komento: "))
        if action == 0:
            print("Heippa!")
            break
        if action == 1:
            nimi = input("Nimeä Cube: ")
            uusi_cube = cube_and_cards.Cube(nimi)
            cubeUI(uusi_cube)
        if action == 9:
            for i in INITIAL_ACTIONS:
                print(f"'{i}' : {INITIAL_ACTIONS[i]}")


def cubeUI(cube: cube_and_cards.Cube):
    for i in CUBE_ACTIONS:
        print(f"'{i}' : {CUBE_ACTIONS[i]}")
    while True:
        action = int(input("Anna komento: "))
        if action == 0:
            print("Palataan")
            break
        if action == 1:
            name = input("Kortin nimi: ")
            if cube_and_cards.card_test(name):
                cube.add_card(name)
            else:
                print("Kortin nimellä haku ei onnistunut")
        if action == 2:
            for i in cube.collection:
                print(i)

initialUI()
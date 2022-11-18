import cube_and_cards as cube_and_cards
import Saver_loader as saver
import os

INITIAL_ACTIONS = {
    1: "luo uusi cube",
    2: "lataa vanha cube",
    9: "toista komennot",
    0: "lopeta"
}

CUBE_ACTIONS = {
    1: "1 lisää kortti",
    2: "2 printtaa cube",
    3: "3 tallenna cube",
    9: "9 toista komennot",
    0: "0 lopeta"

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
            if cube_and_cards.card_test(name) == True:
                cube.add_card(name)
            else:
                print("Kortin nimellä haku ei onnistunut")
        if action == 2:
            for i in cube.collection:
                print(i)
        if action == 3:
            if os.path.exists(f"src/entities/Saved_Cubes/{cube.name}.db"):
                confirmation = input("Tällä nimellä on jo cube olemassa. Haluatko varmasti tallentaa sen päälle? Y/n: ")
                if confirmation == "Y":
                    print("Tallennettu")
                    os.remove(f"src/entities/Saved_Cubes/{cube.name}.db")
                    saver.save(cube)
                    print("Tallennettu")
                else:
                    print("Ei tallennettu")
            else:
                saver.save(cube)
                print("Tallennettu")

# initialUI()
os.remove("src/entities/Saved_Cubes/Pallo.db")
kuutio = cube_and_cards.Cube("Pallo")
kuutio.add_card("Black Lotus")
kuutio.add_card("vampiric tutor")
kuutio.add_card("island")
print(kuutio.collection)
saver.save(kuutio)
for i in kuutio.collection:
    print(i)
# # lataus = load("Pallo")
# # print(lataus)
# print(type(lataus))
# print(lataus.collection)
# for i in lataus.collection:
#     print(i)

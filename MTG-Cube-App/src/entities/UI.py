import cube_and_cards as cube_and_cards
import saver_loader as saver
import os
import printer
import filter

INITIAL_ACTIONS = {
    1: "luo uusi cube",
    2: "lataa vanha cube",
    3: "luo cube tiedostosta",
    9: "toista komennot",
    0: "lopeta"
}

CUBE_ACTIONS = {
    1: "1 lisää kortti",
    2: "2 printtaa cube",
    3: "3 tallenna cube",
    4: "4 suodata cube",
    9: "9 toista komennot",
    0: "0 lopeta"

}


def initialUI():
    for i in INITIAL_ACTIONS:
        print(f"'{i}' : {INITIAL_ACTIONS[i]}")
    while True:
        action = 3#int(input("Anna komento: "))
        if action == 0:
            print("Heippa!")
            break
        if action == 1:
            name = input("Nimeä Cube: ")
            new_cube = cube_and_cards.Cube(name)
            cubeUI(new_cube)
        if action == 2:
            name = input("Ladattava Cube: ")
            cubeUI(saver.load(name))
        if action == 3:
            txt_file_name = "Testilista.txt"#input("Tiedostonimi, josta lista haetaan: ")
            if os.path.exists("src/entities/card_lists/"+txt_file_name):
                name_for_cube = input("Nimi luotavalle Cubelle: ")
                cubeUI(saver.load_from_list(name_for_cube, txt_file_name))
            else:
                print("Tällä nimellä ei löytynyt listaa. Sisällytithän '.txt' syötteeseen?")
                break
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
            printer.print_list(cube)
        if action == 3:
            if os.path.exists(f"src/entities/Saved_Cubes/{cube.name}.db"):
                confirmation = input(
                    "Tällä nimellä on jo cube olemassa. Haluatko varmasti tallentaa sen päälle? Y/n: ")
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
        if action == 4:
            filter.filter_cube(cube)

initialUI()
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

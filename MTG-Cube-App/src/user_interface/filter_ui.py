from entities.cube import Cube
from filter.filter import refresh_database, color_filter, color_id_filter
from filter.filter import cmc_filter, type_filter, oracle_filter, power_filter, toughness_filter
from printer.printer import print_list_imgs, print_list_table

def filter_ui(cube:Cube):
    not_filtered_cube = cube
    cube = refresh_database(cube)
    while True:
        instructions()
        commands = {
            1 : "'1': värillä",
            2 : "'2': väri-identiteetillä",
            3 : "'3': mana-arvolla",
            4 : "'4': tyypeillä",
            5 : "'5': tekstillä",
            6 : "'6': power-arvolla",
            7 : "'7': toughness-arvolla",
            9 : "'9': tulosta suodatettu lista",
            0 : "'0': palaa"
        }
        for i in commands.items():
            print(i[1])
        action = int(input("Anna komento: "))
        if action == 1:
            colors = input("Millä väreillä suodatetaan? (W,U,R,G,B): ")
            cube = color_filter(cube.name, colors)
        if action == 2:
            color_id = input("Suodata väri-identiteetillä (W,B,G,U,R): ")
            cube = color_id_filter(cube.name, color_id)
        if action == 3:
            cmc_query = int(input("Mana-arvosuodatuksen tyyppi ('1'"+
                ":enintään, '2': vähintään, '3':tasan): "))
            cmc_value = int(input("Anna arvo (kokonaisluku): "))
            cube = cmc_filter(cube.name,cmc_query,cmc_value)
        if action == 4:
            target_type = input("Suodata korttityypillä ja/tai -alatyypillä: ")
            cube = type_filter(cube.name,target_type)
        if action == 5:
            oracle = input("Suodata tekstillä: ")
            cube = oracle_filter(cube.name, oracle)
        if action == 6:
            power = []
            power.append(int(input("Power-arvon suodatustyyppi "+
                "('1':enintään, '2': vähintään, '3':tasan): ")))
            power.append(int(input("Suodata power-arvolla: ")))
            cube = power_filter(cube.name, power[0], power[1])
        if action == 7:
            toughness = []
            toughness.append(int(input("Toughness-arvosuodatuksen"+
                " tyyppi ('1':enintään, '2': vähintään, '3':tasan): ")))
            toughness.append(int(input("Anna arvo (kokonaisluku): ")))
            cube = toughness_filter(cube.name, toughness[0], toughness[1])
        if action == 9:
            table_or_imgs = input("Taulukko vai kuvat? (T/k)?")
            if table_or_imgs.lower() == "t":
                print_list_table(cube)
            if table_or_imgs.lower() == "k":
                print_list_imgs(cube)
        if action == 0:
            print("Palataan")
            return not_filtered_cube

def instructions():
    print("Ohjelma kysyy kaikki suodattimet läpi ja tulostaa suodatetun listan html-tiedostona")
    print("Jos et halua käyttää jotain suodatinta, jatka Enterillä")
    print("Väreillä suodattaminen vaatii, että kortista löytyy jokin syötetyistä väreistä")
    print("Väri-identiteetillä suodattaminen vaatii, ettei kortin väri-"+
        "identiteettiin sisälly mitään väriä syötettyjen värien lisäksi")
    print("Power- ja toughness-arvoilla suodattamallla hakuun jää vain olentoja")
    print("Suodatetaanko:")

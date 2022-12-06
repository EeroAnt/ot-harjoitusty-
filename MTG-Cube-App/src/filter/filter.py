import os
import sqlite3
from entities.cube import Cube
from printer.printer import print_list_table
from data.saver_loader import save

def filter_cube(cube:Cube):
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
            print(i)
        action = int(input("Anna komento: "))
        if action == 1:
            cube = color_filter(cube.name)
        if action == 2:
            cube = color_id_filter(cube.name)
        if action == 3:
            cube = cmc_filter(cube.name)
        if action == 4:
            cube = type_filter(cube.name)
        if action == 5:
            cube = oracle_filter(cube.name)
        if action == 6:
            power_filter()
        if action == 7:
            toughness_filter()
        if action == 9:
            print_list_table(cube)
        if action == 0:
            print("Palataan")
            return not_filtered_cube

def instructions():
    print("Ohjelma kysyy kaikki suodattimet läpi ja tulostaa suodatetun listan html-tiedostona")
    print("Jos et halua käyttää jotain suodatinta, jatka Enterillä")
    print("Väreillä suodattaminen vaatii, että kortista löytyy jokin syötetyistä väreistä")
    print("Väri-identiteetillä suodattaminen vaatii, ettei kortin väri-"+
        "identiteettiin sisälly mitään väriä syötettyjen värien lisäksi")
    #print("Power- ja toughness-arvoilla suodattamallla hakuun jää vain olentoja")
    print("Useamman tyypin etsimiseen, erottele hakusanat pilkulla\n")
    print("Suodatetaanko:\n")

def refresh_database(cube:Cube):
    os.remove("src/data/Saved_Cubes/temp.db")
    cube.name = "temp"
    save(cube)
    return cube

def color_filter(name):
    d_b = sqlite3.connect("src/data/Saved_Cubes/temp.db")
    d_b.isolation_level = None
    colors = input("Suodata väreillä (W,B,G,U,R): ")
    string_to_execute = "SELECT * From Cards WHERE colors LIKE ?"
    for i in range(len(colors)-1):
        string_to_execute += "or colors LIKE ?"
    string_to_execute += ";"
    list_of_variables = []
    for i in range(len(colors)):
        list_of_variables.append(f"%{colors[i]}%")
    filtered_list = d_b.execute(string_to_execute, list_of_variables).fetchall()
    new_cube = Cube(name)
    for i in filtered_list:
        new_cube.add_card(i[1])
    new_cube = refresh_database(new_cube)
    return new_cube

def color_id_filter(name):
    d_b = sqlite3.connect("src/data/Saved_Cubes/temp.db")
    d_b.isolation_level = None
    color_id = input("Suodata väri-identiteetillä (W,B,G,U,R): ")
    not_valid_colors = "WURGB"
    for i in color_id:
        if i in not_valid_colors:
            not_valid_colors.replace(i,'')
    string_to_execute = "SELECT * From Cards WHERE color_identity NOT LIKE ?"
    for i in range(len(not_valid_colors)-1):
        string_to_execute += "AND color_identity NOT LIKE ?"
    string_to_execute += ";"
    list_of_variables = []
    for i in range(len(not_valid_colors)):
        list_of_variables.append(f"%{not_valid_colors[i]}%")
    filtered_list = d_b.execute(string_to_execute, list_of_variables).fetchall()
    new_cube = Cube(name)
    for i in filtered_list:
        new_cube.add_card(i[1])
    return new_cube

def cmc_filter(name):
    cmc_query = input("Mana-arvosuodatuksen tyyppi ('1':enintään, '2': vähintään, '3':tasan): ")
    if cmc_query in ["1","2","3"]:
        cmc_value = input("Anna arvo (kokonaisluku): ")
    cmc_query = int(cmc_query)
    cmc_value = int(cmc_value)
    d_b = sqlite3.connect("src/data/Saved_Cubes/temp.db")
    d_b.isolation_level = None
    if cmc_query == 1:
        filtered_list = d_b.execute("SELECT * From Cards WHERE cmc <= ?;", [cmc_value]).fetchall()
    if cmc_query == 2:
        filtered_list = d_b.execute("SELECT * From Cards WHERE cmc >= ?;", [cmc_value]).fetchall()
    if cmc_query == 3:
        filtered_list = d_b.execute("SELECT * From Cards WHERE cmc = ?;", [cmc_value]).fetchall()
    new_cube = Cube(name)
    for i in filtered_list:
        new_cube.add_card(i[1])
    new_cube =refresh_database(new_cube)
    return new_cube

def type_filter(name):
    types = input("Suodata korttityypeillä ja/tai -alatyypeillä: ")
    if "," in types:
        list_of_types = types.split(",")
    else:
        list_of_types = [types]
    d_b = sqlite3.connect("src/data/Saved_Cubes/temp.db")
    d_b.isolation_level = None
    if len(list_of_types) == 1:
        filtered_list = d_b.execute("SELECT * From Cards WHERE type LIKE ?",
            [f"'%{list_of_types[0]}%'"])
    else:
        list_of_variables = []
        for i in range(len(list_of_types)):
            list_of_variables.append(f"%{list_of_types[i]}%")
        string_to_execute = "SELECT * From Cards WHERE type LIKE ?"
        for i in range(len(list_of_types)-1):
            string_to_execute += ",?"
        string_to_execute += ";"
        filtered_list = d_b.execute(string_to_execute,list_of_variables).fetchall()
    new_cube = Cube(name)
    for i in filtered_list:
        new_cube.add_card(i[1])
    new_cube = refresh_database(new_cube)
    return new_cube

def oracle_filter(name):
    oracle = input("Suodata tekstillä: ")
    d_b = sqlite3.connect("src/data/Saved_Cubes/temp.db")
    d_b.isolation_level = None
    filtered_list = d_b.execute("SELECT From Cards WHERE oracle LIKE ?",
        ["%"+oracle+"%"]).fetchall()
    new_cube = Cube(name)
    for i in filtered_list:
        new_cube.add_card(i[1])
    new_cube = refresh_database(new_cube)
    return new_cube

def power_filter():
    print("Tämä ominaisuus tulossa myöhemmin")
    # power_query = input("Power-arvon suodatustyyppi ('1':enintään, '2': vähintään, '3':tasan): ")
    # if power_query in ["1","2","3"]:
    #     power_value = input("Suodata power-arvolla: ")

def toughness_filter():
    print("Tämä ominaisuus tulossa myöhemmin")
    # toughness_query = input("Toughness-arvon suodatustyyppi"+
    #     " ('1':enintään, '2': vähintään, '3':tasan): ")
    # if toughness_query in ["1","2","3"]:
    #     toughness_value = input("Suodata toughness-arvolla: ")

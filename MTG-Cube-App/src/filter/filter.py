import os
import sqlite3
from entities.cube import Cube
from printer.printer import print_list_table, print_list_imgs
from data.saver_loader import save

def filter_cube(cube:Cube):
    not_filtered_cube = cube
    cube = refresh_database(cube)
    while True:
        #instructions()
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
            cube = power_filter(cube.name)
        if action == 7:
            cube = toughness_filter(cube.name)
        if action == 9:
            print("Taulukko vai kuvat? (T/k)?")
            table_or_imgs = get_input()
            if table_or_imgs.lower() == "t":
                print_list_table(cube)
            if table_or_imgs.lower() == "k":
                print_list_imgs(cube)
        if action == 0:
            print("Palataan")
            return not_filtered_cube

def get_input():
    return input()

def instructions():
    print("Ohjelma kysyy kaikki suodattimet läpi ja tulostaa suodatetun listan html-tiedostona")
    print("Jos et halua käyttää jotain suodatinta, jatka Enterillä")
    print("Väreillä suodattaminen vaatii, että kortista löytyy jokin syötetyistä väreistä")
    print("Väri-identiteetillä suodattaminen vaatii, ettei kortin väri-"+
        "identiteettiin sisälly mitään väriä syötettyjen värien lisäksi")
    print("Power- ja toughness-arvoilla suodattamallla hakuun jää vain olentoja")
    print("Suodatetaanko:")

def refresh_database(cube:Cube):
    os.remove("src/data/Saved_Cubes/temp.db")
    cube.name = "temp"
    save(cube)
    return cube

def color_filter(name):
    print("Älä syötä muita merkkejä, kuin värejä kuvaavia kirjaimia")
    d_b = sqlite3.connect("src/data/Saved_Cubes/temp.db")
    d_b.isolation_level = None
    print("Suodata väreillä (W,B,G,U,R): ")
    colors = get_input()
    string_to_execute = "SELECT * From Cards WHERE colors LIKE ?"
    for i in range(len(colors)-1):
        string_to_execute += "or colors LIKE ?"
    string_to_execute += ";"
    list_of_variables = []
    for ele in enumerate(colors):
        list_of_variables.append(f'%{ele[1]}%')
    print(list_of_variables)
    filtered_list = d_b.execute(string_to_execute, list_of_variables).fetchall()
    color_filtered_cube = Cube(name)
    for i in filtered_list:
        color_filtered_cube.add_card(i[1])
    color_filtered_cube = refresh_database(color_filtered_cube)
    return color_filtered_cube

def color_id_filter(name):
    d_b = sqlite3.connect("src/data/Saved_Cubes/temp.db")
    d_b.isolation_level = None
    print("Suodata väri-identiteetillä (W,B,G,U,R): ")
    color_id = get_input()
    not_valid_colors = "WURGB"
    for i in color_id:
        if i in not_valid_colors:
            not_valid_colors = not_valid_colors.replace(i,'')
    print(not_valid_colors)
    string_to_execute = "SELECT * From Cards WHERE color_identity NOT LIKE ?"
    for i in range(len(not_valid_colors)-1):
        string_to_execute += " AND color_identity NOT LIKE ?"
    string_to_execute += ";"
    list_of_variables = []
    for ele in enumerate(not_valid_colors):
        list_of_variables.append(f'%{ele[1]}%')
    filtered_list = d_b.execute(string_to_execute, list_of_variables).fetchall()
    color_id_filtered_cube = Cube(name)
    for i in filtered_list:
        color_id_filtered_cube.add_card(i[1])
    color_id_filtered_cube = refresh_database(color_id_filtered_cube)
    return color_id_filtered_cube

def cmc_filter(name):
    print("Mana-arvosuodatuksen tyyppi ('1':enintään, '2': vähintään, '3':tasan): ")
    cmc_query = get_input()
    if cmc_query in ["1","2","3"]:
        print("Anna arvo (kokonaisluku): ")
        cmc_value = get_input()
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
    cmc_filtered_cube = Cube(name)
    for i in filtered_list:
        cmc_filtered_cube.add_card(i[1])
    cmc_filtered_cube =refresh_database(cmc_filtered_cube)
    return cmc_filtered_cube

def type_filter(name):
    print("Suodata korttityypillä ja/tai -alatyypillä: ")
    target_type = get_input()
    d_b = sqlite3.connect("src/data/Saved_Cubes/temp.db")
    d_b.isolation_level = None
    filtered_list = d_b.execute("SELECT * From Cards WHERE type LIKE ?",
        [f'%{target_type}%'])
    type_filtered_cube = Cube(name)
    for i in filtered_list:
        type_filtered_cube.add_card(i[1])
    type_filtered_cube = refresh_database(type_filtered_cube)
    return type_filtered_cube

def oracle_filter(name):
    oracle = input("Suodata tekstillä: ")
    d_b = sqlite3.connect("src/data/Saved_Cubes/temp.db")
    d_b.isolation_level = None
    filtered_list = d_b.execute("SELECT * From Cards WHERE oracle LIKE ?",
        ["%"+oracle+"%"]).fetchall()
    text_filtered_cube = Cube(name)
    for i in filtered_list:
        text_filtered_cube.add_card(i[1])
    text_filtered_cube = refresh_database(text_filtered_cube)
    return text_filtered_cube

def power_filter(name):
    print("Power-arvon suodatustyyppi ('1':enintään, '2': vähintään, '3':tasan): ")
    power_query = get_input()
    if power_query in ["1","2","3"]:
        print("Suodata power-arvolla: ")
        power_value = int(get_input())
    d_b = sqlite3.connect("src/data/Saved_Cubes/temp.db")
    d_b.isolation_level = None
    power_query = int(power_query)
    if power_query == 1:
        filtered_list = d_b.execute("SELECT * From (SELECT * From Cards "+
        "WHERE type LIKE '%creature%') WHERE power <= ?;", [power_value]).fetchall()
    if power_query == 2:
        filtered_list = d_b.execute("SELECT * From (SELECT * From Cards "+
        "WHERE type LIKE '%creature%') WHERE power >= ?;", [power_value]).fetchall()
    if power_query == 3:
        filtered_list = d_b.execute("SELECT * From (SELECT * From Cards "+
        "WHERE type LIKE '%creature%') WHERE power = ?;", [power_value]).fetchall()
    power_filtered_cube = Cube(name)
    for i in filtered_list:
        power_filtered_cube.add_card(i[1])
    power_filtered_cube =refresh_database(power_filtered_cube)
    return power_filtered_cube

def toughness_filter(name):
    print("Toughness-arvosuodatuksen tyyppi ('1':enintään, '2': vähintään, '3':tasan): ")
    toughness_query = get_input()
    if toughness_query in ["1","2","3"]:
        print("Anna arvo (kokonaisluku): ")
        toughness_value = get_input()
    toughness_query = int(toughness_query)
    toughness_value = int(toughness_value)
    d_b = sqlite3.connect("src/data/Saved_Cubes/temp.db")
    d_b.isolation_level = None
    if toughness_query == 1:
        filtered_list = d_b.execute("SELECT * From (SELECT * From Cards "+
        "WHERE type LIKE '%creature%') WHERE toughness <= ?;", [toughness_value]).fetchall()
    if toughness_query == 2:
        filtered_list = d_b.execute("SELECT * From (SELECT * From Cards "+
        "WHERE type LIKE '%creature%') WHERE toughness >= ?;", [toughness_value]).fetchall()
    if toughness_query == 3:
        filtered_list = d_b.execute("SELECT * From (SELECT * From Cards "+
        "WHERE type LIKE '%creature%') WHERE toughness = ?;", [toughness_value]).fetchall()
    new_cube = Cube(name)
    for i in filtered_list:
        new_cube.add_card(i[1])
    new_cube =refresh_database(new_cube)
    return new_cube

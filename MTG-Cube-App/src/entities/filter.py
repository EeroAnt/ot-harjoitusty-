import os
import sqlite3
import cube_and_cards
import printer
import saver_loader

def filter_cube(cube:cube_and_cards.Cube):
    refresh_database(cube)
    name_of_list = cube.name
    instructions()
    list_of_filters = []
    symbol_dict = {
        "1": "<=",
        "2": ">=",
        "3": "="
    }
    colors = input("Suodata väreillä (W,B,G,U,R): ")
    color_id = input("Suodata väri-identiteetillä (W,B,G,U,R): ")
    cmc_query = input("Mana-arvosuodatuksen tyyppi ('1':enintään, '2': vähintään, '3':tasan): ")
    if cmc_query in ["1","2","3"]:
        cmc_value = input("Anna arvo (kokonaisluku): ")
        list_of_filters.append(f",manavalue{symbol_dict[cmc_query]}{cmc_value}")
    types = input("Suodata korttityypeillä tai -alatyypeillä: ")
    oracle = input("Suodata tekstillä: ")
    power_query = input("Power-arvon suodatustyyppi ('1':enintään, '2': vähintään, '3':tasan): ")
    if power_query in ["1","2","3"]:
        power_value = input("Suodata power-arvolla: ")
        list_of_filters.append(f",power{symbol_dict[power_query]}{power_value}")
    toughness_query = input("Toughness-arvon suodatustyyppi"+
        " ('1':enintään, '2': vähintään, '3':tasan): ")
    if toughness_query in ["1","2","3"]:
        toughness_value = input("Suodata toughness-arvolla: ")
        list_of_filters.append(f",toughness{symbol_dict[toughness_query]}{toughness_value}")
    if colors != "":
        list_of_filters.append(",colors:"+colors)
        cube = color_filter(colors, name_of_list)
        refresh_database(cube)
    if color_id != "":
        list_of_filters.append(",color_id:"+color_id)
        cube = color_id_filter(color_id, name_of_list)
        refresh_database(cube)
    if cmc_query != "":
        cube = cmc_filter(cmc_query, cmc_value, name_of_list)
        refresh_database(cube)
    if types != "":
        list_of_filters.append(",types:"+types)
        cube = type_filter(types, name_of_list)
        refresh_database(cube)
    if oracle != "":
        list_of_filters.append(oracle)
        cube = oracle_filter(oracle, name_of_list)
        refresh_database(cube)
    for i in list_of_filters:
        if i != "":
            name_of_list += i
    filtered_cube = cube_and_cards.Cube(name_of_list)
    for i in cube.card_names:
        filtered_cube.add_card(i)
    printer.print_list(filtered_cube)

def instructions():
    print("Ohjelma kysyy kaikki suodattimet läpi ja tulostaa suodatetun listan html-tiedostona")
    print("Jos et halua käyttää jotain suodatinta, jatka Enterillä")
    print("Väreillä suodattaminen vaatii, että kortista löytyy jokin syötetyistä väreistä")
    print("Väri-identiteetillä suodattaminen vaatii, ettei kortin väri-"+
        "identiteettiin sisälly mitään väriä syötettyjen värien lisäksi")
    print("Power- ja toughness-arvoilla suodattamallla hakuun jää vain olentoja")
    print("Useamman tyypin etsimiseen, erottele hakusanat pilkulla")

def refresh_database(cube:cube_and_cards.Cube):
    os.remove("src/entities/Saved_Cubes/temp.db")
    cube.name = "temp"
    saver_loader.save(cube)

def color_filter(colors:str, name):
    d_b = sqlite3.connect("src/entities/Saved_Cubes/temp.db")
    d_b.isolation_level = None
    string_to_execute = "SELECT * From Cards WHERE colors LIKE ?"
    for i in range(len(colors)-1):
        string_to_execute += "or colors LIKE ?"
    string_to_execute += ";"
    list_of_variables = []
    for i in range(len(colors)):
        list_of_variables.append(f"%{colors[i]}%")
    filtered_list = d_b.execute(string_to_execute, list_of_variables).fetchall()
    new_cube = cube_and_cards.Cube(name)
    for i in filtered_list:
        new_cube.add_card(i[1])
    return new_cube

def color_id_filter(color_id:str, name):
    d_b = sqlite3.connect("src/entities/Saved_Cubes/temp.db")
    d_b.isolation_level = None
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
    new_cube = cube_and_cards.Cube(name)
    for i in filtered_list:
        new_cube.add_card(i[1])
    return new_cube

def cmc_filter(cmc_query: str, cmc_value: str, name):
    cmc_query = int(cmc_query)
    cmc_value = int(cmc_value)
    d_b = sqlite3.connect("src/entities/Saved_Cubes/temp.db")
    d_b.isolation_level = None
    if cmc_query == 1:
        filtered_list = d_b.execute("SELECT * From Cards WHERE cmc <= ?;", [cmc_value]).fetchall()
    if cmc_query == 2:
        filtered_list = d_b.execute("SELECT * From Cards WHERE cmc >= ?;", [cmc_value]).fetchall()
    if cmc_query == 3:
        filtered_list = d_b.execute("SELECT * From Cards WHERE cmc = ?;", [cmc_value]).fetchall()
    new_cube = cube_and_cards.Cube(name)
    for i in filtered_list:
        new_cube.add_card(i[1])
    return new_cube

def type_filter(types:str,name):
    if "," in types:
        list_of_types = types.split(",")
    else:
        list_of_types = [types]
    d_b = sqlite3.connect("src/entities/Saved_Cubes/temp.db")
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
    new_cube = cube_and_cards.Cube(name)
    for i in filtered_list:
        new_cube.add_card(i[1])
    return new_cube

def oracle_filter(oracle:str,name):
    d_b = sqlite3.connect("src/entities/Saved_Cubes/temp.db")
    d_b.isolation_level = None
    filtered_list = d_b.execute("SELECT From Cards WHERE oracle LIKE ?",
        ["%"+oracle+"%"]).fetchall()
    new_cube = cube_and_cards.Cube(name)
    for i in filtered_list:
        new_cube.add_card(i[1])
    return new_cube

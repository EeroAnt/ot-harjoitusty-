import os
import sqlite3
from entities.cube import Cube
from data.saver_loader import save

# Suodattelun tuloksia ylläpidetään temp.db-tiedostossa
def refresh_database(cube:Cube):
    # Ensiksi vanha poistetaan
    os.remove("src/data/Saved_Cubes/temp.db")
    # Ja sitten uusi tallennetaan
    cube.name = "temp"
    save(cube)
    return cube

# Värin perusteella filtteröinti. Kortin väreistä tulee löytyä
# jokin haetuista väreistä 
def color_filter(name, colors):
    # Yhdistetään väliaikaiseen tietokantaan
    # (en toista kaikkia kommentteja joka suodattimessa)
    d_b = sqlite3.connect("src/data/Saved_Cubes/temp.db")
    d_b.isolation_level = None
    # Rakennetaan sql-kysely
    string_to_execute = "SELECT * From Cards WHERE colors LIKE ?"
    # Jokainen väri ensimmäisen jälkeen luo oman ehdon
    for i in range(len(colors)-1):
        string_to_execute += "or colors LIKE ?"
    string_to_execute += ";" # Varmaan toimis ilmankin, mutta lisään silti
    # Kirjataan värit sql-kyselylle sopivaan muotoon (lista)
    list_of_variables = []
    for ele in enumerate(colors):
        list_of_variables.append(f'%{ele[1]}%')
    # Yhdistetään palikat ja tehdään kysely
    filtered_list = d_b.execute(string_to_execute, list_of_variables).fetchall()
    # Luodaan uusi cube suodatetulla sisällöllä
    color_filtered_cube = Cube(name)
    for i in filtered_list:
        color_filtered_cube.add_card(i[1])
    # Ja päivitetään se uudeksi väliaikaiseksi tietokannaksi
    color_filtered_cube = refresh_database(color_filtered_cube)
    return color_filtered_cube

# Väri-identiteetti suodataa pois ne kortit, joiden väri-identiettiin
# sisältyy jokin väri, joka ei ollut haussa mukana. Eli värittömät
# kortit kelpaavat aina (toisin kuin väri-suodatukseen), mutta käypän
# värin löytyminen ei takaa, että kortti jäisi listalle (korteilla voi
# olla useampi väri)
def color_id_filter(name, color_id):
    d_b = sqlite3.connect("src/data/Saved_Cubes/temp.db")
    d_b.isolation_level = None
    # Ensiksi sisällän kaikki värit kelvottomiin
    not_valid_colors = "WURGB"
    # sitten poistan kelvottomista kelvot
    for i in color_id:
        if i in not_valid_colors:
            not_valid_colors = not_valid_colors.replace(i,'')
    string_to_execute = "SELECT * From Cards WHERE color_identity NOT LIKE ?"
    # Tällä kertaa suodatetaan pois rivit, joiden väri-identiteettiin
    # sisältyy kelvottomia värejä
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

# tämä suodattaa kortit, niiden mana-arvon (ennen cmc eli converted mana cost)
# perusteella.
def cmc_filter(name, cmc_query, cmc_value):
    d_b = sqlite3.connect("src/data/Saved_Cubes/temp.db")
    d_b.isolation_level = None
    # haetaan kortit, joiden mana-arvo vähintään cmc_value
    if cmc_query == 1:
        filtered_list = d_b.execute("SELECT * From Cards WHERE cmc <= ?;", [cmc_value]).fetchall()
    # haetaan kortit, joiden mana-arvo enintään cmc_value
    if cmc_query == 2:
        filtered_list = d_b.execute("SELECT * From Cards WHERE cmc >= ?;", [cmc_value]).fetchall()
    # haetaan kortit, joiden mana-arvo tasan cmc_value
    if cmc_query == 3:
        filtered_list = d_b.execute("SELECT * From Cards WHERE cmc = ?;", [cmc_value]).fetchall()
    cmc_filtered_cube = Cube(name)
    for i in filtered_list:
        cmc_filtered_cube.add_card(i[1])
    cmc_filtered_cube =refresh_database(cmc_filtered_cube)
    return cmc_filtered_cube

# Haetaan kortit, joilla on pyydetty tyyppi
def type_filter(name,target_type):
    d_b = sqlite3.connect("src/data/Saved_Cubes/temp.db")
    d_b.isolation_level = None
    filtered_list = d_b.execute("SELECT * From Cards WHERE type LIKE ?",
        [f'%{target_type}%'])
    type_filtered_cube = Cube(name)
    for i in filtered_list:
        type_filtered_cube.add_card(i[1])
    type_filtered_cube = refresh_database(type_filtered_cube)
    return type_filtered_cube

# Suodatetaan tekstillä teksti-laatikosta
def oracle_filter(name, oracle):
    d_b = sqlite3.connect("src/data/Saved_Cubes/temp.db")
    d_b.isolation_level = None
    filtered_list = d_b.execute("SELECT * From Cards WHERE oracle LIKE ?",
        ["%"+oracle+"%"]).fetchall()
    text_filtered_cube = Cube(name)
    for i in filtered_list:
        text_filtered_cube.add_card(i[1])
    text_filtered_cube = refresh_database(text_filtered_cube)
    return text_filtered_cube

# Mana-arvoa vastaava suodatus power-arvolle
def power_filter(name, power_query, power_value):
    d_b = sqlite3.connect("src/data/Saved_Cubes/temp.db")
    d_b.isolation_level = None
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

# Mana-arvoa vastaava suodatus toughness-arvolle
def toughness_filter(name, toughness_query, toughness_value):
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

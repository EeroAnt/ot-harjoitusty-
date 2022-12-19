import os
import sqlite3


def build():
    if os.path.exists("src/data/fetched_cards/fetched_cards.db"):
        os.remove("src/data/fetched_cards/fetched_cards.db")
    d_b = sqlite3.connect("src/data/fetched_cards/fetched_cards.db")
    d_b.isolation_level = None
    d_b.execute(
        "CREATE TABLE Cards (id INTEGER PRIMARY KEY, name TEXT, "+
        "colors TEXT, color_identity TEXT, cmc INTEGER, mana_cost "+
        "TEXT, type TEXT, keywords TEXT, oracle TEXT, image_uri TEXT,"+
        " layout TEXT, power TEXT, toughness TEXT );")
    if os.path.exists("src/data/Saved_Cubes/temp.db"):
        os.remove("src/data/Saved_Cubes/temp.db")
    d_b = sqlite3.connect("src/data/Saved_Cubes/temp.db")
    d_b.isolation_level = None
    d_b.execute(
        "CREATE TABLE Cards (id INTEGER PRIMARY KEY, name TEXT, "+
        "colors TEXT, color_identity TEXT, cmc INTEGER, mana_cost "+
        "TEXT, type TEXT, keywords TEXT, oracle TEXT, image_uri TEXT,"+
        " layout TEXT, power TEXT, toughness TEXT );")
    if os.path.exists("src/data/Saved_Cubes/TestCube.db"):
        os.remove("src/data/Saved_Cubes/TestCube.db")
    d_b = sqlite3.connect("src/data/Saved_Cubes/TestCube.db")
    d_b.isolation_level = None
    d_b.execute(
        "CREATE TABLE Cards (id INTEGER PRIMARY KEY, name TEXT, "+
        "colors TEXT, color_identity TEXT, cmc INTEGER, mana_cost "+
        "TEXT, type TEXT, keywords TEXT, oracle TEXT, image_uri TEXT,"+
        " layout TEXT, power TEXT, toughness TEXT );")

build()

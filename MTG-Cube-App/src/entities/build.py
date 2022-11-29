import os
import sqlite3


def build():
    if os.path.exists("src/entities/fetched_cards/fetched_cards.db"):
        pass
    else:
        d_b = sqlite3.connect("src/entities/fetched_cards/fetched_cards.db")
        d_b.isolation_level = None
        d_b.execute(
            "CREATE TABLE Cards (id INTEGER PRIMARY KEY, name TEXT, "+
            "colors TEXT, color_identity TEXT, cmc INTEGER, mana_cost "+
            "TEXT, type TEXT, keywords TEXT, oracle TEXT, image_uri TEXT, p_t TEXT );")
    if os.path.exists("src/entities/fetched_cards/temp.db"):
        pass
    else:
        d_b = sqlite3.connect("src/entities/fetched_cards/temp.db")
        d_b.isolation_level = None
        d_b.execute(
            "CREATE TABLE Cards (id INTEGER PRIMARY KEY, name TEXT, "+
            "colors TEXT, color_identity TEXT, cmc INTEGER, mana_cost "+
            "TEXT, type TEXT, keywords TEXT, oracle TEXT, image_uri TEXT, p_t TEXT );")
    if os.path.exists("src/entities/fetched_cards/TestCube.db"):
        pass
    else:
        d_b = sqlite3.connect("src/entities/fetched_cards/TestCube.db")
        d_b.isolation_level = None
        d_b.execute(
            "CREATE TABLE Cards (id INTEGER PRIMARY KEY, name TEXT, "+
            "colors TEXT, color_identity TEXT, cmc INTEGER, mana_cost "+
            "TEXT, type TEXT, keywords TEXT, oracle TEXT, image_uri TEXT, p_t TEXT );")

build()

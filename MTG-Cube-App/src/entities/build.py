import os
import sqlite3

def build():
    if os.path.exists(f"src/entities/fetched_cards/fetched_cards.db"):
        pass
    else:
        db = sqlite3.connect(f"src/entities/fetched_cards/fetched_cards.db")
        db.isolation_level = None
        db.execute("CREATE TABLE Cards (id INTEGER PRIMARY KEY, name TEXT, colors TEXT, color_identity TEXT, cmc INTEGER, mana_cost TEXT, type TEXT, keywords TEXT, oracle TEXT, image_uri TEXT, p_t TEXT );")

build()
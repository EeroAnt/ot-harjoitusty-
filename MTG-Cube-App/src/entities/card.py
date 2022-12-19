import sqlite3
import time
import json
import requests

class Card:
    # Tämä vastaa yksittäistä korttia.
    def __init__(self, name: str):
        self.name = name
        card_dict = CardData(name).card_dict
        self.colors = card_dict["colors"]
        self.color_id = card_dict["color_identity"]
        self.cmc = int(card_dict["cmc"])
        self.mana_cost = card_dict["mana_cost"]
        self.type = card_dict["type_line"]
        self.keywords = card_dict["keywords"]
        self.text = card_dict["oracle_text"]
        self.img_uri = card_dict["image_uris"]["png"]
        self.layout = card_dict["layout"]
        self.power = ""
        self.toughness = ""
        for i in card_dict:
            if i == "power":
                self.power = card_dict["power"]
                self.toughness = card_dict["toughness"]
        name_for_img = name.replace(" ", "+").replace("/", "").replace(",", "")
        self.name_for_img = name_for_img.lower()

class CardData:
    # Tähän haetaan raakaversio, josta korttiluokka osaa sitten hakea
    # tarvitsemansa tiedot. Ensisijaisesti tarkastatetaan aiemmin
    # haettujen korttien tietokanta fetched_cards.db, ja jos sieltä
    # ei löydy, tehdään api-kutsu.
    def __init__(self, name):
        self.card_dict = {}
        d_b = sqlite3.connect("src/data/fetched_cards/fetched_cards.db")
        d_b.isolation_level = None
        card_data = d_b.execute("SELECT * FROM Cards WHERE name LIKE ?", [name]).fetchone()
        if card_data is not None:
            self.card_dict = data_from_db(name)
        else:
            self.card_dict = data_from_api(name)

# Tällä testataan, onko kortti validi (löytyykö aiemmista korteista
# tai scryfall tietokannasta)
def card_test(name: str):
    d_b = sqlite3.connect("src/data/fetched_cards/fetched_cards.db")
    d_b.isolation_level = None
    card_data = d_b.execute(
        "SELECT * FROM Cards WHERE name LIKE ?", [name]).fetchone()
    if card_data is not None:
        return True
    if data_from_api(name) is not False:
        return True
    return False

# Tämä kääntää json-objektin luettavaan muotoon merkkijonoksi
def jprint(obj):
    data = json.dumps(obj, sort_keys=True, indent=4)
    return data

# Tämä hakee yksittäisen kortin tiedot lokaalista tietokannasta
def data_from_db(name):
    d_b = sqlite3.connect("src/data/fetched_cards/fetched_cards.db")
    d_b.isolation_level = None
    card_data = d_b.execute("SELECT * FROM Cards WHERE name LIKE ?", [name]).fetchone()
    card_dict = {
        "name": card_data[1],
        "colors": card_data[2],
        "color_identity": card_data[3],
        "cmc": card_data[4],
        "mana_cost": card_data[5],
        "type_line": card_data[6],
        "keywords": card_data[7],
        "oracle_text": card_data[8],
        "image_uris": {"png": card_data[9]},
        "layout": card_data[10]}
    if card_data[11] is not None:
        card_dict["power"] = card_data[11]
        card_dict["toughness"] = card_data[12]
    return card_dict

# Tämä hakee kortin tiedot internetistä
def data_from_api(name:str):
    name_for_api = name.replace(" ", "+")
    name_for_api = name_for_api.replace("/", "")
    name_for_api = name_for_api.replace(",", "")
    card_data_api = requests.get(
        "https://api.scryfall.com/cards/named?exact="+
        name_for_api, timeout=10)
    time.sleep(0.1)
    card_dict = json.loads(jprint(card_data_api.json()))
    if "name" not in card_dict.keys():
        return False
    card_dict = parse_card_data(card_dict)
    return data_from_db(name)

# Luodaan uusi rivi fetched_cards-tietokantaan api-kutsun perusteella.
# Kortteja on erilaisia, joten välillä pitää valikoida eri asioita
def api_data_to_db(card_dict):
    d_b = sqlite3.connect("src/data/fetched_cards/fetched_cards.db")
    d_b.isolation_level = None
    card_data = d_b.execute(
        "SELECT * FROM Cards WHERE name LIKE ?", [card_dict["name"]]).fetchone()
    if card_data is None:
        if "power" in card_dict.keys():
            d_b.execute("INSERT INTO Cards (name, colors, color_identity, "+
                "cmc, mana_cost, type, keywords, oracle, image_uri, layout,"+
                " power, toughness) VALUES (?,?,?,?,?,?,?,?,?,?,?,?);", [
                    card_dict["name"],
                    str(card_dict["colors"]),
                    str(card_dict["color_identity"]),
                    card_dict["cmc"],
                    str(card_dict["mana_cost"]),
                    card_dict["type_line"],
                    str(card_dict["keywords"]),
                    card_dict["oracle_text"],
                    card_dict["image_uris"]["png"],
                    card_dict["layout"],
                    card_dict["power"],
                    card_dict["toughness"]
                ])
        else:
            d_b.execute(
                "INSERT INTO Cards ("+
                "name, colors, color_identity, cmc, mana_cost, "+
                "type, keywords, oracle, image_uri, layout) "+
                "VALUES (?,?,?,?,?,?,?,?,?,?);", [
                    card_dict["name"],
                    str(card_dict["colors"]),
                    str(card_dict["color_identity"]),
                    card_dict["cmc"],
                    str(card_dict["mana_cost"]),
                    card_dict["type_line"],
                    str(card_dict["keywords"]),
                    card_dict["oracle_text"],
                    card_dict["image_uris"]["png"],
                    card_dict["layout"]
                ])

# Kortin muotoilun/leikkauksen tunnistaminen
def parse_card_data(card_dict:dict):
    if "oracle_text" not in card_dict.keys():
        card_dict.update({"oracle_text": ''})
    if card_dict["layout"] == "normal":
        api_data_to_db(card_dict)
        get_image(card_dict)
        return card_dict
    if card_dict["layout"] == "transform" or card_dict["layout"] == "modal_dfc":
        two_faced_card(card_dict)
    if card_dict["layout"] == "split":
        split_card(card_dict)
        return card_dict

def two_faced_card(card_dict):
    card_dict_front = {
        "name": card_dict["card_faces"][0]["name"],
        "colors": card_dict["card_faces"][0]["colors"],
        "color_identity": card_dict["color_identity"],
        "cmc": card_dict["cmc"],
        "mana_cost": card_dict["card_faces"][0]["mana_cost"],
        "type_line":card_dict["card_faces"][0]["type_line"],
        "keywords": card_dict["keywords"],
        "oracle_text": card_dict["card_faces"][0]["oracle_text"],
        "image_uris": {"png": card_dict["card_faces"][0]["image_uris"]["png"]},
        "layout": card_dict["layout"],
        "power": "",
        "toughness": ""
    }
    if "power" in card_dict["card_faces"][0].keys():
        card_dict_front.update({
            "power":card_dict["card_faces"][0]["power"],
            "toughness":card_dict["card_faces"][0]["toughness"]
            })
    card_dict_back = {
        "name": card_dict["card_faces"][1]["name"],
        "colors": card_dict["card_faces"][1]["colors"],
        "color_identity": card_dict["color_identity"],
        "cmc": card_dict["cmc"],
        "mana_cost": card_dict["card_faces"][1]["mana_cost"],
        "type_line":card_dict["card_faces"][1]["type_line"],
        "keywords": card_dict["keywords"],
        "oracle_text": card_dict["card_faces"][1]["oracle_text"],
        "image_uris": {"png": card_dict["card_faces"][1]["image_uris"]["png"]},
        "layout": "backside",
        "power": "",
        "toughness": ""
    }
    if "power" in card_dict["card_faces"][1].keys():
        card_dict_back.update({
            "power":card_dict["card_faces"][1]["power"],
            "toughness":card_dict["card_faces"][1]["toughness"]
            })
    api_data_to_db(card_dict_front)
    api_data_to_db(card_dict_back)
    get_image(card_dict_front)
    get_image(card_dict_back)
    return card_dict

def split_card(card_dict):
    for i in card_dict["card_faces"]:
        card_dict["oracle_text"] += i["oracle_text"] + "//"
    api_data_to_db(card_dict)
    get_image(card_dict)
    return card_dict

def get_image(card_dict):
    name_for_api = card_dict["name"].replace(" ", "+")
    name_for_api = name_for_api.replace("/", "")
    name_for_api = name_for_api.replace(",", "")
    image = requests.get(
    card_dict["image_uris"]["png"],allow_redirects=True, timeout=10)
    with open("src/data/fetched_cards/"+name_for_api.lower()+".png", 'wb') as pic:
        pic.write(image.content)

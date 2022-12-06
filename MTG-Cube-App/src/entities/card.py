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
        self.p_t = ""
        for i in card_dict:
            if i == "p/t":
                self.p_t = card_dict["p/t"]
        name_for_img = name.replace(" ", "+").replace("/", "").replace(",", "")
        self.name_for_img = name_for_img.lower()

    # def __str__(self):
    #     return self.name


class CardData:
    # Tähän haetaan raaka, josta korttiluokka osaa sitten hakea tarvitsemansa tiedot.
    # Ensisijaisesti tarkastatetaan aiemmin haettujen korttien tietokanta
    # fetched_cards.db, ja jos sieltä ei löydy, tehdään api-kutsu.
    def __init__(self, name):
        self.card_dict = {}
        d_b = sqlite3.connect("src/data/fetched_cards/fetched_cards.db")
        d_b.isolation_level = None
        card_data = d_b.execute("SELECT * FROM Cards WHERE name LIKE ?", [name]).fetchone()
        if card_data is not None:
            if data_from_db is not False:
                self.card_dict = data_from_db(name)
        else:
            self.card_dict = data_from_api(name)

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


def jprint(obj):
    # Converts json object to string
    data = json.dumps(obj, sort_keys=True, indent=4)
    return data

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
        "image_uris": {"png": card_data[9]}}
    if card_data[10] is not None:
        card_dict["p/t"] = card_data[10]
    return card_dict

def data_from_api(name:str):
    #pilkotaan kortin nimi api-kutsulle kelpaavaksi
    name_for_api = name.replace(" ", "+")
    name_for_api = name_for_api.replace("/", "")
    name_for_api = name_for_api.replace(",", "")
    card_data_api = requests.get(
        "https://api.scryfall.com/cards/named?exact="+
        name_for_api, timeout=10)
    #scryfall-apin dokumentaatiossa oli pyyntö, ettei useammin tehtäisi kutsuja
    time.sleep(0.1)
    if card_data_api.status_code == 200:
        card_dict = json.loads(jprint(card_data_api.json()))
        # Erilaisilla korteilla on erilainen rakenne jsonissa.
        # Käsitteekseni kaikki, muut paitsi kaksipuoleiset
        # kortit menevät jo olemassaolevalla rakenteella läpi.
        if "name" not in card_dict.keys():
            two_faced_card_handler()
        else:
            api_data_to_db(card_dict)
            image = requests.get(
            card_dict["image_uris"]["png"],allow_redirects=True, timeout=10)
            with open("src/data/fetched_cards/"+name_for_api.lower()+".png", 'wb') as pic:
                pic.write(image.content)
            # Tää oli hämmentävä. api-kutsulla tehdyn kortin attribuuttien muotoilu oli
            # erilainen, vaikka api-kutsun perusteella rakennetaan db-rivi kyseiselle
            # kortille. Päätin sitten antaa api-kutsun vain luoda kyseisen rivin ja
            # rakentaa sen perusteella kortti-olion, jotta pysyisivät yhdenmuotoisina.
            return data_from_db(name)
    return False

def api_data_to_db(card_dict):
    # tuplakorteilla (eri kuin kaksipuoleiset) on oracle-teksti
    # eri tavoin kuin yksinkertaisilla korteilla.
    # Katso esimerkiksi Carnival // Carnage testilistasta.
    oracle = ""
    if "oracle_text" in card_dict.keys():
        oracle = card_dict["oracle_text"]
    else:
        for i in card_dict["card_faces"]:
            oracle += i["oracle_text"] + "//"
    d_b = sqlite3.connect("src/data/fetched_cards/fetched_cards.db")
    d_b.isolation_level = None
    if "power" in card_dict.keys():
        card_dict["p/t"] = str(card_dict["power"]) + \
            "/"+str(card_dict["toughness"])
        d_b.execute("INSERT INTO Cards (name, colors, color_identity, "+
            "cmc, mana_cost, type, keywords, oracle, image_uri, p_t)"+
            " VALUES (?,?,?,?,?,?,?,?,?,?);", [
                card_dict["name"],
                str(card_dict["colors"]),
                str(card_dict["color_identity"]),
                card_dict["cmc"],
                str(card_dict["mana_cost"]),
                card_dict["type_line"],
                str(card_dict["keywords"]),
                oracle,
                card_dict["image_uris"]["png"],
                card_dict["p/t"]
            ])
    else:
        d_b.execute(
            "INSERT INTO Cards ("+
            "name, colors, color_identity, cmc, mana_cost, "+
            "type, keywords, oracle, image_uri) "+
            "VALUES (?,?,?,?,?,?,?,?,?);", [
                card_dict["name"],
                str(card_dict["colors"]),
                str(card_dict["color_identity"]),
                card_dict["cmc"],
                str(card_dict["mana_cost"]),
                card_dict["type_line"],
                str(card_dict["keywords"]),
                oracle,
                card_dict["image_uris"]["png"]
            ])

def two_faced_card_handler():
    pass

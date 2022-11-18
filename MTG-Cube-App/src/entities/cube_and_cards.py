import requests
import json
import time
import sqlite3


class Cube:
    #Tämä luokka toimii yksittäisenä kokoelmana, johon voi tallettaa kortteja
    def __init__(self, name):
        self.name = name
        self.collection = []
        self.card_names = []

    def add_card(self, name):
        initial_load = CardData(name).card_dict
        if initial_load['name'] in self.card_names:
            print(f"{initial_load['name']} on jo cubessa")
        else:
            self.collection.append(Card(initial_load['name']))
            self.card_names.append(initial_load['name'])

    def __str__(self):
        return self.name

class Card:
    #Tämä vastaa yksittäistä korttia. Kortille määritellään alustavasti nimi, mutta myöhemmin lisää ominaisuuksia
    def __init__(self, name:str):
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
        self.pt = ""
        if "p/t" in card_dict.keys():
            self.pt = card_dict["p/t"]
        
    def __str__(self):
        return self.name

class CardData:
    def __init__(self, name):
        self.card_dict = {}
        db = sqlite3.connect(f"src/entities/fetched_cards/fetched_cards.db")
        db.isolation_level = None
        card_data = db.execute("SELECT * FROM Cards WHERE name LIKE ?", [name]).fetchone()
        if card_data != None:
            self.card_dict["name"] = card_data[1]
            self.card_dict["colors"] = card_data[2]
            self.card_dict["color_identity"] = card_data[3]
            self.card_dict["cmc"] = card_data[4]
            self.card_dict["mana_cost"] = card_data[5]
            self.card_dict["type_line"] = card_data[6]
            self.card_dict["keywords"] = card_data[7]
            self.card_dict["oracle_text"] = card_data[8]
            self.card_dict["image_uris"] = {"png":card_data[9]}
            if card_data[10] != None:
                self.card_dict["p/t"] = card_data[10]
        else:
            name_for_api = name.replace(" ","+")
            name_for_api = name_for_api.replace("/","")
            name_for_api = name_for_api.replace(",","")
            card_data_api = requests.get(f"https://api.scryfall.com/cards/named?exact={name_for_api}")
            time.sleep(0.1)
            if card_data_api.status_code == 200:
                self.card_dict = json.loads(jprint(card_data_api.json()))
                db = sqlite3.connect(f"src/entities/fetched_cards/fetched_cards.db")
                db.isolation_level = None
                oracle = ""
                if "oracle_text" in self.card_dict.keys(): 
                        oracle = self.card_dict["oracle_text"]
                else:
                    for i in self.card_dict["card_faces"]:
                        oracle += i["oracle_text"] + "//"
                if "power" in self.card_dict.keys():
                    self.card_dict["p/t"] = str(self.card_dict["power"])+"/"+str(self.card_dict["toughness"])
                    db.execute("INSERT INTO Cards (name, colors, color_identity, cmc, mana_cost, type, keywords, oracle, image_uri, p_t) VALUES (?,?,?,?,?,?,?,?,?,?);",[
                        self.card_dict["name"],
                        str(self.card_dict["colors"]),
                        str(self.card_dict["color_identity"]),
                        self.card_dict["cmc"],
                        str(self.card_dict["mana_cost"]),
                        self.card_dict["type_line"],
                        str(self.card_dict["keywords"]),
                        oracle,
                        self.card_dict["image_uris"]["png"],
                        self.card_dict["p/t"]
                        ])
                else:
                    db.execute("INSERT INTO Cards (name, colors, color_identity, cmc, mana_cost, type, keywords, oracle, image_uri) VALUES (?,?,?,?,?,?,?,?,?);",[
                        self.card_dict["name"],
                        str(self.card_dict["colors"]),
                        str(self.card_dict["color_identity"]),
                        self.card_dict["cmc"],
                        str(self.card_dict["mana_cost"]),
                        self.card_dict["type_line"],
                        str(self.card_dict["keywords"]),
                        oracle,
                        self.card_dict["image_uris"]["png"]
                        ])

def card_test(name: str):
    db = sqlite3.connect(f"src/entities/fetched_cards/fetched_cards.db")
    db.isolation_level = None
    card_data = db.execute("SELECT * FROM Cards WHERE name LIKE ?", [name]).fetchone()
    if card_data != None:
        return True
    name_for_api = name.replace(" ","+")
    name_for_api = name_for_api.replace("/","")
    name_for_api = name_for_api.replace(",","")
    response = requests.get(f"https://api.scryfall.com/cards/named?exact={name_for_api}")
    time.sleep(0.1)
    if response.status_code == 200:
        return True



def jprint(obj):
    #Converts json object to string
    data = json.dumps(obj, sort_keys=True, indent=4)
    return data
    

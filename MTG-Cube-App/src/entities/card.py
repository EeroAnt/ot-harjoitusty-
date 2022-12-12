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
    # Yhdistetään tietokantaan
    d_b = sqlite3.connect("src/data/fetched_cards/fetched_cards.db")
    d_b.isolation_level = None
    # Kurkataan fetched_cards.db, jos sieltä löytyisi rivi
    card_data = d_b.execute(
        "SELECT * FROM Cards WHERE name LIKE ?", [name]).fetchone()
    # Jos löytyi, meillä on kortti
    if card_data is not None:
        return True
    # Jos ei löytynyt lokaalista tietokannasta, koitetaan internetsiä
    if data_from_api(name) is not False:
        return True
    # Jos kummastakaan ei löytynyt. Sen nimistä korttia ei cubeen
    # tällä saa
    return False

# Tämä kääntää json-objektin luettavaan muotoon merkkijonoksi
def jprint(obj):
    data = json.dumps(obj, sort_keys=True, indent=4)
    return data

# Tämä hakee yksittäisen kortin tiedot lokaalista tietokannasta
def data_from_db(name):
    # Yhdistetään tietokantaan
    d_b = sqlite3.connect("src/data/fetched_cards/fetched_cards.db")
    d_b.isolation_level = None
    # Haetaan kortin rivi
    card_data = d_b.execute("SELECT * FROM Cards WHERE name LIKE ?", [name]).fetchone()
    # Pilkotaan sarakkeet sanakirjaan
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
    # Kaikilla korteilla ei ole Power- ja Toughness-arvoja,
    # niille luodaan avain sanakirjaan vain tarvittaessa
    if card_data[10] is not None:
        card_dict["power"] = card_data[10]
        card_dict["toughness"] = card_data[11]
    # Palautetaan luotu sanakirja
    return card_dict

# Tämä hakee kortin tiedot internetistä
def data_from_api(name:str):
    # Pilkotaan kortin nimi api-kutsulle kelpaavaksi
    name_for_api = name.replace(" ", "+")
    name_for_api = name_for_api.replace("/", "")
    name_for_api = name_for_api.replace(",", "")
    # Tehdään api-kutsu
    card_data_api = requests.get(
        "https://api.scryfall.com/cards/named?exact="+
        name_for_api, timeout=10)
    #scryfall-apin dokumentaatiossa oli pyyntö, ettei useammin tehtäisi kutsuja
    time.sleep(0.1)
    card_dict = json.loads(jprint(card_data_api.json()))
    # Erilaisilla korteilla on erilainen rakenne jsonissa.
    # Käsitteekseni kaikki, muut paitsi kaksipuoleiset
    # kortit menevät jo olemassaolevalla rakenteella läpi.
    if "name" not in card_dict.keys():
        return False
        # two_faced_card_handler()
    else:
        # Syötetään löydetyistä tiedoista olennaiset osat lokaaliin
        # tietokantaan ja ladataan kuva talteen
        api_data_to_db(card_dict)
        image = requests.get(
        card_dict["image_uris"]["png"],allow_redirects=True, timeout=10)
        with open("src/data/fetched_cards/"+name_for_api.lower()+".png", 'wb') as pic:
            pic.write(image.content)
        # Jonka jälkeen kortti kasataan juuri luodun tietokantarivin
        # perusteella. Näin ei tarvinnut miettiä uudestaan tiedon muotoilua
        return data_from_db(name)


def api_data_to_db(card_dict):
    # tuplakorteilla (eri kuin kaksipuoleiset) on oracle-teksti
    # eri tavoin kuin yksinkertaisilla korteilla.
    # Katso esimerkiksi Carnival // Carnage testilistasta.
    # oracle pitää löytyä, mutta se voi olla tyhjäkin
    oracle = ""
    # Yksinkertaisilla korteilla se löytyy suoraan
    if "oracle_text" in card_dict.keys():
        oracle = card_dict["oracle_text"]
    # Jos korteilla on kahdet "kasvot", pitää molempien omat
    # tekstit hakea erikseen. Tuplakorttien kohdalla yhdistän
    # ne kahdella /-merkillä
    else:
        for i in card_dict["card_faces"]:
            oracle += i["oracle_text"] + "//"
    # Yhdistetään tietokantaan
    d_b = sqlite3.connect("src/data/fetched_cards/fetched_cards.db")
    d_b.isolation_level = None
    # Jos kyseessä kortilla on power-arvo, sillä on myös toughness-arvo.
    # Tehdään rivit tietokantaan sen mukaisesti
    if "power" in card_dict.keys():
        d_b.execute("INSERT INTO Cards (name, colors, color_identity, "+
            "cmc, mana_cost, type, keywords, oracle, image_uri, power, toughness)"+
            " VALUES (?,?,?,?,?,?,?,?,?,?,?);", [
                card_dict["name"],
                str(card_dict["colors"]),
                str(card_dict["color_identity"]),
                card_dict["cmc"],
                str(card_dict["mana_cost"]),
                card_dict["type_line"],
                str(card_dict["keywords"]),
                oracle,
                card_dict["image_uris"]["png"],
                card_dict["power"],
                card_dict["toughness"]
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

# def two_faced_card_handler():
#     print("Kaksipuoleisten korttien tuki tulossa toivottavasti myöhemmin")

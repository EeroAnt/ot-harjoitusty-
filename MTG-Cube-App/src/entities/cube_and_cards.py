import requests
import json

class Cube:
    #Tämä luokka toimii yksittäisenä kokoelmana, johon voi tallettaa kortteja
    def __init__(self, name):
        self.name = name
        self.collection = []

    def add_card(self, name):
        initial_load = CardData(name).card_dict       
        if initial_load['name'] in self.collection:
            print(f"{Card(name)} on jo cubessa")
        else:
            self.collection.append(Card(initial_load['name']))

    def __str__(self):
        return self.name

class Card:
    #Tämä vastaa yksittäistä korttia. Kortille määritellään alustavasti nimi, mutta myöhemmin lisää ominaisuuksia
    def __init__(self, name:str):
        self.name = name
        card_dict = CardData(name).card_dict
        self.cmc = int(card_dict["cmc"])
        self.type = card_dict["type_line"]

    def __str__(self):
        return self.name

class CardData:
    def __init__(self, name):
        name_for_api = name.replace(" ","+")
        card_data = requests.get(f"https://api.scryfall.com/cards/named?exact={name_for_api}")
        if card_data.status_code == 200:
            self.card_dict = json.loads(jprint(card_data.json()))
        else:
            return False    

def card_test(name: str):
    name_for_api = name.replace(" ","+")
    response = requests.get(f"https://api.scryfall.com/cards/named?exact={name_for_api}")
    if response.status_code == 200:
        return True

# response = requests.get("https://api.scryfall.com/cards/named?exact=black+lotus")
# print(response.status_code)


def jprint(obj):
    #Converts json object to string
    data = json.dumps(obj, sort_keys=True, indent=4)
    return data
    
# print(jprint(response.json()))
cube = Cube("any")
cube.add_card("Black Lotus")
for i in cube.collection:
    print(i, i.cmc, i.type)
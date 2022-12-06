# import json
# import time
# import sqlite3
# import requests
from entities.card import Card, CardData


class Cube:
    # Tämä luokka toimii yksittäisenä kokoelmana, johon voi tallettaa kortteja
    def __init__(self, name):
        self.name = name
        self.collection = []
        self.card_names = []

    def add_card(self, name):
        initial_load = CardData(name).card_dict
        for i in initial_load:
            if i == 'name':
                if initial_load['name'] in self.card_names:
                    print(f"{initial_load['name']} on jo cubessa")
                else:
                    self.collection.append(Card(initial_load['name']))
                    self.card_names.append(initial_load['name'])

    def remove_card(self, name):
        if name in self.card_names:
            self.card_names.remove(name)
            self.collection.remove(Card(name))
        else:
            print(f"{name} nimellä ei löytynyt korttia Cubesta")

    def __str__(self):
        return self.name

from entities.card import Card, CardData, card_test
from card_list_text_files.card_list_text_file_handler import lister


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

    def add_cards_from_list(self, name_of_txt_file):
        card_list = lister(name_of_txt_file)
        cards_to_be_added = []
        cards_failed_to_add = []
        cards_already_in = []
        for i in card_list:
            if card_test(i):
                cards_to_be_added.append(i)
            else:
                cards_failed_to_add.append(i)
        for i in cards_to_be_added:
            if i in self.card_names:
                cards_already_in.append(i)
            else:
                self.add_card(i)
        print("Kortit, joita ei tunnistettu:\n")
        for i in cards_failed_to_add:
            print(i)
        print("Kortit, jotka olivat jo cubessa:\n")
        for i in cards_already_in:
            print(i)

    def remove_card(self, name):
        if name in self.card_names:
            self.card_names.remove(name)
            for i in self.collection:
                if i.name == name:
                    card = i
            self.collection.remove(card)
        else:
            print(f"{name} nimellä ei löytynyt korttia Cubesta")

    def __str__(self):
        return self.name

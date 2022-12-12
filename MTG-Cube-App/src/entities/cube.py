from entities.card import Card, CardData, card_test
from card_list_text_files.card_list_text_file_handler import lister


class Cube:
    # Tämä luokka toimii yksittäisenä kokoelmana, johon voi tallettaa kortteja
    def __init__(self, name):
        self.name = name
        # collection sisältää itse kortti-oliot
        self.collection = []
        # card_names sisältää ainoastaan korttien nimet
        self.card_names = []

    # Kortin lisäys
    def add_card(self, name):
        # haetaan raakaversio kortin tiedoista
        initial_load = CardData(name).card_dict
        # Kortin raakaversiolla on oltava nimi. Koodi
        # kaataisiohjelman kaksipuolisten korttien kohdalla muuten
        if initial_load is not None:
            if 'name' in initial_load.keys():
                # Tarkistetaan, löytyykö kortti jo cubesta.
                # Duplikaatteja ei sallita
                if initial_load['name'] in self.card_names:
                    print(f"{initial_load['name']} on jo cubessa")
                # Jos ei löydy, lisätään se
                else:
                    self.collection.append(Card(initial_load['name']))
                    self.card_names.append(initial_load['name'])

    # Korttien lisäys tekstitiedostosta
    def add_cards_from_list(self, name_of_txt_file):
        # Muutetaan tekstitiedoston sisältö listaksi lister-moduulilla
        card_list = lister(name_of_txt_file)
        # Alustetaan lisättävien, ei käypien ja cubesta jo löytyvien listat
        cards_to_be_added = []
        cards_failed_to_add = []
        cards_already_in = []
        # Jaetaan card_listin sisältö lisättäviin ja ei käypiin
        for i in card_list:
            if card_test(i):
                cards_to_be_added.append(i)
            else:
                cards_failed_to_add.append(i)
        # Lisätään lisättävisti ne, joita ei vielä cubessa ole,
        # loput laitetaan jo löytyvien listalle
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

    # Kortin poistaminen cubesta
    def remove_card(self, name):
        # Tarkistetaan, että kortti löytyy cubesta
        if name in self.card_names:
            # Poistetaan se korttien nimien listalta
            self.card_names.remove(name)
            # Etsitään kortti-olio omalta listaltaan
            for i in self.collection:
                if i.name == name:
                    card = i
            # Poistetaan se. (Näyttää kömpelöltä, mutta piti iteroida
            # loppuun, ennen kuin sai muuttaa listan sisältöä)
            self.collection.remove(card)
        # Jos poistettavaa korttia ei löydy, tulostetaan tieto siitä
        else:
            print(f"{name} nimellä ei löytynyt korttia Cubesta")

    def __str__(self):
        return self.name

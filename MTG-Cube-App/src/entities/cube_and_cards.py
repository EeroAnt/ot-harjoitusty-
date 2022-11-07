
from string import ascii_lowercase

class Cube:
    #Tämä luokka toimii yksittäisenä kokoelmana, johon voi tallettaa kortteja
    def __init__(self, name):
        self.name = name
        self.collection = []

    def add_card(self, name):
        if Card(name) not in self.collection:
            self.collection.append(Card(name))
        else:
            print(f"{Card(name)} on jo cubessa")

    def __str__(self):
        return self.collection #väliaikainen ratkaisu


class Card:
    #Tämä vastaa yksittäistä korttia. Kortille määritellään alustavasti nimi, mutta myöhemmin lisää ominaisuuksia
    def __init__(self, name:str):
        self.name = name.ascii_lowercase

    def __str__(self):
        return self.name
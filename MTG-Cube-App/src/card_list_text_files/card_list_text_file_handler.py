import os

# Tämä muuntaa tekstitiedoston sisällön listaksi. Rivinvaihto erottelee alkiot.
def lister(filename):
    # Tässä luodaan polku hakemistoon
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    # Tässä avataan hakemistosta löytyvä tekstitiedosto
    with open(os.path.join(__location__, filename), "r", encoding='UTF-8') as file:
        list_of_cards = file.readlines()
    # Alustetaan palautettava lista ja lisätään siihen rivit ilman rivinvaihtoja
    list_to_return = []
    for i in list_of_cards:
        list_to_return.append(i[:len(i)-1])
    return list_to_return

import os


def lister(filename):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, filename), "r", encoding='UTF-8') as file:
        list_of_cards = file.readlines()
    list_to_return = []
    for i in list_of_cards:
        list_to_return.append(i[:len(i)-1])
    list_to_return.pop()
    return list_to_return

# print(lister("Testilista.txt"))

import os

def lister(filename):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    list = open(os.path.join(__location__, filename)).readlines()
    list_to_return = []
    for i in list:
        list_to_return.append(i[:len(i)-1])
    list_to_return.pop()
    return list_to_return

lister("Testilista.txt")
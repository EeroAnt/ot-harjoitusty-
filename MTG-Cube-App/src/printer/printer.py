from entities.cube import Cube

def print_list_table(name_of_cube:Cube):
    print("Nimeä tuloste: ")
    name_list = get_input()
    with open(f"src/printer/Printed_lists/{name_list}.html","w",encoding='UTF-8') as file:
        file.write("<!DOCTYPE html>\n<html>"+
        '<head><link rel="stylesheet" href="style.css"></head>\n'+
        "\n<body>\n<h1>"+name_list+"</h1>\n<section>\n<table>\n")
        file.write("<tr>\n"+
        "<th >Card Name</th>\n"+
        "<th>Colors</th>\n"+
        "<th>Color Identity</th>\n"+
        "<th>Mana Cost</th>\n"+
        "<th>Type</th>\n"+
        "<th>Oracle Text</th>\n"+
        "<th>Power</th>\n"+
        "<th>Toughness</th>\n"+
        "</tr>")
        for i in name_of_cube.collection:
            file.write("<tr>\n"+
            f'<td>{i.name}\n'+
            f"<td>{i.colors}</td>\n"+
            f"<td>{i.color_id}</td>\n"+
            f"<td>{i.mana_cost}</td>\n"+
            f"<td>{i.type}</td>\n"+
            f"<td>{i.text}</td>\n"+
            f"<td>{i.power}</td>\n"+
            f"<td>{i.toughness}</td>\n"+
            "</tr>")
        file.write("</table>\n</section>\n")
        file.write("</body>\n</html>")

def print_list_imgs(name_of_cube:Cube):
    print("Nimeä tuloste: ")
    name_list = get_input()
    with open(f"src/printer/Printed_lists/{name_list}.html","w",encoding='UTF-8') as file:
        file.write("<!DOCTYPE html>\n<html>"+
        '<head><link rel="stylesheet" href="img_style.css"></head>\n'+
        "\n<body>\n<h1>"+name_list+"</h1>\n<section>\n")
        for i in name_of_cube.collection:
            file.write(f'<img src="../../data/fetched_cards/{i.name_for_img}.png"/>\n')
        file.write("</section>\n</body>\n</html>")

def get_input():
    return input()
# def print_from_db(name_of_cube:str):

# for i in name_of_cube.collection:
#     file.write(f'<img src="../data/fetched_cards/{i.name_for_img}.png"/>\n')
        
from entities.cube_and_cards import Cube

def print_list(name_of_cube:Cube):
    name_list = input("Nimeä tuloste: ")
    with open(f"src/entities/Printed_lists/{name_list}.html","w",encoding='UTF-8') as file:
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
        "<th>P/T</th>\n"+
        "</tr>")
        for i in name_of_cube.collection:
            file.write("<tr>\n"+
            f'<td>{i.name}\n'+
            f"<td>{i.colors}</td>\n"+
            f"<td>{i.color_id}</td>\n"+
            f"<td>{i.mana_cost}</td>\n"+
            f"<td>{i.type}</td>\n"+
            f"<td>{i.text}</td>\n"+
            f"<td>{i.p_t}</td>\n"+
            "</tr>")
        file.write("</table>\n</section>\n<aside>")
        for i in name_of_cube.collection:
            file.write(f'<img src="../fetched_cards/{i.name_for_img}.png"/>\n')
        file.write("</aside>")
        file.write("</body>\n</html>")

# def print_from_db(name_of_cube:str):

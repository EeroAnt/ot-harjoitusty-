from cube_and_cards import Cube

def print_list(name_of_cube:Cube):
    with open(f"src/entities/Printed_lists/{name_of_cube}.html","w",encoding='UTF-8') as file:
        file.write("<!DOCTYPE html>\n<html>\n<body>\n<h1>"+name_of_cube.name+"</h1>\n<table>\n")
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
            f'<td><span>{i.name}</span><img src="fetched_cards/{i.img_location}"/></td>\n'+
            f"<td>{i.colors}</td>\n"+
            f"<td>{i.color_id}</td>\n"+
            f"<td>{i.mana_cost}</td>\n"+
            f"<td>{i.type}</td>\n"+
            f"<td>{i.text}</td>\n"+
            f"<td>{i.p_t}</td>\n"+
            "</tr>")
        file.write("</table>\n</body>\n</html>")

# def print_from_db(name_of_cube:str):

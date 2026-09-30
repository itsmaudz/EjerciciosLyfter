def add_line_to_file(path):
    line_to_add = input('Ingrese la linea a agregar: ')
    with open(path, 'a', encoding='utf-8') as file:
        file.write(line_to_add + '\n')

add_line_to_file('canciones.txt')
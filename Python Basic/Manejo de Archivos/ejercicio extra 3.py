def turn_capital_letter(path,out_path):
    with open(path, 'r', encoding='utf-8') as file:
        new_file = file.read()
        capital_file = new_file.upper()

    with open(out_path, 'w', encoding='utf-8') as file:
        file.write(capital_file)


turn_capital_letter('canciones.txt','nuevo archivo de mayusculas.txt')
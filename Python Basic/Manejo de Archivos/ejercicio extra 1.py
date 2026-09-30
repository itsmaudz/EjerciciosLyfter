def remove_line_breaks(input_path,output_path):
    new_list = []
    with open(input_path, 'r', encoding='utf-8' ) as file:
        for line in file:
            new_line = line.strip()
            new_list.append(new_line)
    result = ' '.join(new_list)

    with open (output_path, 'w', encoding='utf-8') as file:
        file.write(result)

remove_line_breaks('saltos de linea.txt','nuevos saltos de linea.txt')
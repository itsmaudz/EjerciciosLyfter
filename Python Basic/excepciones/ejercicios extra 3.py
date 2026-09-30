my_list = ['10', 'manzana', '5.5', '3', 'n/a']

def sum_values(my_list):
    total = 0
    for element in my_list:
        try:
            number = float(element)
            total += number
            print(f'{element} sumado correctamente')            

        except ValueError:
            print(f'Elemento invalido: {element}')

    print(f'total de la suma: {total}')

(sum_values(my_list))
my_list = ['4', 'hola', '10', '5.2', '@@@', '0']

def convert_to_integer(numbers):
    result = []
    for index in numbers:
        try:
            integer = int(index)
            result.append(f'{index} convertido a {integer}')

        except ValueError:
            result.append(f'No se pudo convertir el elemento: {index}')

    return result  


final_result = convert_to_integer(my_list)

for element in final_result:
    print(element)

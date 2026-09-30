

list = []
counter = 0

number_list = int(input('Cuantos numero va a tener  la lista: '))
number_to_search = int(input('Numero a buscar: '))

for i in range(number_list):

    number = int(input('ingrese una lista de numeros: '))
    
    list.append(number)

    if number == number_to_search:
        counter += 1


print(f'El numero {number_to_search} aparece {counter} veces')
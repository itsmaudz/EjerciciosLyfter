list = []
new_list = []
flag = False

for index in range(0,5):
    word = input(f'Escriba la palabra {index+1}: ')

    list.append(word)

print(f'Primera lista es: {list}')

for index in range(len(list)):
        
    if len(list[index]) > 4:
        
        new_list.append(list[index])
        flag = True


if flag == False:
    print('La lista no tiene palabras mayores a 4 letras, por lo tanto no se pudo generar una nueva lista')

if flag == True:
    print(f'La nueva lista es: {new_list}')





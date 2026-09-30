list_1 = ["cielo", "sol", "maravilloso", "día"]
min_length = int(input("Ingrese el numero de letras minimas en la palabra: "))

def filter_words(list_1,min_length):
    new_list = []
    for word in list_1:
        if len(word) >= min_length:
            new_list.append(word)

    if not new_list:
        return 'No hay palabras con ese minimo de letras'

    return new_list

print(filter_words(list_1,min_length))
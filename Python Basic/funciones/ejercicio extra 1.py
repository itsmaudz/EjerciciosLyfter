text = 'programacion'
character = input('Ingrese el caracter que desea buscar: ')

def find_character(text,character):
    count = 0
    for letter in text:
        if letter == character:
            count += 1
        
    return count

print(find_character(text,character))
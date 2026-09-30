def get_name(message):

        name = input(message)

        if name.isdigit():
            raise ValueError('El nombre no pueder ser un numero')

        return name

def get_age(message):
    try:
        return int(input(message))
    
    except ValueError:
        raise ValueError('Número no valido')

def main():
    try:
        name = get_name('ingrese su nombre: ')
        age = get_age('ingrese su edad: ')
        print(f'hola {name}, su edad es {age}')
        
    except ValueError as ex:
        print(ex)

main()
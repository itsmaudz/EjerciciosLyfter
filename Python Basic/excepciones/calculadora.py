def show_menu(first_number):
    print(f'Numero actual: {first_number}')
    
    print('Elija una de las  siguientes opciones:')
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicación')
    print('4. División')
    print('5. Borrar resultado')
    print('6. Salir')

    option = input('Elija una de las  siguientes opciones: ')

    return option

def add(current,number):
    return current + number

def subtract(current,number):
    return current - number

def multiply(current,number):
    return current * number

def divide(current,number):
    if number == 0: 
        raise ZeroDivisionError
    else:
        return current / number

def reset():    return 0

def main():
    current_number = int(input('ingrese el primer numero de su operacion: '))
    
    while True:
        option = show_menu(current_number)
        if option == '1':
            try:
                number = int(input('Ingrese el numero a sumar: '))
                current_number = add(current_number,number)

            except ValueError as ex:
                print(f'Ha ocurrido un error al convertir este string a numero: {ex}')

        elif option == '2':
            try:
                number = int(input('Ingrese el numero a restar: '))
                current_number = subtract(current_number,number)
            
            except ValueError as ex:
                print(f'Ha ocurrido un error al convertir este string a numero: {ex}')

        elif option == '3':
                try:
                    number = int(input('Ingrese el numero a multiplicar: '))
                    current_number = multiply(current_number,number)
                
                except ValueError as ex:
                    print(f'Ha ocurrido un error al convertir este string a numero: {ex}')

        elif option == '4':
                try:
                    number = float(input('Ingrese el numero a dividir: '))
                    current_number = divide(current_number,number)
                
                except ValueError as ex:
                    print(f'Ha ocurrido un error al convertir este string a numero: {ex}')

                except ZeroDivisionError as ex:
                    print(f'Ha ocurrido un error al intentar divir entre cero : {ex}')

        elif option == '5':
                current_number = reset()

        elif option == '6':
            break

        else: 
            print('Opcion invalida')

main()

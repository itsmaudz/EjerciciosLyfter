print( "ingrese 3 numeros y te diremos cual es el mayor")

number_1 = int(input("ingrese el primer numero: " ))
number_2 = int(input("ingrese el segundo numero: "))
number_3 = int(input("ingrese el tercer número: "))

if number_1 > number_2:
    if number_1 > number_3:
        print(f"el numero mayor es: {number_1}")
    else:    
        print(f"el numero mayor es: {number_3}")
elif number_2 > number_3:
    print(f"el numero mayor es: {number_2}")
else:
    print(f"el numero mayor es: {number_3}")

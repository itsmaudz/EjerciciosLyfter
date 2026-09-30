import random

print("......adivina el numero secreto......")

secret_number = random.randint(1,10)
number = int(input( "adivina el numero del 1 a 10: "))
while secret_number != number:
    print ( "sigue intentando")
    number = int(input( "intenta otra vez: "))
else:
    print ("Adivinaste")

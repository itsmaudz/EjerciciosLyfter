number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
number_3 = int(input("Enter the third number: "))

if number_1 == 30 or number_2 == 30 or number_3 == 30:
    print("true")
elif number_1 + number_2 + number_3 == 30:
    print("true")
else:
    print("false")
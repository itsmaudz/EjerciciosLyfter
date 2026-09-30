# ejercicio 2.1

def get_sum():
    number_1 = 1
    number_2 = 2
    total = number_1 + number_2


print(total)
print(number_1)



# ejercicio 2.2

global_variable = 700


def get_sum():
    global global_variable
    number_1 = 100
    number_2 = 500
    total = number_1 + number_2
    global_variable += 700 + total

print(global_variable)





new_list=[]
compare = 0
for i in range(10):
    number = int(input(f"ingrese el {i+1}, numero: "))
    new_list.append(number)

    if i == 0:
        compare = number
    else:
        if number > compare:
            compare = number


print(new_list, "El número mayor es:", compare)

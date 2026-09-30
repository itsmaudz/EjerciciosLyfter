list = [5,10,15,20,25,30,35,40,45,50,55,60,65,70]
new_list = []
average = 0
sum = 0
for index in range(0,len(list)):
    sum += list[index]
    average = sum/len(list)

for index in range(0,len(list)):
    
    if list[index] > average:
        new_list.append(list[index])

print(f'Promedio de la lista: {average}')   

print(new_list)
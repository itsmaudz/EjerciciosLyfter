my_list = [1,2,3,4,5,6,7,8,9,10]

new_list = []
for numbers in my_list: 
    if numbers % 2 != 1:

        new_list.append(numbers)

print(new_list)


print("OTHER WAY")

my_list = [1,2,3,4,5,6,7,8,9,10]

for numbers in range(len(my_list)-1,-1,-1): 
    if my_list[numbers] % 2 != 0:

        my_list.pop(numbers)

print(my_list)
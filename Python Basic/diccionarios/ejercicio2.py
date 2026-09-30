list_1 = [1,2,3,4,5]
list_2 = ['uno','dos','tres','cuatro','cinco']
new_dictionary = {}

for i in range(len(list_1)):
    new_dictionary[list_1[i]] = list_2[i]


print(new_dictionary)
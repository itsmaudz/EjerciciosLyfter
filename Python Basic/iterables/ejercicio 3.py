print ("WAY 1")

my_list = [1,2,3,4,5,6,7]

A = my_list[0]
B = my_list[-1]

my_list[0] = B     
my_list[-1] = A  

print(my_list)


print("WAY 2")


my_list = [1,2,3,4,5,6,7]

my_list[0], my_list[-1] = my_list[-1], my_list[0] 


print(my_list)
list = [-10,2,3,4,2,3,0,7]
minor = list[0]

for index in range(1,len(list)):
    if list[index] < minor:
        minor = list[index]

print(minor)

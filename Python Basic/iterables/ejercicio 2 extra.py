
list = [1,2,3,4,2,1,1,7]


for index in range(0,len(list)):
    
    read = list[index]
    
    if read > 0:
        positive = True
        
    else:
        positive = False
        break
    
if positive == True:
    print("todos los  valores de la lista son positivos")
else:
    print("Hay al menos un número negativo o cero")
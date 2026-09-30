print("hi" + "world")  #result: "hiworld"

print("hola" + 9)    # result: line 3, in <module>  print("hola" + 9) TypeError: can only concatenate str (not "int") to str

print(10 + "20")    # result: line 6, in <module>  print(10 + "20") TypeError: can only concatenate str (not "int") to str

print([1, 2, 3] + [4, 5, 6])   # result: [1, 2, 3, 4, 5, 6] because the + operator concatenates the two lists together.

print("string" + [1, 2, 3])    # result: line 9, in <module>  print("string" + [1, 2, 3]) TypeError: can only concatenate str (not "list") to str

print(10.52 + 5)    # result: 15.52 because the + operator adds the two numbers together.

print(False + True) # result: 1 because in Python, the boolean values False and True are treated as 0 and 1 respectively when used in arithmetic operations. 
                    #Therefore, False + True is equivalent to 0 + 1, which equals 1.
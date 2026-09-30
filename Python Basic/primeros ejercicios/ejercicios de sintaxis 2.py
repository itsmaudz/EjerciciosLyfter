print("......Age Categories......")

name = (input("please enter your name: "))
lastname = (input("please enter your last name: "))
age = int(input("please enter your age: ")) 

if age < 3:
    category = "baby "
elif age < 12:
    category = "child"
elif age < 18:
    category = "teenager"
elif age < 30:
    category = "young adult"
elif age < 60:
    category = "adult"
else:
    category = "senior"
    
print(f"{name} {lastname}, you are a {category}.")

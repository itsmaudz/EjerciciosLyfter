sum = 0
count = 1

number = int(input("enter a number: "))
while count <= number:
    sum += count
    count += 1

print(f"the sum is: {sum}")
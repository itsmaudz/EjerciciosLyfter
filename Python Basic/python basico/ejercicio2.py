time = int(input("enter the time in seconds: "))
if time < 600:
    time = 600 - time
    print(f"the time in seconds is shorter; the remaining seconds would be: {time}")
elif time > 600:
    print("higher")
else: 
    print("equal")
    
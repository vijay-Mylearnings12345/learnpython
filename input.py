

name1 = input("Please Enter your name: ")
name2 = input("Please Enter second name: ")
age1 = int(input("Please Enter your age1: "))
age2 = int(input("Please Enter your age2: "))

if age1 > age2:
    print(f"{name1} is older than {name2}")
elif age1 < age2:
    print(f"{name2} is older than {name1}")
else:
    print(f"{name1} and {name2} are of the same age")

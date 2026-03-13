# Conditional statements

a = 20
b = 15
if a < 15:
    print("The value of a is lesser than b!")
else:
    print("The value of a is not lesser than b!")


c = [1, 2, 3, 4, 5, 6]
if 2 in c:
    print("Correct")
else:
    print("wrong")


user1 = input("Please Enter the software version number: ")

if user1 >= "26.0.4":
    print("The software version is compatible with the latest features.")
elif user1 < "26.0.4":
    print("The software version is not compatible with the latest features.")
else:
    print("Please enter a valid software version number.")

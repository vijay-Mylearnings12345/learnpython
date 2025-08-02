#Brake, continue,pass

x = int(input("Enter the number of bottles required....! "))

av = 5
i = 1

while i <= x:
    if i > av:
        print("Stock finished. Only", av, "bottles available.")
        break
    print("Bottle", i)
    i += 1
    
    
    
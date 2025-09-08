#Learning the OOPS concept again

from main import Laptop

laptop1 = Laptop("ASUS", "25", "25000INR", "2014", "Yes")
laptop2 = Laptop("HP", "28", "35000INR", "2018", "Yes")

print(laptop1.model)
print(laptop1.size)
print(laptop1.price)
print(laptop1.make_year)
print(laptop1.availability)

print(laptop2.model)
print(laptop2.size)
print(laptop2.price)
print(laptop2.make_year)
print(laptop2.availability)

laptop1.booting_time()

laptop1.shutdown_time()
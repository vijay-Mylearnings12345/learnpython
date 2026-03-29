# Python Object Oriented Program

"""
Objects = Parameters (Variables), Methods (functions)
Class within the same python file
Different class file
"""

class person():
    def __init__(self, name, age, marital_status, live_Status):
     self.name = name
     self.age = age
     self.marital_status = marital_status
     self.live_Status = live_Status
    def capacity(self):
        print(f"{self.name} {self.age} old who's married status is {self.marital_status} and who's live status {self.live_Status} is real!")
    
    def capability(self):
        print(f"{self.name} {self.age} old who's married status is {self.marital_status} and who's live status {self.live_Status} is fake!")
    
    

person1 = person("Vijay",38,"married",True)
person2 = person("Ajay",39,"unmarried",True)
person3 = person("Tejay",40,"unmarried",False)

print(person1.name)
print(person1.age)
print(person1.marital_status)
print(person1.live_Status)



print(person2.name)
print(person2.age)
print(person2.marital_status)
print(person2.live_Status)


print(person3.name)
print(person3.age)
print(person3.marital_status)
print(person3.live_Status)

print(person1.capacity())
print(person1.capability())

print(person2.capacity())
print(person2.capability())

print(person3.capacity())
print(person3.capability())


#Example2

class gateway():
    def __init__(self, board, version, release_date, test_status):
     self.board = board
     self.version = version
     self.release_date = release_date
     self.test_status = test_status
    def release_status(self):
        print(f"{self.board} {self.version} with the release date {self.release_date} with test cases status as {self.test_status}, recommeded for production release!")  
    

gw1 = gateway("imx8GW",2.3,"July2025","Pass")


print(gw1.board)
print(gw1.version)
print(gw1.release_date)
print(gw1.test_status)



print(gw1.release_status())

#Example3

class house():
    def __init__(self, size, rooms, kitchen, storage):
     self.size = size
     self.rooms = rooms
     self.kitchen = kitchen
     self.storage = storage
    def Samllfamily(self):
        print(f"This house has the following parameters such as the size of the house is {self.size} and the no of rooms are {self.rooms} with big size kitchen {self.kitchen} and the seperate storage room size {self.storage}, recommended for family of 3!")
    def Bigfamily(self):
        print(f"This house has the following parameters such as the size of the house is {self.size} and the no of rooms are {self.rooms} with big size kitchen {self.kitchen} and the seperate storage room size {self.storage}, recommended for family of 3!") 
    

Family1 = house("50sq-m","2","with all aminities","10sq-m")
Family2 = house("70sq-m","3","with all aminities","15sq-m")


print(Family1.size)
print(Family1.rooms)
print(Family1.kitchen)
print(Family1.storage)


print(Family1.Samllfamily())

print(Family2.size)
print(Family2.rooms)
print(Family2.kitchen)
print(Family2.storage)

print(Family2.Bigfamily())
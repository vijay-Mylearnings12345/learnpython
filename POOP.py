# Python Object Oriented Program

"""
Objects = Parameters (Variables), Methods (functions)
Class 
"""

class person():
    def __init__(self, name, age, marital_status, live_Status):
     self.name = name
     self.age = age
     self.marital_status = marital_status
     self.live_Status = live_Status
    def capacity(self):
        print(f"{self.name} {self.age} old who's married status is {self.marital_status} and who's live status {self.live_Status} cant do anything!")
    

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

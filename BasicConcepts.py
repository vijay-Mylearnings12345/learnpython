###Basic Concepts

#Understanding the data types #integers, float, boolean, complex

num1=2
num2=3.5
add = num1 + num2
print('addition is ',add)


a = 10
b = 30
if a < 30:
    print(True)
else:
    print(Flase)
    
    
#Print function
a = 10
b = 5
print("a+b")



#Classes & Objects

class school:
    name1 = ""
    name2 = ""
       
    def teacher(self):
        print("The teacher name is very good")
    

first_teacher = school
second_teacher = school

first_teacher.name1 = "TOM VICTOR"
second_teacher.name2 = "ABDUL"

print(first_teacher.name1)
print(second_teacher.name2)

#conditional statements
#if & else statement

user1=input("Enter the number please", )
user2=input("Enter the number please", )
if user1 > user2:
    print("user1 input number is bigger!")
else:
    print("user1 input number is smaller!")



print=("Enter your name, please!")
name=input()
print=(f"Hello {name}")


User1_D1 =input("Please Enter your Name")
User1_D2=input("Please Enter your age")
User2_D1 =input("Please Enter your Name")
User2_D2=input("Please Enter your age")
if User1_D2>User2_D2:
    print("User1 is Elder! and He/She is the Senior!")
else:
    print("User2 is Elder! and He/She is the Senior!")
    
 
a=40
b=40
if a!=b:
  print("Correct")
else:
  print("Nothing")
  
num1=input("Enter the First Number")
num2=input("Enter the secod Number")
sum = num1 + num2
print("The sume is", sum)

#Constructing the interger, Float and string

x = int(1)
y = int(2.5)
z =int("7.8")
print(x)
print(y)
print(z)



x = float(1)
y = float("2.5")
z =float("0.1")
print(x)
print(y)
print(z)


x = str("1")
y = str(2.5)
z =str("Test")
print(x)
print(y)
print(z)


#Slicing Strings

b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

#String Concatenation

a = "vijaykumar"
b = "chandra sekar"
c = a + b
print(c)


a = "vijaykumar"
b = "chandrasekar"
c = a + " " + b
print(c)

#string methods

txt = "For only {price:.3f} rupees!"
print(txt.format(price = 49))

#comments
"""
This is the part to learn the comments feature
Need to understand the comments
"""
#single line comment
#if 5 > 2
print("The comment line is working as expected")
print("This is the important learing period for me")

#python environment
#windows
 python -m venv myfirstproject
#linux
python -m venv myfirstproject

#Functions

def first_functtion():
    print("This is not the first function")
    
first_function()

def result():
    a=10
    b=12.5
    sum=a+b
    print(sum)
    
result()

def conditional():
    a=500
    b=800
    if a>b:
        print("a is Bigger value")
    else:
        print("a is not the Bigger value")
        
conditional()

#Using Dictionaries in function

def test():
    thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
    print(thisdict)
    
test()
        
def test():
    thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
    print(thisdict["brand"])
    print(thisdict["year"]
    print(thisdict["model"]
    
test()
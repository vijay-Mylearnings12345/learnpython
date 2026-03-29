'''This chapter deals with the variables
All concepts about the variables
Important to know about declarion of global variables'''

#Variables
#Variable names
#Multiple variable & values
#Output Variable
#Global Variable

a='text'
print(a)
b="text"
print(b)
c=5
print(c)
d=7
print(d)
D=7
print(D)

myvar="string"
print(type(myvar))


x=y=z='vijaykumar'
print(x)
print(y)
print(z)

x,y,z=('vijay','kumar','great')
print(x)
print(y)
print(z)

x = 'awesome'
def myfunc():
  x = 'fantastic'
myfunc()
print('Python is always ' + x)

x = "Nice"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print('Python is always ' +x)

x = 'awesome'
def myfunc():
  global x
  x = 'fantastic'
myfunc()
print('Python is ' + x)

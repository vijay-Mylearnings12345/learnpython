# All about sets
"""
How to create a set, set function,
empty set, method, add, remove, clear, discard,
pop,iterating the sets, if -in statement,union,
intersetction,difference, symmetric_difference,
update,intersection_update,
"""


#Set creation

myset ={1,2,3,"vijay",1.5,'True'}
print(myset)


myset =set([1,2,3,'vijay',1.5,'False'])
print(myset)
print(type(myset))

myset =set("VIJAY")
print(myset)


myset =set()
print(type(myset))


myset={}
print(type(myset))

#add, remove,clear,discard

myset =set()
print(type(myset))


myset.add(1)
myset.add(2)
myset.add('vijay')
myset.add('True')
print(myset)

myset.remove(2)
print(myset)

myset.discard(1)
print(myset)

myset.clear()
print(myset)

#pop

myset =set([1,2,"VIJAY"])

myset.pop()
print(myset)

#interating the elements in the set

myset ={1,2,4,5,'vijay','kumar'}
for i in myset:
	print(i)
    

#if in statement

myset ={1,2,4,5,'vijay','kumar'}
if 6 in myset:
	print("Correct")
else:
	print("incorrect")

#Union

even = {2,4,6,8,10}
odd = {0,1,3,5,7,9}
prime = {1,3,5,7,11}


u = odd.union(even)
print(u)

u = even.union(odd)
print(u)


u = even.union(prime)
print(u)

#intersection
even = {2,4,6,8,10}
odd = {0,1,3,5,7,9}
prime = {1,3,5,7,11}


u = odd.intersection(even)
print(u)

u = even.intersection(odd)
print(u)


u = even.intersection(prime)
print(u)

list1 = {1,2,3,4}
list2 = {1,2,3}

i = list1.intersection(list2)
print(i)

# difference

even = {2,4,6,8,10}
odd = {0,1,3,5,7,9}
prime = {1,3,5,7,11}


d = odd.difference(even)
print(d)

d = even.difference(odd)
print(d)



list1 = {1,2,3,4}
list2 = {1,2,3}

d = list1.difference(list2)
print(d)




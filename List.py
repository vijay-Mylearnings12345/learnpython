#List

#Methods - append, copy, clear, count, extend, index, insert, remove, pop, reverese, sort

#Length
list = [ "Name", "age", "Birthcity", "Nationality", "Marrital Status", 38, True, 1.5]
print(len(list))


#append
list = [ "Name", "age", "Birthcity", "Nationality", "Marrital Status", 38, True, 1.5]
list.append("Religion")
print(list)

#copy & Clear
list = [ "Name", "age", "Birthcity", "Nationality", "Marrital Status", 38, True, 1.5]
newlist = list.copy()
newlist.clear()
print(list)
print(newlist)

#Copy & remove
list = [ "Name", "age", "Birthcity", "Nationality", "Marrital Status", 38, True, 1.5, "Religion"]
newlist = list.copy()
newlist.remove("Religion")
print(list)
print(newlist)

#Count
list = [ "Name", "age", "Birthcity", "Nationality", "Marrital Status", 38, True, 1.5, "Religion"]
newlist = list.count("Name")
print(newlist)

list = [ "Name", "age", "Birthcity", "Nationality", "Marrital Status", 38, True, 1.5, "Religion"]
newlist = list.count("a")
print(newlist)

list = [ "Name", "age", "Birthcity", "Nationality", "Marrital Status", 38, True, 1.5, "Religion"]
newlist = list.count(38)
print(newlist)

#Extend
list = [ "Name", "age", "Birthcity", "Nationality", "Marrital Status", 38, True, 1.5, "Religion"]
list1 = [ "City", "Workstatus", "Experience"]
list.extend(list1)
print(list)



























my_list = [1, "text", 2.5, True]

print(my_list)
print(type(my_list))
print(len(my_list))

my_list = list((1, "text", 2.5, True,"constrructor"))
print(my_list)
print(my_list[1])
print(my_list[-1])

print(my_list[2:4])
print(my_list[:4])
print(my_list[2:])


my_list = [1, "text", 2.5, True]
my_list.insert(4,"new item inserted")
print(my_list)


my_list = [1, "text", 2.5, True]
my_list.append("appended new item")
print(my_list)


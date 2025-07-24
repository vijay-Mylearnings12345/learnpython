#List

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


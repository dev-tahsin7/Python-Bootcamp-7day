# List

this_list = ["Tahsin", "Ahmad", 10, 60j, 10.57, "Tahsin"]
# print(type(this_list))
# print(this_list)
# print(this_list[5])
# print(len(this_list))

# The list() Constructor

newList = list(("Tahsin", 10, True))
# print(newList)

# use of in keyword

# if 10 in newList:
#     print("True")
# else:
#     pass

# Change of list items
newList[1] = "Ahmad"
# print(newList)

# insert()

# x = ['Proxima IT', 'Bootcamp', 'Python', 7, 3]
# x.insert(1, 'Tahsin')
# print(x)

# append()
# x.append("P te programming")
# print(x)

# extend()
# y = [1,2,3,4]
# z = ['A', 'B','C']
# y.extend(z)
# print(y)

# remove(), pop(), del keyword, clear() >> to clear the list
# X = ['Proxima IT', 'Bootcamp', 'Python', 7, 3]
# X.remove('Bootcamp')
# X.pop(2)
# del X[0]
# print(X)

# sort(), reverse(), copy()
# a = ['B','A','D','C']
# b = [20,30,50,40,100]
# a.sort()
# a.sort(reverse=True)
# b.sort()
# b.reverse()
# c = b.copy()
# c = a + b >> join list using +
# print()


# ---------------------------------

# Tuple

# this_tuple = ('Tahsin', 'Proxima IT', 7, 'Python')
# print(this_tuple)

# single_tuple = ('iPhone',)
# print(type(single_tuple))

#  tuple() Constructor >> to create a tuple, you can also use tuple()

# Update item to tuple

# x = ('Tahsin','Python','Bootcamp')
# y = list(x) # x convert into list now
# y.append('Proxima IT')
# # print(y)
# x = tuple(y) # now y convert into tuple 3
# print(x)

# unpack
fruits = ("apple", "mango", "banana") # packed
# (a , b , c) = fruits
# print(a)

# fruits = fruits * 2
# print(fruits)

# ---------------------------------------------

# Set

this_set = {'Vijay', 'Messi', 'CR7', 'Bangladesh'}
# print(this_set)

# use of in keyword
# print('Messi' in this_set)

# add() >> to add new item
# update() >> To add items from another set into the current set, use the update() method.

# newSet = {'Proxima IT', 7, 'Day', 'Python'}
# new_set = {10, 20, 30j}
# newSet.add('Bootcamp')
# print(newSet)

# newSet.update(new_set)
# print(newSet)

# set() constructor to make a set.

# Set join >> union() , update() , intersection(), symmetric_difference(), difference()

set_1 = {10,20 ,30, 'Leo', 'Neymar', 'FCB'}
set_2 = {20, 10 , 'Leo', 'Messi', 'Argentina', 'Brazil'}
# set_1 = set_1.union(set_2)
# set_1 = set_1.intersection(set_2)
# set_1 = set_1.difference(set_2)
# set_1 = set_1.symmetric_difference(set_2)
# print(set_1)

# ----------------------------------------

# Dict
this_dict = {
    "name" : "Tahsin",
    "age" : 20,
    "city" : "Sirajganj"
}

# print(this_dict)
# print(this_dict["age"])
# print(this_dict.get("age")) # get() method
# print(this_dict.keys()) # keys()
# print(this_dict.values()) # values()
# print(this_dict.items()) # key, value as tuple

# add item
# this_dict["college"] = "Govt. Science College, Dhaka"
# update()
# this_dict.update({"college" : "GOVT. Science College"})
# print(this_dict)
# print(this_dict.popitem())

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = dict(thisdict)
# print(mydict)



# dict() constructor to make a dictionary.

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child2"])
print(myfamily["child2"]["name"])


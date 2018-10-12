from my_list import CircularPositionalList


list1 = CircularPositionalList()
list1.add_first(2)
list1.add_last(10)
list1.add_after(list1.find(2), 6)
list1.add_before(list1.find(10), 8)
list2 = list1.copy()

print("\nEcco le due liste di riferimento:\n")

print("LIST 1: ", str(list1))
print("LIST 2: ", str(list2))


print("-----------------------------------------------------------")

list1.add_first(-2)
print("ADDED -2 at the beginning of LIST1 ")
list2.add_first(-2)
print("ADDED -2 at the beginning of LIST2 ")
print("LIST 1: ", str(list1))
print("LIST 2: ", str(list2))

print("-----------------------------------------------------------")

list1.add_last(-32)
print("ADDED -32 at the end of LIST1 ")
list2.add_last(-32)
print("ADDED -32 at the end of LIST2 ")
print("LIST 1: ", str(list1))
print("LIST 2: ", str(list2))

print("-----------------------------------------------------------")

print("FOUND 6 IN LIST 1: ", list1.find(6).element() == 6)
print("FOUND 6 IN LIST 2: ", list2.find(6).element() == 6)
print("FOUND -3 IN LIST 1: ", list1.find(-3) == -3)
print("FOUND -3 IN LIST 2: ", list2.find(-3) == -3)

print("-----------------------------------------------------------")

for i in range(10):
    list1.add_first(i)
    print("ADDED ",i," at the beginning of LIST1 ")
    list2.add_first(i)
    print("ADDED ", i, " at the beginning of LIST2 ")
    list1.add_last(i + 11)
    print("ADDED ",i+11," at the end of LIS1 ")
    list2.add_last(i + 11)
    print("ADDED ", i + 11, " at the end of LIST2 ")

print("LIST 1 - len ",len(list1))
print("LIST 1: ", str(list1))

print("LIST 2 - len ",len(list2))
print("LIST 2: ", str(list2))

print("-----------------------------------------------------------")

list3 = list1 + list2
print("LIST 3 - len ",len(list3))
print("LIST 3: ", str(list3))
print("REVERSE OF LIST 3: ", str(list3.reverse()))
print("CLEAR LIST 3")
list3.clear()
print("LIST 3 - len ",len(list3))
print("LIST 3: ", str(list3))


print("-----------------------------------------------------------")

value=list1.add_before(list1.first(),-1)
print("ADDED  ",value.element()," before first of list1")
value=list2.add_before(list2.first(),-1)
print("ADDED  ",value.element()," before first of list1")

value=list1.add_before(list1.find(5),-100)
print("ADDED  ",value.element()," before 5 of list1")
value=list2.add_before(list2.find(5),-100)
print("ADDED  ",value.element()," before 5 of list2")

value=list1.add_after(list1.last(),100)
print("ADDED  ",value.element()," after last of list1")
value=list2.add_after(list2.last(),100)
print("ADDED  ",value.element()," after last of list2")

value=list1.add_after(list1.find(15),-100)
print("ADDED  ",value.element()," after 15 of list1")
value=list2.add_after(list2.find(15),-100)
print("ADDED  ",value.element()," after 15 of list2")

print("AFTER INSERT LIST 1 - len ",len(list1))
print("AFTER INSERT LIST 2 - len ",len(list2))

print("LIST 1: ", str(list1))
print("LIST 2: ", str(list2))

print("-----------------------------------------------------------")
print("FIND -100 AND -101010 in LIST 1:")
print(list1.find(-100).element())
print(list1.find(-101010))
print("FIND -100 AND -101010 in LIST 1:")
print(list2.find(-100).element())
print(list2.find(-101010))

print("-----------------------------------------------------------")

print("LIST 1: ", str(list1))
print("LIST 2: ", str(list2))
print("FIND 1 in LIST 1 AND USE get_item:")
print(list1[list1.find(1)])
print("FIND 1 in LIST 2 AND USE get_item:")
print(list2[list2.find(1)])

print("IS 1 CONTAINED IN LIST 1?")
print(list1.find(1) in list1)
print("Is 1 CONTAINED IN LIST 2?")
print(list2.find(1) in list2)

print("IS 27 CONTAINED IN LIST 1?")
try:
    list3.add_first(27)
    pos = list3.first()
    print(pos in list1)
    print("27 is contained in LIST 1")
except ValueError or TypeError :
    print("p does not belong to this container, so it isn't contained")

print("IS 27 CONTAINED IN LIST 2?")
try:
    list3.add_first(27)
    pos = list3.first()
    print(pos in list2)
    print("27 is contained in LIST 2")
except ValueError or TypeError :
    print("p does not belong to this container, so it isn't contained")

print("-----------------------------------------------------------")

print("LIST 1: ", str(list1))
print("LIST 2: ", str(list2))
print("DELETE 1 IN LIST 1")
del list1[list1.find(1)]
print("LIST 1: ", str(list1))
print("DELETE 1 IN LIST 2")
del list2[list2.find(1)]
print("LIST 2: ", str(list3))

print("-----------------------------------------------------------")

list1.delete(list1.find(9))
print("DELETE 9 IN LIST 1")
print("LIST 1: ", str(list1))
list2.delete(list2.find(9))
print("DELETE 9 IN LIST 2")
print("LIST 2: ", str(list2))

print("-----------------------------------------------------------")


print("REPLACE -100 WITH -500 in LIST 1")
old_element = list1.replace(list1.find(-100), -500)
print("LIST 1: ", str(list1))
print("OLD ELEMENT: ", str(old_element))

print("REPLACE -100 WITH -500 in LIST 2")
old_element = list2.replace(list2.find(-100), -500)
print("LIST 2: ", str(list2))
print("OLD ELEMENT: ", str(old_element))

print("-----------------------------------------------------------")

print("REPLACE 27 (not exist) WITH -27 in LIST 1")
try:
    old_element = list1.replace(list1.find(27), -27)
    print("LIST 1: ", str(list1))
    print("OLD ELEMENT: ", str(old_element))
except TypeError:
    print("ELEMENT DOES NOT EXSIST")

print("REPLACE 27 (not exist) WITH -27 in LIST 2")
try:
    old_element = list2.replace(list2.find(27), -27)
    print("LIST 2: ", str(list2))
    print("OLD ELEMENT: ", str(old_element))
except TypeError:
    print("ELEMENT DOES NOT EXSIST")

print("-----------------------------------------------------------")

print("LIST 1: ", str(list1))
print("REPLACE 12 WITH -1000 in LIST 1")
list1[list1.find(12)]= -1000
print("LIST 1: ", str(list1))

print("LIST 2: ", str(list2))
print("REPLACE 12 WITH -1000 in LIST 2")
list2[list2.find(12)]= -1000
print("LIST 2: ", str(list2))

print("-----------------------------------------------------------")

print("LIST 1: ", str(list1))
print("LIST 2: ", str(list2))
print("CLEAR LIST 1 AND LIST 2")
list1.clear()
list2.clear()
print("LIST 1: ", str(list1))
print("LIST 2: ", str(list2))

print("REVERSE OF LIST 1: ", str(list1.reverse()))              #reverse of an empty list
print("REVERSE OF LIST 2: ", str(list2.reverse()))              #reverse of an empty list


list1.add_first(-2)
print("ADDED -2 to LIST1")
list2.add_first(-2)
print("ADDED -2 to LIST2")
print("LIST 1: ", str(list1))
print("LIST 2: ", str(list2))
print("REVERSE OF LIST 1: ", str(list1.reverse()))              #reverse of a list with one node
print("REVERSE OF LIST 2: ", str(list2.reverse()))              #reverse of a list with one node

list1.add_first(10)                                             #reverse of a list with 2 elements
print("ADDED 10 to LIST1")
list2.add_first(10)                                             #reverse of a list with 2 elements
print("ADDED 10 to LIST2")
print("LIST 1: ", str(list1))
print("LIST 2: ", str(list2))
print("REVERSE OF LIST 1: ", str(list1.reverse()))
print("REVERSE OF LIST 2: ", str(list2.reverse()))

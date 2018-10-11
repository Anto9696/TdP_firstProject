from my_list import CircularPositionalList

list1 = CircularPositionalList()
list2 = CircularPositionalList()



list1.add_last(-2)
print("ADDED -2 to LIST1 ")
list2.add_first(-2)
print("ADDED -2 to LIST2 ")


print("FOUND -2 - ", list1.find(-2).element() == -2)
print("FOUND -3 - ", list1.find(-3) == -3)

for i in range(10):
    list1.add_first(i)
    print("ADDED ",i," at the beginning of LIST1 ")
    list2.add_last(i + 11)
    print("ADDED ",i+11," at the end of LIST2 ")

print("LIST 1 - len ",len(list1))
print("LIST 1: ", str(list1))

print("LIST 2 - len ",len(list2))
print("LIST 2: ", str(list2))

list3 = list1 + list2
print("LIST 3 - len ",len(list3))
print("LIST 3: ", str(list3))

value=list3.add_before(list3.first(),-1)
print("ADDED  ",value.element()," before first of list3")
value=list3.add_before(list3.find(5),-100)
print("ADDED  ",value.element()," before 5 of list3")
value=list3.add_after(list3.last(),100)
print("ADDED  ",value.element()," after last of list3")
value=list3.add_after(list3.find(15),-100)
print("ADDED  ",value.element()," after 15 of list3")

print("AFTER INSERT LIST 3 - len ",len(list3))
print("LIST 3: ", str(list3))

print(list3.find(-100).element())
print(list3.find(-101010))

list1.clear()
print("List 1 cleared")
print("LIST 1: ", str(list1))

print("LIST 3: ", str(list3))
print(list3[list3.find(1)])
print(list3.find(1) in list3)
del list3[list3.find(1)]
print("LIST 3: ", str(list3))

list3.delete(list3.find(9))
print("DELETE 9 IN LIST 3")
print("LIST 3: ", str(list3))

list4 = CircularPositionalList()
print("LIST 4: ", str(list4))
print("REVERSE OF LIST 4: ", str(list4.reverse()))
list4.add_first(-2)
print("ADDED -2 to LIST4")
print("REVERSE OF LIST 4: ", str(list4.reverse()))
list4.add_first(10)
print("ADDED 10 to LIST4")
print("LIST 4: ", str(list4))
print("REVERSE OF LIST 4: ", str(list4.reverse()))
print("LIST 3: ", str(list3))
print("REVERSE OF LIST 3: ", list3.reverse())

print("REPLACE -100 WITH -500")
old_element = list3.replace(list3.find(-100), -500)
print("LIST 3: ", str(list3))
print("OLD ELEMENT: ", str(old_element))
print("REPLACE 27 (not exist) WITH -27")
try:
    old_element = list3.replace(list3.find(27), -27)
    print("LIST 3: ", str(list3))
    print("OLD ELEMENT: ", str(old_element))
except TypeError:
    print("ELEMENT DOES NOT EXSIST")

print("LIST 2: ", str(list2))
print("REPLACE 12 WITH -1000")
list2[list2.find(12)]= -1000
print("LIST 2: ", str(list2))













from my_list import MyList

list1 = MyList()
list2 = MyList()



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
cursor=list1._header
for e in list1:
    print("Value "+str(e))

print("LIST 2 - len ",len(list2))
for e in list2:
    print("Value "+str(e))

list3 = list1 + list2
print("LIST 3 - len ",len(list3))
for e in list3:
    print("Value "+str(e))

value=list3.add_before(list3.first(),-1)
print("ADDED  ",value.element()," before first of list3")
value=list3.add_before(list3.find(5),-100)
print("ADDED  ",value.element()," before 5 of list3")
value=list3.add_after(list3.last(),100)
print("ADDED  ",value.element()," after last of list3")
value=list3.add_after(list3.find(15),-100)
print("ADDED  ",value.element()," after 15 of list3")

print("AFTER INSERT LIST 3 - len ",len(list3))
for e in list3:
    print("Value "+str(e))

print(list3.find(-100).element())
print(list3.find(-101010))
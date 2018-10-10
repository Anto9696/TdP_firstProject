from my_list import MyList

list1 = MyList()
list2 = MyList()


list1.add_last(-2)
list2.add_first(-2)

print(list1.find(-2).element())
print(list1.find(-3))

for i in range(10):
    list1.add_first(i)
    list2.add_last(i + 11)

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
print("ADDED  ",value.element())
value=list3.add_before(list3.find(5),-100)
print("ADDED  ",value.element())
value=list3.add_after(list3.last(),100)
print("ADDED  ",value.element())
value=list3.add_after(list3.find(15),-100)
print("ADDED  ",value.element())

print("AFTER INSERT LIST 3 - len ",len(list3))
for e in list3:
    print("Value "+str(e))

print(list3.find(-100).element())
print(list3.find(-101010))
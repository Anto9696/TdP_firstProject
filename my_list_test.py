from my_list import MyList

list1 = MyList()
list2 = MyList()

position = list1.add_first(1)
print(position.element())
position = list1.add_first(2)
print(position.element())

for i in range(10):
    print("WRITING ",i)
    print(isinstance(list1._header,MyList._Node))
    list1.add_first(i)
    list2.add_last(i + 11)

print("LIST 1 - len ",len(list1))
cursor=list1._header
for i in range(len(list1)):
    print("Value"+str(cursor._element))
    cursor=cursor._next
print("LIST 2")
for e in list2:
    print("Value"+str(e))
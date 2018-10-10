from my_list import MyList

list1 = MyList()
list2 = MyList()

for i in range(10):
    list1.add_first(i)
    list2.add_last(i + 11)

print("LIST 1")
for e in list1:
    print(e)
print("LIST 2")
for e in list2:
    print(e)
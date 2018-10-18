from my_list import CircularPositionalList

def assert_copy(list1,list2):
    result = str(list1) == str(list2)
    if result:
        print("The lists are equal")
    else:
        print("The lists are not equal")
    return result

list1 = CircularPositionalList()

for i in range(10):
    list1.add_first(i)

list2 = list1.copy()

assert_copy(list1,list2)
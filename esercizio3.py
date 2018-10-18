from my_list_test import CircularPositionalList


def merge(list1, list2):
    """prende in input due CircularPositionalList ordinate e le fonde in una nuova CircularPositionalList ordinata"""
    if not isinstance(list1,CircularPositionalList) or not isinstance(list2,CircularPositionalList):
        raise TypeError("The operands are not CircularPositionalList")
    if not(list1.is_sorted() and list2.is_sorted()):
        raise ValueError("The lists are not sorted")
    current_first_list = list1.first()
    current_second_list = list2.first()
    i = e = 0
    new_list = CircularPositionalList()
    while i < len(list1) and e < len(list2):
        if current_first_list.element() > current_second_list.element():
            new_list.add_last(current_second_list.element())
            current_second_list = list2._next_position(current_second_list) # super(CircularPositionalList, list2).after(current_second_list)
            e += 1
        else:
            new_list.add_last(current_first_list.element())
            current_first_list = list1._next_position(current_first_list) # super(CircularPositionalList, list1).after(current_first_list)
            i += 1
    while i<len(list1):
        new_list.add_last(current_first_list.element())
        current_first_list = list1._next_position(current_first_list) # super(CircularPositionalList, list1).after(current_first_list)
        i += 1
    while e<len(list2):
        new_list.add_last(current_second_list.element())
        current_second_list = list2._next_position(current_second_list) # super(CircularPositionalList, list2).after(current_second_list)
        e += 1
    return new_list


if __name__=="__main__":
    list_1 = CircularPositionalList()
    list_2 = CircularPositionalList()
    for i in range(10):
        if i % 2 == 0:
            list_1.add_last(i)
        else:
            list_2.add_last(i)
    list_1.add_last(23)
    list_1.add_last(24)
    print("LIST 1")
    print(list_1)
    print("LIST 2")
    print(list_2)

    print("merge LIST ")
    new = merge(list_1,list_2)
    print(new)

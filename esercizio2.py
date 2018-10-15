from my_list import CircularPositionalList

def bubblesorted(list):
    """ordina gli elementi della CircularPositionalList e
    li restituisce nell’ordine risultante."""
    list_ordered=list.copy()
    sup = len(list_ordered) - 1
    while sup != 0:
        last_swap = 0
        cursor = list_ordered.first()
        succ_cursor = super(CircularPositionalList,list_ordered).after(cursor)
        for i in range(sup):
            if cursor.element() > succ_cursor.element():
                list_ordered.replace(succ_cursor,list_ordered.replace(cursor,succ_cursor.element()))
                last_swap = i
            cursor = succ_cursor
            succ_cursor = super(CircularPositionalList,list_ordered).after(cursor)
        sup=last_swap

    for element in list_ordered:
        yield element


if __name__=="__main__":
    list1 = CircularPositionalList()
    list2 = CircularPositionalList()
    for i in range(10):
        list1.add_first(i)
        list2.add_last(i+11)

    print("LIST 1")
    print(list1)
    print("LIST 2")
    print(list2)

    list3 = list1 + list2
    print("LIST 3")
    print(list3)

    print("ORDERED LIST 3")
    for e in bubblesorted(list3):
        print(e)

    print("LIST 3")
    print(list3)

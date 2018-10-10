from my_list import MyList

'''def bubblesorted(list):
    list_ordered=list
    sup=len(list)
    while sup!=0:
        last_swap = 0
        cursor=list_ordered.first()
        succ_cursor=list_ordered.after(cursor)
        for i in range(sup-1):
            if cursor.element() > succ_cursor.element():
                list_ordered.replace(succ_cursor,list_ordered.replace(cursor,succ_cursor.element()))
                last_swap = i
        sup=last_swap

    for element in list_ordered:
        yield element
        '''

def bubblesorted(list):
    ord_list=sorted(list)
    for i in ord_list:
        yield i

if __name__=="__main__":
    list1 = MyList()
    list2 = MyList()
    for i in range(10):
        list1.add_first(i)
        list2.add_last(i+11)

    print("LIST 1")
    for e in list1:
        print(e)
    print("LIST 2")
    for e in list2:
        print(e)

    list3 = list1 + list2
    print("LIST 3")
    for e in list3:
        print(e)

    print("ORDERED LIST 3")
    for e in bubblesorted(list3):
        print(e)

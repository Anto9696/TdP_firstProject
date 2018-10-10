from my_list import MyList

def merge(list1,list2):
    current_first_list=list1.first()._node
    current_second_list=list2.first()._node
    e=i=0
    while(i<list1.__len__() and e<list2.__len__() ):
        if(current_first_list._element>current_second_list._element):
            list1.add_before(list1._make_position(current_first_list),current_second_list._element)
            current_second_list=current_second_list._next
            e+=1
        else:
            current_first_list=current_first_list._next
            i+=1
    while (e<list2.__len__()):
        list1.add_last(current_second_list._element)
        current_second_list=current_second_list._next
        e+=1

if __name__=="__main__":
    list1 = MyList()
    list2 = MyList()
    for i in range(10):
        if(i%2==0):
            list1.add_last(i)
        else:
            list2.add_last(i)
    list1.add_last(23)
    list1.add_last(24)
    print("LIST 1")
    for e in list1:
        print(e)
    print("LIST 2")
    for e in list2:
        print(e)

    print("merge LIST ")
    merge(list1,list2)
    for e in list1:
        print(e)

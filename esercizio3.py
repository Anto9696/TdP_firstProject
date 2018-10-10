from my_list import MyList

class Merge(MyList):
    def merge(list1,list2):
        current_first_list=list1.first()
        current_second_list=list2.first()
        while(current_first_list is not None and current_second_list is not None ):
            if(current_first_list.element()>current_second_list.element()):
                list1.add_before(current_first_list,current_second_list.element())
                current_second_list.after()
            else:
                current_first_list.after()
        while (current_second_list is not None):
            list1.add_before(current_first_list,current_second_list.element())

from TdP_collections.list.positional_list import PositionalList

class MyList(PositionalList):

    def __init__(self):
        """Create an empty list."""
        self._header = None
        self._trailer = None
        self._size = 0

    def first(self):
        """restituisce la Position dell’elemento che è identificato come il primo oppure
        None se la lista è vuota"""
        return self._make_position(self._header)

    def last(self):
        """restituisce la Position dell’elemento che è identificato come l’ultimo oppure
        None se la lista è vuota"""
        return self._make_position(self._trailer)

    def _before(self,p): #restituisce il nodo
        node=self._validate(p)
        current_node=self._front
        i=0
        pre=None
        while (i<self.__len__())  and  (current_node._next!=node):
            i+=1
            current_node=current_node._next
            pre=current_node
        if(i==self.__len__()):
            raise ValueError
        else:
            return pre

    def before(self,p): #restituisce l'elemento
        var=self._before(p)
        if(var is None):
            return None
        else:
            return var._element

    def after(self,p):
        if(p._node.next is None):
            return None
        else:
            node=self._validate(p)
            return node.next._element

    def is_empty(self):
        """restituisce True se la lista è vuota e False altrimenti"""
        return self._size == 0
        # raise NotImplementedError("Not implemented")

    def is_sorted(self):
        """restituisce True se la lista è ordinata e False altrimenti"""
        current_node = self._validate(self.first())

        for i in range(self.__len__()):
            if current_node._element < current_node._next._element:
                current_node = current_node._next
            else:
                return False
        return True
        # raise NotImplementedError("Not implemented")

    def _insert_first_node(self,e):
        if self.is_empty():
            node = self._Node(e,None,None)
            node._prev = node
            node._next = node
            self._header = node
            self._trailer = node
            return node
        raise ValueError("The list is not empty")

    def add_first(self,e):
        if self.is_empty():
            node = self._insert_first_node(e)
        else:
            node = self._insert_between(e,self._trailer,self._header)
            self._header = node
        return self._make_position(node)

    def add_last(self,e):
        if self.is_empty():
            node = self._insert_first_node(e)
        else:
            node = self._insert_between(e,self._trailer,self._header)
            self._trailer = node
        return self._make_position(node)

    def add_before(self,p,e):
        node = super().add_before(p,e)
        if self._header == p._node:
            self._header = node
        return self._make_position(node)

    def add_after(self,p,e):
        node = super().add_after(p, e)
        if self._trailer == p._node:
            self._trailer = node
        return self._make_position(node)

    def find(self,e):
        """Restituisce una Position contenente la prima occorrenza dell’elemento e
        nella lista o None se e non è presente"""
        current_node = self._header
        while True:
            if current_node == e:
                return self._make_position(current_node)
            elif current_node == self._trailer:
                return None
        # raise NotImplementedError("Not implemented")

    def replace(self,p,e):
        raise NotImplementedError("Not implemented")

    def delete(self,p):
        """Rimuove e restituisce l’elemento in Position p dalla lista e invalida p"""
        remove_pos=self.find(p.element())
        if self.first() == remove_pos:  # if the position is header
            self.first()._node = self.first()._node._next
            self._size -= 1
            return remove_pos.element()
        elif remove_pos is None:        # if the position not exist
            print("Non-existent position")
            return None
        else:
            prev = self._validate(remove_pos._node._prev)
            next = self._validate(remove_pos._node._next)
            elem = remove_pos.element()
            prev._next = next
            next._prev = prev
            remove_pos._node._next = remove_pos._node._prev = remove_pos._node._element = None
            self._size -= 1
            return elem

        # FIRST VER
        # current_node=self._front
        # i=0
        # while (i<self.__len__() ):
        #     i+=1
        #     if( p==self._make_position(current_node._next)):
        #         var= current_node._next
        #         element=current_node._next._element
        #         current_node._next=current_node._next._next
        #         var=None
        #         return element
        #     current_node=current_node._next
        # return None




    def clear(self):
        raise NotImplementedError("Not implemented")

    def count(self,e):
        """Resituisce il numero di occorrenze di e nella Lista"""
        current_node = self._front
        counter = 0
        for i in range(self.__len__()):
            if current_node._element == e:
                counter += 1
            current_node = current_node._next
        return counter
        # raise NotImplementedError("Not implemented")

    def reverse(self):
        raise NotImplementedError("Not implemented")

    def copy(self):
        new=MyList()
        current_node=self._front
        i=0
        while (i<self.__len__()):
            i+=1
            new.add_last(current_node._element)
            current_node=current_node._next
        return new



    def __add__(self, other):
        if not isinstance(other,MyList):
            raise TypeError("Not a MyList")
        elif other.is_empty():
            return self.copy()
        elif self.is_empty():
            return other.copy()
        else:
            new_list = MyList()
            for element in self:
                new_list.add_last(element)
            for element in other:
                new_list.add_last(element)
            return new_list

    def __contains__(self, item):
        current_position = self.first()
        last_position = self.last()
        while current_position != last_position:
            if current_position == item:
                return True
            current_position = self._make_position(current_position._node._next)
        return False
        # raise NotImplementedError("Not implemented")

    def __getitem__(self, item):
        return item.element()
        #raise NotImplementedError("Not implemented")

    def __setitem__(self, key, value):
        raise NotImplementedError("Not implemented")

    def __len__(self):
        return self._size

    def __del__(self,p):
        self.delete(p)

    def __iter__(self):
        cursor = self._header
        while cursor is not self._trailer:
            yield cursor._element
            cursor = cursor._next

    def __str__(self):
        raise NotImplementedError("Not implemented")


if __name__=="__main__":
    d = MyList()
    d.append(5)
    d.append(7)
    d.append(8)
    d.show()
    # d.remove(7)
    # d.show()
    # d.append(6)
    # d.show()
    # d.reverse()
    # d.show()
    d.insert(1, 9)
    d.show()

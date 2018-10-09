from TdP_collections.list.positional_list import PositionalList

class MyList:
    class _Node:
        __slots__ = '_element', '_next'  # streamline memory

        def __init__(self, element, next):  # initialize node's fields
            self._element = element  # user's element
            self._next = next  # next node reference

    class Position(PositionalList.Position):
        pass

    __slots__ = '_size', '_front', '_back'
    def __init__(self):
        """Create an empty list."""
        self._front = None
        self._back = None
        self._size = 0

    def _validate(self,p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:  # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if sentinel)."""
        return self.Position(self, node)  # legitimate position

    def first(self):
        return self._make_position(self._first)

    def last(self):
        return self._make_position(self._back)

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
        raise NotImplementedError("Not implemented")

    def is_sorted(self):
        raise NotImplementedError("Not implemented")

    def add_first(self,e):
        raise NotImplementedError("Not implemented")

    def add_last(self,e):
        raise NotImplementedError("Not implemented")

    def add_before(self,p,e):
        raise NotImplementedError("Not implemented")

    def add_after(self,p,e):
        raise NotImplementedError("Not implemented")

    def find(self,e):
        raise NotImplementedError("Not implemented")

    def replace(self,p,e):
        raise NotImplementedError("Not implemented")

    def delete(self,p):
        current_node=self._front
        i=0
        while (i<self.__len__() ):
            i+=1
            if( p!=self._make_position(current_node._next)):
                var= current_node.next
                element=current_node._element
                current_node.next=current_node._next._next
                current_node._next=None
                return element
            current_node=current_node._next
        return None





    def clear(self):
        raise NotImplementedError("Not implemented")

    def count(self,e):
        raise NotImplementedError("Not implemented")

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
            self.add_last()
        return new



    def __add__(self, other):
        raise NotImplementedError("Not implemented")

    def __contains__(self, item):
        raise NotImplementedError("Not implemented")

    def __getitem__(self, item):
        raise NotImplementedError("Not implemented")

    def __setitem__(self, key, value):
        raise NotImplementedError("Not implemented")

    def __len__(self):
        return self._size

    def __del__(self,p):
        raise NotImplementedError("Not implemented")

    def __iter__(self):
        raise NotImplementedError("Not implemented")

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

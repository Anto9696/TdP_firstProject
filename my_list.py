from TdP_collections.list.positional_list import PositionalList

class MyList(PositionalList):

    def __init__(self):
        """Create an empty list."""
        self._header = None
        self._trailer = None
        self._size = 0

    def _make_position(self, node):
        """Return Position instance for given node (or None if sentinel)."""
        return self.Position(self, node)  # legitimate position

    def first(self):
        """restituisce la Position dell’elemento che è identificato come il primo oppure
        None se la lista è vuota"""
        return self._make_position(self._header)

    def last(self):
        """restituisce la Position dell’elemento che è identificato come l’ultimo oppure
        None se la lista è vuota"""
        return self._make_position(self._trailer)

    def before(self,p): #restituisce l'elemento
        var=super().before(p)
        return var.element() if var is not None else None

    def after(self,p):
        var=super().after(p)
        return var.element() if var is not None else None

    def is_sorted(self):
        """restituisce True se la lista è ordinata e False altrimenti"""
        current_node = self._header

        while current_node != self._trailer:
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
            self._size = self._size + 1
            return node
        raise ValueError("The list is not empty")

    def add_first(self,e):
        if self.is_empty():
            node = self._insert_first_node(e)
        else:
            node = super(PositionalList,self)._insert_between(e,self._trailer,self._header)
            self._header = node
        return self._make_position(node)

    def add_last(self,e):
        if self.is_empty():
            node = self._insert_first_node(e)
        else:
            node = super(PositionalList,self)._insert_between(e,self._trailer,self._header)
            self._trailer = node
        return self._make_position(node)

    def add_before(self,p,e):
        node = self._validate(p)
        new_node=super(PositionalList,self)._insert_between(e,node._prev,node)
        if self.first() == p:
            self._header = new_node
        return self._make_position(new_node)

    def add_after(self,p,e):
        node = self._validate(p)
        new_node = super(PositionalList, self)._insert_between(e, node, node._next)
        if self.last() == p:
            self._trailer = new_node
        return self._make_position(new_node)

    def find(self,e):
        """Restituisce una Position contenente la prima occorrenza dell’elemento e
        nella lista o None se e non è presente"""
        if self.is_empty():
            return None
        else:
            current_node = self._header
            while current_node != self._trailer and current_node._element != e:
                current_node = current_node._next
            return self._make_position(current_node) if current_node._element == e else None

    def replace(self,p,e):

        """Sostituisce l’elemento in Position p con e restituisce il vecchio elemento"""
        p = self._validate(p)
        old_elem = p._node._element
        p._node._element = e
        return old_elem


    def delete(self,p):
        """Rimuove e restituisce l’elemento in Position p dalla lista e invalida p"""
        remove_pos = self.find(p.element())
        if self.first() == remove_pos:  # if the position is header
            self.first()._node = self.first()._node._next
            self._size -= 1
            return remove_pos.element()
        elif remove_pos is None:        # if the position not exist
            print("Non-existent position")
            return None
        else:
            return super().delete(p)
            # prev = self._validate(remove_pos._node._prev)
            # next = self._validate(remove_pos._node._next)
            # elem = remove_pos.element()
            # prev._next = next
            # next._prev = prev
            # remove_pos._node._next = remove_pos._node._prev = remove_pos._node._element = None
            # self._size -= 1
            # return elem

    def clear(self):
        """Rimuove tutti gli elementi della lista invalidando le corrispondenti Position"""
        if not self.is_empty():
            cursor = self._header
            while cursor != self._trailer:
                next = cursor._next
                cursor._next = None         #invalidation of a node
                cursor = next
            self._header = None
            self._trailer = None
            self._size = 0

    def count(self,e):
        """Resituisce il numero di occorrenze di e nella Lista"""
        if not self.is_empty():
            current_node = self._header
            counter = 0
            while current_node != self._trailer:
                if current_node._element == e:
                    counter += 1
                current_node = current_node._next
            return counter
        # raise NotImplementedError("Not implemented")

    def reverse(self):
        """Inverte l’ordine degli elementi nella lista"""
        if len(self) <= 1:
            return self
        tmp = self._header
        for i in range(len(self)):
            old_prev = tmp._node._prev
            tmp._node._prev = tmp._node._next
            tmp._node._next = old_prev
        return self


    def copy(self):
        new=MyList()
        current_node=self._trailer
        i=0
        while i<self._size:
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
        self._validate(item)
        current_position = self.first()
        last_position = self.last()
        while current_position != last_position:
            if current_position == item:
                return True
            current_position = self._make_position(current_position._node._next)
        return False

    def __getitem__(self, item):
        self._validate(item)
        return item.element()

    def __setitem__(self, key, value):
        """Sostituisce l’elemento nella position p con e"""
        self.replace(p, e)

    def __delitem__(self,p):
        self.delete(p)

    def __iter__(self):
        """Iterator della classe"""
        if not self.is_empty():
            cursor = self._header
            yield cursor._element
            while cursor != self._trailer:
                cursor = cursor._next
                yield cursor._element


    def __str__(self):
        """Rappresenta il contenuto della lista come una sequenza di elementi,
        separati da virgole, partendo da quello che è identificato come primo"""
        str = ""
        for elem in self:
            str += str(elem) + ", "
        return str[:-2]


# if __name__=="__main__":
#     d = MyList()
#     d.append(5)
#     d.append(7)
#     d.append(8)
#     d.show()
#     # d.remove(7)
#     # d.show()
#     # d.append(6)
#     # d.show()
#     # d.reverse()
#     # d.show()
#     d.insert(1, 9)
#     d.show()

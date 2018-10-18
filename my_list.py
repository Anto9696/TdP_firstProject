from TdP_collections.list.positional_list import PositionalList


class CircularPositionalList(PositionalList):

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
        return self._make_position(self._header) if self._header is not None else None

    def last(self):
        """restituisce la Position dell’elemento che è identificato come l’ultimo oppure
        None se la lista è vuota"""
        return self._make_position(self._trailer) if self._trailer is not None else None

    def _prev_position(self, p):
        """punta alla position precedente a p"""
        return super().before(p)

    def _next_position(self, p):
        """punta alla position successiva a p"""
        return super().after(p)

    def before(self, p):
        """punta all'elemento precedente alla position p altrimenti restituisce None"""
        var = self._prev_position(p)
        return var.element() if len(self) > 1 else None

    def after(self, p):
        """punta all'elemento successivo alla position p altrimenti restituisce None"""
        var = self._next_position(p)
        return var.element() if len(self) > 1 else None

    def is_sorted(self):
        """restituisce True se la lista è ordinata e False altrimenti"""
        current_node = self.first()
        while current_node != self.last() and current_node.element() < self._next_position(current_node).element():
            current_node = self._next_position(current_node)
        return True if current_node == self.last() else False

    def _insert_first_node(self, e):
        """inserisce il primo nodo con elemento e"""
        if self.is_empty():
            node = self._Node(e, None, None)
            node._prev = node
            node._next = node
            self._header = node
            self._trailer = node
            self._size = self._size + 1
            return self._make_position(node)
        raise ValueError("The list is not empty")

    def add_first(self, e):
        """Inserisce l’elemento e in testa alla lista e restituisce la Position del nuovo
        elemento"""
        if self.is_empty():
            node = self._insert_first_node(e)
        else:
            node = super()._insert_between(e, self._trailer, self._header)._node #super(PositionalList, self)._insert_between(e, self._trailer, self._header) #super call brutta
            self._header = node
        return self._make_position(node)

    def add_last(self, e):
        """Inserisce l’elemento e in coda alla lista e restituisce la Position del nuovo
        elemento"""
        if self.is_empty():
            node = self._insert_first_node(e)
        else:
            node = super()._insert_between(e, self._trailer, self._header)._node #super(PositionalList, self)._insert_between(e, self._trailer, self._header) #super call brutta
            self._trailer = node
        return self._make_position(node)

    def add_before(self, p, e):
        """Inserisce un nuovo elemento e prima del nodo nella Position p e restituisce la
        Position del nuovo elemento"""
        node = self._validate(p)
        new_position = super()._insert_between(e, node._prev, node)#super(PositionalList, self)._insert_between(e, node._prev, node)  # Non so come sostituire, super call brutta
        if self.first() == p:
            self._header = new_position._node
        return new_position

    def add_after(self, p, e):
        """Inserisce un nuovo elemento e dopo il nodo nella Position p e restituisce la
        Position del nuovo elemento"""
        node = self._validate(p)
        new_position = super()._insert_between(e, node, node._next)  # Uguale e sopra
        if self.last() == p:
            self._trailer = new_position._node
        return new_position

    def find(self, e):
        """Restituisce una Position contenente la prima occorrenza dell’elemento e
        nella lista o None se e non è presente"""
        if self.is_empty():
            return None
        else:
            current_position = self.first()
            while current_position != self.last() and current_position.element() != e:
                current_position = self._next_position(current_position)
            return current_position if current_position.element() == e else None

    def delete(self, p):
        """Rimuove e restituisce l’elemento in Position p dalla lista e invalida p"""
        node = self._validate(p)
        if len(self) == 1:
            element = node._element
            node._element = node._prev = node._next = None      #Nodo Invalidato
            self._size = 0
            self._header = None
            self._trailer = None
        else:
            element = super()._delete_node(node)
            if self.first() == p:
                self._header = self._header._next
            elif self.last() == p:
                self._trailer = self._trailer._prev
        return element

    def clear(self):
        """Rimuove tutti gli elementi della lista invalidando le corrispondenti Position"""
        if not self.is_empty():
            cursor = self.first()
            while not self.is_empty():
                next_cur = self._next_position(cursor)
                self.delete(cursor)
                cursor = next_cur

    def count(self, e):
        """Restituisce il numero di occorrenze di e nella Lista"""
        counter = 0
        for element in self:
            if element == e:
                counter += 1
        return counter

    def reverse(self):
        """Inverte l’ordine degli elementi nella lista"""
        if len(self) <= 1:
            return self
        tmp = self._header
        old_header = self._header
        self._header = self._trailer
        for i in range(len(self)):
            old_prev = tmp._prev
            tmp._prev = tmp._next
            tmp._next = old_prev
            tmp = tmp._next
        self._header = self._trailer
        self._trailer = old_header
        return self

    def copy(self):
        """Restituisce una nuova CircularPositionalList che contiene gli stessi elementi
        della lista corrente memorizzati nello stesso ordine"""
        new = CircularPositionalList()
        for element in self:
            new.add_last(element)
        return new

    def __add__(self, other):
        """Crea una lista con tutti gli elementi di self e tutti gli elementi di other inseriti dopo
        l’ultimo elemento di self"""
        if not isinstance(other, CircularPositionalList):
            raise TypeError("Operand is not a CircularPositionalList")
        elif other.is_empty():
            return self.copy()
        elif self.is_empty():
            return other.copy()
        else:
            new_list = CircularPositionalList()
            for element in self:
                new_list.add_last(element)
            for element in other:
                new_list.add_last(element)
            return new_list

    def __contains__(self, item):
        """restituisce True se item è presente nella lista e False altrimenti"""
        self._validate(item)  #Se è una posizione validata..c'è nella lista
        current_position = self.first()
        for i in range(len(self)):
            if current_position == item:
                return True
            current_position = self._next_position(current_position)
        return False

    def __getitem__(self, item):
        """Restituisce l’elemento contenuto nella position item"""
        self._validate(item)
        return item.element()

    def __setitem__(self, p, e):
        """Sostituisce l’elemento nella position p con e"""
        self.replace(p, e)          # in replace viene validata già la position

    def __delitem__(self, p):
        """Rimuove l’elemento nella position p invalidando la position"""
        self.delete(p)              # il validate è in delete

    def __iter__(self):
        """Iterator della classe"""
        if not self.is_empty():
            cursor = self.first()
            yield cursor.element()
            while cursor != self.last():
                cursor = self._next_position(cursor)
                yield cursor.element()

    def __str__(self):
        """Rappresenta il contenuto della lista come una sequenza di elementi,
        separati da virgole, partendo da quello che è identificato come primo"""
        string = ""
        for el in self:
            string += str(el) + ", "
        return string[:-2]

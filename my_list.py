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

    def _prev_position(self, p):  # pubblici sarebbero più utili
        return super().before(p)

    def _next_position(self, p):  # pubblici sarebbero più utili
        return super().after(p)

    def before(self, p):
        var = self._prev_position(p)
        return var.element() if var is not None else None

    def after(self, p):
        var = self._next_position(p)
        return var.element() if var is not None else None

    def is_sorted(self):
        """restituisce True se la lista è ordinata e False altrimenti"""
        current_node = self.first()
        while current_node != self.last() and current_node.element() < self._next_position(current_node).element():
            current_node = self._next_position(current_node)
        return True if current_node == self.last() else False

    def _insert_first_node(self, e):
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
            node = super(PositionalList, self)._insert_between(e, self._trailer, self._header)
            self._header = node
        return self._make_position(node)

    def add_last(self, e):
        """Inserisce l’elemento e in coda alla lista e restituisce la Position del nuovo
        elemento"""
        if self.is_empty():
            node = self._insert_first_node(e)
        else:
            node = super(PositionalList, self)._insert_between(e, self._trailer, self._header)
            self._trailer = node
        return self._make_position(node)

    def add_before(self, p, e):
        """Inserisce un nuovo elemento e prima del nodo nella Position p e restituisce la
        Position del nuovo elemento"""
        node = self._validate(p)
        new_node = super(PositionalList, self)._insert_between(e, node._prev, node)  # Non so come sostituire
        if self.first() == p:
            self._header = new_node
        return self._make_position(new_node)

    def add_after(self, p, e):
        """Inserisce un nuovo elemento e dopo il nodo nella Position p e restituisce la
        Position del nuovo elemento"""
        node = self._validate(p)
        new_node = super(PositionalList, self)._insert_between(e, node, node._next)  # Non so come sostituire
        if self.last() == p:
            self._trailer = new_node
        return self._make_position(new_node)

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

    def delete(self, p):  # forse si può non cercare
        """Rimuove e restituisce l’elemento in Position p dalla lista e invalida p"""
        self._validate(p)
        remove_pos = self.find(p.element())
        if remove_pos is None:
            raise ValueError("Non-existent position")
        else:
            if self.first() == remove_pos:  # if the position is header
                self._header = self._validate(self._next_position(self.first()))
            elif self.last() == remove_pos:
                self._trailer = self._validate(self._prev_position(self.last()))
            return super().delete(p)

    def clear(self):
        """Rimuove tutti gli elementi della lista invalidando le corrispondenti Position"""
        if not self.is_empty():
            cursor = self.first()
            while not self.is_empty():
                next_cur = self._next_position(cursor)
                self.delete(cursor)
                cursor = next_cur
            self._header = None
            self._trailer = None

    def count(self, e):
        """Resituisce il numero di occorrenze di e nella Lista"""
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

    def __contains__(self, item):  # Se c'è solo 1 elemento??
        self._validate(item)
        current_position = self.first()
        # last_position = self.last()
        for i in range(len(self)):
            if current_position == item:
                return True
            current_position = self._next_position(current_position)
        return False
        # while current_position != last_position:
        #     if current_position == item:
        #         return True
        #     current_position = self._next_position(current_position)
        # return False

    def __getitem__(self, item):  # controllare se validare == ci sta
        self._validate(item)
        return item.element()

    def __setitem__(self, p, e):
        """Sostituisce l’elemento nella position p con e"""
        self.replace(p, e)  # in replace viene validata già la position

    def __delitem__(self, p):
        self.delete(p)

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

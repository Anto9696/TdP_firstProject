from TdP_collections.list.positional_list import PositionalList


class CircularPositionalList(PositionalList):

    def __init__(self):
        """Create an empty list."""
        self._header = None
        self._trailer = None
        self._reverse = False       # quando è a False la lista scorre normalmente, altrimenti viene letta al contrario -> REVERSE in O(1)
        self._size = 0

    def _make_position(self, node):
        """Return Position instance for given node"""
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
        return super().before(p) if not self._reverse else super().after(p)  # se il flag della reverse è attivo allora il before sarà un after

    def _next_position(self, p):
        """punta alla position successiva a p"""
        return super().after(p) if not self._reverse else super().before(p)  # se il flag della reverse è attivo allora l'after sarà un before

    def before(self, p):
        """punta all'elemento precedente alla position p altrimenti restituisce None"""
        var = self._prev_position(p)
        return var.element() if len(self) > 1 else None      # perchè se c'è un solo elemento, il predecessore di questo non deve essere se stesso, dato che essendo una lista doppiamente linkata con un solo elemento il prev punterebbe a se stesso

    def after(self, p):
        """punta all'elemento successivo alla position p altrimenti restituisce None"""
        var = self._next_position(p)
        return var.element() if len(self) > 1 else None      # perchè se c'è un solo elemento, il successore di questo non deve essere se stesso, dato che essendo una lista doppiamente linkata con un solo elemento il next punterebbe a se stesso

    # LA FUNZIONE is_empty la eredita da doubly_linked_base

    def is_sorted(self):
        """restituisce True se la lista è ordinata e False altrimenti"""
        current_node = self.first()
        while current_node != self.last() and current_node.element() <= self._next_position(current_node).element():
            current_node = self._next_position(current_node)
        return True if current_node == self.last() else False

    def _insert_first_node(self, e):
        """inserisce il primo nodo con elemento e"""  # viene usato per inserire il primo nodo quando la lista è vuota
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
            if not self._reverse:
                node = super()._insert_between(e, self._trailer, self._header)._node    # "._node" perchè restituisce una position ma del tipo positional_list
            else:                                                                       # distinguiamo qui tra i 2 casi perchè si utilizza la insert_between di doubly_linked_base e
                node = super()._insert_between(e, self._header, self._trailer)._node    # questa utilizza i puntatori _next e _prev, quindi per condizionarne il comporrtamento scambiamo
            self._header = node                                                         # predecessore e successore passatogli
        return self._make_position(node)

    def add_last(self, e):
        """Inserisce l’elemento e in coda alla lista e restituisce la Position del nuovo
        elemento"""
        if self.is_empty():
            node = self._insert_first_node(e)
        else:
            if not self._reverse:
                node = super()._insert_between(e, self._trailer, self._header)._node   #distinguiamo qui tra i 2 casi perchè si utilizza la insert_between di doubly_linked_base e
            else:                                                                      #questa utilizza i puntatori _next e _prev, quindi per condizionarne il comporrtamento scambiamo
                node = super()._insert_between(e, self._header, self._trailer)._node   #predecessore e successore passatogli
            self._trailer = node
        return self._make_position(node)

    def __add_before(self, p, e):
        """Inserisce un nuovo elemento e prima del nodo nella Position p e restituisce la
        Position del nuovo elemento"""
        node = self._validate(p)
        new_position = super()._insert_between(e, node._prev, node)
        if not self._reverse and self.first() == p:     # se la lista non è invertita e aggiungo prima del primo allora aggiorno l'header
            self._header = new_position._node
        elif self._reverse and self.last() == p:        # se la lista è invertita la _add_before viene chiamata dalla add_after pubblica per inserire dopo l'elemento scelto, se questo è l'ultimo allora
            self._trailer = new_position._node          # l'elemento scelto sarà il nuovo ultimo
        return new_position

    def __add_after(self, p, e):
        """Inserisce un nuovo elemento e dopo il nodo nella Position p e restituisce la
        Position del nuovo elemento"""
        node = self._validate(p)
        new_position = super()._insert_between(e, node, node._next)
        if not self._reverse and self.last() == p:     # se la lista non è invertita e aggiungo dopo l'ultimo allora aggiorno trailer
            self._trailer = new_position._node
        elif self._reverse and self.first() == p:      # se la lista è invertita la _add_after viene richiamata dalla add_bedore pubblica per inserire prima dell'elemento scelto, se inserisco prima del
            self._header = new_position._node          # primo allora aggiorno l'header
        return new_position

    def add_before(self, p, e):
        """richiama _add_before se il flag di reverse non è attivo, altrimenti __add_after"""
        if not self._reverse:
            return self.__add_before(p, e)
        else:
            return self.__add_after(p, e)

    def add_after(self, p, e):
        """richiama __add_after se il flag di reverse non è attivo, altrimenti __add_after"""
        if not self._reverse:
            return self.__add_after(p, e)
        else:
            return self.__add_before(p, e)

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
            node._element = node._prev = node._next = None  # Nodo Invalidato
            self._size = 0
            self._header = None
            self._trailer = None
            self._reverse = False
        else:
            if self.first() == p:
                self._header = self._header._next if not self._reverse else self._header._prev
            elif self.last() == p:
                self._trailer = self._trailer._prev if not self._reverse else self._trailer._next
            element = super()._delete_node(node)
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
        self._reverse = not self._reverse  # impostiamo il flag per far invertire il funzionamento di _prev_position e _next_position
        tmp = self._header  # e invertiamo header e trailer
        self._header = self._trailer
        self._trailer = tmp

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
        """restituisce True se item è una position presente nella lista e False altrimenti"""
        try:
            self._validate(item)  # se il validate non restituisce nessuna eccezione allora la posizione esiste ed è presente
            return True
        except:
            return False

    def __getitem__(self, item):
        """Restituisce l’elemento contenuto nella position item"""
        self._validate(item)
        return item.element()

    def __setitem__(self, p, e):
        """Sostituisce l’elemento nella position p con e"""
        self.replace(p, e)  # La position viene valtata in replace

    def __delitem__(self, p):
        """Rimuove l’elemento nella position p invalidando la position"""
        self.delete(p)  # il validate è in delete

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

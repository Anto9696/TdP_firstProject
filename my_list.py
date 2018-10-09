class MyList:
    class _Node:
        __slots__ = '_element', '_prev', '_next'  # streamline memory

        def __init__(self, element, prev, next):  # initialize node's fields
            self._element = element  # user's element
            self._prev = prev  # previous node reference
            self._next = next  # next node reference

    __slots__ = '_size', '_header', '_trailer'

    def __init__(self):
        """Create an empty list."""
        self._header = None
        self._trailer = None
        # self._header._next = self._trailer                  # trailer is after header
        # self._trailer._prev = self._header                  # header is before trailer
        self._size = 0  # number of elements

    def __add__(self, add):
        raise NotImplementedError("Not implemented")

    def __iadd__(self, add):
        raise NotImplementedError("Not implemented")

    def __le__(self, other):
        return self < other or self == other

    def __eq__(self, other):
        raise NotImplementedError("Not implemented")

    def __ne__(self, other):
        return not self == other

    def __ge__(self, other):
        return self == other or self > other

    def __gt__(self, other):
        raise NotImplementedError("Not implemented")

    def __lt__(self, other):
        raise NotImplementedError("Not implemented")

    def __contains__(self, item):
        raise NotImplementedError("Not implemented")

    def __setitem__(self, key, value):
        if key >= len(self):
            raise IndexError
        current = self._header
        for x in range(key):
            current = current._next
        current._element = value

    def __getitem__(self, item):
        if item >= len(self):
            raise IndexError
        current = self._header
        for x in range(item):
            current = current._next
        return current._element

    def __delitem__(self, item):
        raise NotImplementedError("Not implemented")

    def __del__(self):
        raise NotImplementedError("Not implemented")

    def __str__(self):
        raise NotImplementedError("Not implemented")

    def __bool__(self):
        raise NotImplementedError("Not implemented")

    def __len__(self):
        return self._size

    def append(self, x):
        new_node = self._Node(x, None, None)
        if self._header is None:
            self._header = self._trailer = new_node
        else:
            new_node._prev = self._trailer
            new_node._next = None
            self._trailer._next = new_node
            self._trailer = new_node
        self._size += 1

    def extend(self, iterable):
        for x in iterable:
            self.append(x)
            next(iterable)
            self._trailer = x
        # raise NotImplementedError("Not implemented")

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = self._Node(e, predecessor, successor)  # linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def insert(self, i, x):
        new_node = self._Node(x, None, None)
        if self._header is None:
            self._header = self._trailer = new_node
        else:
            current_node = self._header
            count = 0
            while current_node is not None and count < i - 1:
                current_node = current_node._next
                count = count + 1
            self._insert_between(x, current_node, current_node._next)

    def remove(self, x):
        current_node = self._header
        if current_node == x:
            self._header = current_node._next
            current_node._next._prev = None
            self._size -= 1
        else:
            while current_node is not None:
                if current_node._element == x:
                    current_node._prev._next = current_node._next
                    current_node._next._prev = current_node._prev
                    self._size -= 1

                current_node = current_node._next

    def pop(self, i=None):
        raise NotImplementedError("Not implemented")

    def clear(self):
        raise NotImplementedError("Not implemented")

    def index(self, x, start=0, end=None):
        raise NotImplementedError("Not implemented")

    def count(self, x):
        count = 0
        for i in range(len(self._size)):
            if self[i] == x:
                count += 1
        return count

    def sort(key=None, reverse=False):
        raise NotImplementedError("Not implemented")

    def reverse(self):
        current_node = self._header
        while current_node is not None:
            var = current_node._prev
            current_node._prev = current_node._next
            current_node._next = var
            current_node = current_node._prev

        var = self._header
        self._header = self._trailer
        self._trailer = var

    def copy(self):
        raise NotImplementedError("Not implemented")

    def show(self):
        """This is not a method of project"""
        print("List data is: ")
        current_node = self._header
        while current_node is not None:
            print(current_node._prev._element if hasattr(current_node._prev, "_element") else None)
            print(current_node._element)
            print(current_node._next._element if hasattr(current_node._next, "_element") else None)
            print()

            current_node = current_node._next
        print("*" * 50)


if __name__ == "__main__":
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

from my_list import MyList



class ScoreBoard:
    class Score:
        def __init__(self):
            self._player = None
            self._score = 0
            self._date = "00/00/0000"

    def __init__(self,x):
        self._best = MyList()
        self._max = x
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def insert(self, s):
        raise NotImplementedError("Not implemented")

    def merge(self,new):
        raise NotImplementedError("Not implemented")

    def top(self,i):
        raise NotImplementedError("Not implemented")

    def last(self,i):
        raise NotImplementedError("Not implemented")

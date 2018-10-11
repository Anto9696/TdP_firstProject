from my_list import MyList
from esercizio2 import bubblesorted
from esercizio3 import merge


class Score:
    def __init__(self):
        self._player = None
        self._score = 0
        self._date = "00/00/0000"

    def add_element(self, pl, sc, da):
        self._player = pl
        self._score = sc
        self._date = da


class ScoreBoard:

    def __init__(self, x):
        self._best = MyList()
        self._max = x
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def insert(self, s):
        """Inserisce un nuovo score nello scoreboard se e solo se non è peggiore dei risultati
        correntemente salvati. Non incrementa la dimensione dello scoreboard"""
        if len(self) < self._max:
            score = self._best._header
            if score is None:
                self._best.add_last(s)
                self._size += 1
            else:
                i = 0
                for i in range(len(self._best)):
                    # print(s._score, score._element._score)
                    i +=1
                    if s._score < score._element._score:
                        raise TypeError("Too bad score")
                    score = score._next
                self._best.add_last(s)
                self._size += 1
        # raise NotImplementedError("Not implemented")

    def merge(self, new):
        """Fonde lo scoreboard corrente con new selezionando i 10 migliori risultati"""
        lis = merge(self._best, new)
        return lis.top(10)
        # raise NotImplementedError("Not implemented")

    def top(self, i):
        """Restituisce i migliori i score nello ScoreBoard"""
        imp = len(self._best) - i
        cur = self._best._header
        lis = MyList()
        for p in range(len(self._best)):
            lis.add_last(cur._element._score)
            cur = cur._next
        counter = 0
        for el in bubblesorted(lis):
            if counter >= imp:
                yield el
            counter += 1
        # raise NotImplementedError("Not implemented")

    def last(self, i):
        """Restituisce i peggiori i score nello ScoreBoard"""
        raise NotImplementedError("Not implemented")


if __name__ == "__main__":
    score1 = Score()
    score2 = Score()
    score3 = Score()
    score1.add_element("Gino", 10, "15/10/2017")
    # print(score1._player, " ", score1._score, " ", score1._date)
    score2.add_element("AAA", 5, "15/10/2017")
    score3.add_element("BBB", 15, "15/10/2017")

    SB = ScoreBoard(4)
    print(SB.is_empty()) # verifico is_empty
    print(len(SB))
    SB.insert(score1)
    print(SB.is_empty()) # verifico is_empty
    print(len(SB))
    SB.insert(score3)
    print(len(SB))
    # print(SB._max)
    SB2 = ScoreBoard(1)
    SB2.insert(score3)
    #print(SB2._best._header._element._score)

    for e in SB.top(2):
        print(e)

from my_list import CircularPositionalList
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

    def give_score(self):
        return self._score


class ScoreBoard:

    def __init__(self, x):
        self._best = CircularPositionalList()
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
            #   QUA AGGIUNGO SOLO SE è MIGLIORE DEGLI ALTRI E SE NON HA RAGGIUNTO IL LIMITE MASSIMO

            #   E CI SONO ANCORA I PRIVATI
            # score = self._best._header
            # if score is None:
            #     self._best.add_last(s)
            #     self._size += 1
            # else:
            #     for i in range(len(self._best)):
            #         # print(s.give_score(), score._element.give_score())
            #         if s.give_score() < score._element.give_score():
            #             raise TypeError("Too bad score")
            #         score = score._next
            #     self._best.add_last(s)
            #     self._size += 1

            #   QUA AGGIUNGE FINCHè NON RAGGIUNGE IL LIMITE MASSIMO, POI AGGIUNGE SE MIGLIORE DEI PRESENTI IN TESTA ELIMINADO IL PRIMO
            self._best.add_last(s)
            self._size += 1
        else:
            scores = self._best.first()
            for i in range(len(self._best)):
                if s.give_score() < scores.element().give_score():
                        raise TypeError("Too bad score")
                scores = super(CircularPositionalList, scores).after(scores) #  NON RIESCO A FARLO AVANZARE
            first_score = self._best.first()
            del first_score
            self._best.add_first(s)
        # raise NotImplementedError("Not implemented")

    def merge(self, new):
        """Fonde lo scoreboard corrente con new selezionando i 10 migliori risultati"""
        lis = merge(self._best, new)    # NON VA PERCHè NON SONO CURRENTPOSITIONAL LIST
        return lis.top(10)

    def top(self, i):
        """Restituisce i migliori i score nello ScoreBoard"""
        imp = len(self._best) - i
        cur = self._best._header
        lis = CircularPositionalList()
        for p in range(len(self._best)):
            lis.add_last(cur._element.give_score())
            cur = cur._next
        counter = 0
        for el in bubblesorted(lis):
            if counter >= imp:
                yield el
            counter += 1

    def last(self, i):
        """Restituisce i peggiori i score nello ScoreBoard"""
        cur = self._best._header
        lis = CircularPositionalList()
        for p in range(len(self._best)):
            lis.add_last(cur._element.give_score())
            cur = cur._next
        counter = 0
        for el in bubblesorted(lis):
            if counter < i:
                yield el
            else:
                break
            counter += 1


if __name__ == "__main__":
    score1 = Score()
    score2 = Score()
    score3 = Score()
    score4 = Score()
    score5 = Score()

    score1.add_element("Gino", 10, "15/10/2017")
    # print(score1._player, " ", score1._score, " ", score1._date)
    score2.add_element("AAA", 5, "15/10/2017")
    score3.add_element("BBB", 15, "15/10/2017")
    score4.add_element("CCC", 1, "15/10/2017")
    score5.add_element("DDD", 21, "15/10/2017")

    SB1 = ScoreBoard(4)
    # print("SCOREBOARD DIMENSION: ", SB._max)
    print("EMPTY SCOREBOARD 1: ", SB1.is_empty())
    print("LENGTH OF SCOREBOARD 1: ", len(SB1))
    print("INSERT SCORE")
    SB1.insert(score1)
    print("EMPTY SCOREBOARD 1: ", SB1.is_empty())
    print("LENGTH OF SCOREBOARD 1: ", len(SB1))
    print("INSERT SCORE IN SCOREBOARD 1")
    SB1.insert(score3)
    print("LENGTH OF SCOREBOARD 1: ", len(SB1))

    print("INSERT SCORE IN SCOREBOARD 2")
    SB2 = ScoreBoard(4)
    SB2.insert(score3)
    SB2.insert(score4)
    SB2.insert(score5)
    # print(SB2._best._header._next._element.give_score())
    print("LENGTH OF SCOREBOARD 2: ", len(SB2))

    print("TOPs 1")
    for e in SB1.top(1):
        print(e)

    print("LASTs 1")
    for e in SB1.last(1):
        print(e)

    print("LENGTH OF SCOREBOARD 1: ", len(SB1))
    print("ADD ELEMENTS: ", len(SB1))
    SB1.insert(score2)
    SB1.insert(score4)
    print("NEW LENGTH OF SCOREBOARD 1: ", len(SB1))
    print("ADD ONE MORE ELEMENT: ", len(SB1))
    SB1.insert(score5)

    # print("MERGE SB1 & SB2")
    # for e in merge(SB1, SB2):
    #     print(e)

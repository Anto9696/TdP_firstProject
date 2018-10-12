from my_list import CircularPositionalList
from esercizio2 import bubblesorted
# from esercizio3 import merge


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
            #   QUA AGGIUNGE FINCHè NON RAGGIUNGE IL LIMITE MASSIMO, POI AGGIUNGE SE MIGLIORE DEI PRESENTI, IN TESTA, ELIMINADO IL PRIMO
            self._best.add_last(s)
            self._size += 1
        else:
            scores = self._best.first()
            min = scores.element().give_score()
            for i in range(len(self._best)):
                if min > scores.element().give_score(): # ricerco il minimo da confrontare
                    min = scores.element().give_score()
                scores = super(CircularPositionalList, self._best).after(scores)
            if s.give_score() < min: # se il nuovo score è minore del minimo non va aggiunto
                raise TypeError("Too bad score")
            self._best.add_first(s)
            self._best.delete(self._best.last())  # delete(super(CircularPositionalList, self._best).after(self._best.first()))
            #   QUA AGGIUNGO SOLO SE è MIGLIORE DEGLI ALTRI E SE NON HA RAGGIUNTO IL LIMITE MASSIMO
            #   E CI SONO ANCORA I PRIVATI
            # if len(self) < self._max:
            #   score = self._best._header
            #   if score is None:
            #       self._best.add_last(s)
            #       self._size += 1
            #   else:
            #       for i in range(len(self._best)):
            #           # print(s.give_score(), score._element.give_score())
            #           if s.give_score() < score._element.give_score():
            #               raise TypeError("Too bad score")
            #           score = score._next
            #       self._best.add_last(s)
            #       self._size += 1

    def merge(self, new):
        """Fonde lo scoreboard corrente con new selezionando i 10 migliori risultati"""
        # lis = merge(self._best, new)    # NON VA PERCHè NON SONO CircularPositionalList
        if not isinstance(self, ScoreBoard) or not isinstance(new, ScoreBoard):
            raise TypeError("The operands are not CircularPositionalList")
        second_board = new._best.first()
        lis = self._best.copy()
        new_board = ScoreBoard(1)
        i = 0
        while i < len(new._best):
            lis.add_last(second_board.element())
            second_board = super(CircularPositionalList, new._best).after(second_board)
            i += 1
        new_board._best = lis
        new_board._size = new_board._max = len(lis)
        return new_board.top(10)

    def top(self, i):
        """Restituisce i migliori i score nello ScoreBoard"""
        imp = len(self._best) - i
        cur = self._best.first()
        lis = CircularPositionalList()
        for p in range(len(self._best)):
            lis.add_last(cur.element().give_score())
            cur = super(CircularPositionalList, self._best).after(cur)
        counter = 0
        for el in bubblesorted(lis):
            if counter >= imp:
                yield el
            counter += 1

    def last(self, i):
        """Restituisce i peggiori i score nello ScoreBoard"""
        cur = self._best.first()
        lis = CircularPositionalList()
        for p in range(len(self._best)):
            lis.add_last(cur.element().give_score())
            cur = super(CircularPositionalList, self._best).after(cur)
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
    score6 = Score()
    score7 = Score()
    score8 = Score()
    score9 = Score()
    score10 = Score()

    score1.add_element("AAA", 10, "15/10/2017")
    # print(score1._player, " ", score1._score, " ", score1._date)
    score2.add_element("BBB", 5, "15/10/2017")
    score3.add_element("CCC", 15, "15/10/2017")
    score4.add_element("DDD", 7, "15/10/2017")
    score5.add_element("EEE", 21, "15/10/2017")
    score6.add_element("EEE", 1, "15/10/2017")
    score7.add_element("EEE", 56, "15/10/2017")
    score8.add_element("EEE", -4, "15/10/2017")
    score9.add_element("EEE", 18, "15/10/2017")
    score10.add_element("EEE", 8, "15/10/2017")

    SB1 = ScoreBoard(4)
    # print("SCOREBOARD DIMENSION: ", SB._max)
    print("EMPTY SCOREBOARD 1: ", SB1.is_empty())
    print("LENGTH OF SCOREBOARD 1: ", len(SB1))
    print("INSERT SCORE")
    SB1.insert(score1)
    print("EMPTY SCOREBOARD 1: ", SB1.is_empty())
    print("LENGTH OF SCOREBOARD 1: ", len(SB1))
    for e in SB1._best:
        print(e.give_score())
    print("INSERT SCORE IN SCOREBOARD 1")
    SB1.insert(score2)
    SB1.insert(score3)
    SB1.insert(score4)
    print("LENGTH OF SCOREBOARD 1: ", len(SB1))
    for e in SB1._best:
        print(e.give_score())

    print("INSERT SCORE IN SCOREBOARD 2")
    SB2 = ScoreBoard(4)
    SB2.insert(score5)
    SB2.insert(score6)
    SB2.insert(score7)
    # print(SB2._best._header._next._element.give_score())
    print("LENGTH OF SCOREBOARD 2: ", len(SB2))
    for e in SB2._best:
        print(e.give_score())

    print("TOPs 1")
    for e in SB1.top(2):
        print(e)

    print("LASTs 1")
    for e in SB1.last(1):
        print(e)

    print("ADD ELEMENTS TO SCOREBOARD 1")
    SB1.insert(score7)
    SB1.insert(score9)
    for e in SB1._best:
        print(e.give_score())
    print("NEW LENGTH OF SCOREBOARD 1: ", len(SB1))
    print("ADD ONE MORE ELEMENT: ", len(SB1))
    SB1.insert(score10)
    for e in SB1._best:
        print(e.give_score())

    print("MERGE SB1 & SB2")
    for e in SB1.merge(SB2):
        print(e)

from my_list_test import CircularPositionalList
from esercizio3 import merge


class ScoreBoard:

    class Score:

        def __init__(self, pl, sc, da):
            self._player = pl
            self._score = sc
            self._date = da

        def __gt__(self, other):
            if not isinstance(other, ScoreBoard.Score):
                raise TypeError("operand is not a Score")
            else:
                return self._score > other._score

        def __eq__(self, other):
            if not isinstance(other, ScoreBoard.Score):
                raise TypeError("operand is not a Score")
            else:
                return self._score == other._score

        def __ge__(self, other):
            return self == other or self > other

        def __lt__(self, other):
            return not self >= other

        def __le__(self, other):
            return not self > other

        def __str__(self):
            return str(self._player) + " " + str(self._date) + " " + str(self._score)

    def __init__(self, x=10):
        self._best = CircularPositionalList()
        self._max = x

    def __len__(self):
        return self._max

    def size(self):
        return len(self._best)

    def is_empty(self):
        return self._best.is_empty()

    def insert(self, s):
        """Inserisce un nuovo score nello scoreboard se e solo se non è peggiore dei risultati
                correntemente salvati. Non incrementa la dimensione dello scoreboard"""
        if self.size() == 0:
            self._best.add_first(s)
        elif self._best.first().element() <= s or self.size() < len(self):
            cursor = self._best.first()
            while cursor != self._best.last() and cursor.element() < s:
                cursor = self._best._next_position(cursor) # super(CircularPositionalList,self._best).after(cursor)
            if cursor.element() < s:
                self._best.add_after(cursor, s)
            elif str(s) != str(cursor.element()):                   #Se sono completamente uguali su nome-data-punteggio non lo inserisco
                self._best.add_before(cursor, s)
            if self.size() > len(self):
                self._best.delete(self._best.first())

    def merge(self, new):
        """Fonde lo scoreboard corrente con new selezionando i 10 migliori risultati"""
        if not isinstance(new, ScoreBoard):
            raise TypeError("The operand is not a ScoreBoard")
        if not(new.is_empty() and self.is_empty()):
            self._best = merge(self._best, new._best)   # Merging ---> RIVEDERE LA RIUTILIZZABILITà ---> PER VIA DELLA DUPLICAZIONE
            while self.size() > len(self):              # seleziona i primi X
                self._best.delete(self._best.first())

    def top(self, i=1):
        """Restituisce i migliori i score nello ScoreBoard"""
        score_list = []
        if not self.is_empty():
            cur = self._best.last()
            counter = 0
            if i >= 1:
                score_list.append(cur.element())
                counter += 1
            while cur != self._best.first() and counter < i:
                cur = self._best._prev_position(cur) # super(CircularPositionalList, self._best).before(cur)
                score_list.append(cur.element())
                counter += 1
        return score_list

    def last(self, i=1):
        """Restituisce i peggiori i score nello ScoreBoard"""
        counter = 0
        score_list = []
        for element in self._best:
            score_list.append(element)
            counter += 1
            if counter == i:
                break
        return score_list

    def __iter__(self):
        for score in self._best:
            yield score


if __name__ == "__main__":
    score1 = ScoreBoard.Score("AAA",10, "15/10/2017")
    score2 = ScoreBoard.Score("BBB",5,"15/10/2017")
    score3 = ScoreBoard.Score("CCC",15,"15/10/2017")
    score4 = ScoreBoard.Score("DDD",7,"15/10/2017")
    score5 = ScoreBoard.Score("EEE",21,"15/10/2017")
    score6 = ScoreBoard.Score("EEE",1,"15/10/2017")
    score7 = ScoreBoard.Score("EEE",56,"15/10/2017")
    score8 = ScoreBoard.Score("EEE",-4,"15/10/2017")
    score9 = ScoreBoard.Score("EEE",18,"15/10/2017")
    score10 = ScoreBoard.Score("EEE",8,"15/10/2017")

    SB1 = ScoreBoard(4)

    print("EMPTY SCOREBOARD 1: ", SB1.is_empty())
    print("LENGTH OF SCOREBOARD 1: ", SB1.size(),"/",len(SB1))
    print("INSERT SCORE")
    SB1.insert(score1)
    print("EMPTY SCOREBOARD 1: ", SB1.is_empty())
    print("LENGTH OF SCOREBOARD 1: ", SB1.size(),"/",len(SB1))
    for e in SB1:
        print(e)
    print("INSERT SCORE IN SCOREBOARD 1")
    SB1.insert(score2)
    SB1.insert(score3)
    SB1.insert(score4)
    print("LENGTH OF SCOREBOARD 1: ", SB1.size(),"/",len(SB1))
    for e in SB1:
        print(e)

    print("INSERT SCORE IN SCOREBOARD 2")
    SB2 = ScoreBoard(4)
    SB2.insert(score5)
    SB2.insert(score6)
    SB2.insert(score7)
    # print(SB2._best._header._next._element.give_score())
    print("LENGTH OF SCOREBOARD 2: ", SB2.size(),"/",len(SB2))
    for e in SB2._best:
        print(e)

    print()
    print("TOPs 2")
    for e in SB1.top(2):
        print(e)

    print("LASTs 1")
    for e in SB1.last():
        print(e)

    print()
    print("ADD ELEMENTS TO SCOREBOARD 1")
    SB1.insert(score7)
    SB1.insert(score9)
    for e in SB1:
        print(e)
    print("NEW LENGTH OF SCOREBOARD 1: ", SB1.size(),"/",len(SB1))
    SB1.insert(score10)
    print("ADD ONE MORE ELEMENT: ", SB1.size(), "/", len(SB1))
    for e in SB1:
        print(e)

    print("MERGE SB1 & SB2")
    for e in SB1:
        print(e)
    print("---------")
    for e in SB2:
        print(e)
    print("---------")

    SB1.merge(SB2)

    for e in SB1:
        print(e)

    print("TEST TOP/LAST")
    for e in SB1.top(10):
        print(e)

    print("--------------------------VOID TEST----------------------------------")
    a = ScoreBoard(10)
    b = ScoreBoard(10)
    print("SIZE ", a.size(), "---- EMPTY ", a.is_empty(), " ---- LEN ", len(a))
    print("----TOP-----")
    for e in a.top(10):
        print(e)
    print("----LAST-----")
    for e in a.last(10):
        print(e)
    print("----ALL-----")
    for e in a:
        print(e)
    SB1.merge(a)
    print("----SB1 MERGING with a-----")
    for e in SB1:
        print(e)
    a.merge(b)
    print("----a MERGING with b-----")
    for e in a:
        print(e)
    a.merge(SB1)
    print("----a MERGING with SB1-----")
    for e in a:
        print(e)
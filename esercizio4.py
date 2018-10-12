from my_list import CircularPositionalList
from esercizio2 import bubblesorted
from esercizio3 import merge


class Score:
    def __init__(self,pl, sc, da):
        self._player = pl
        self._score = sc
        self._date = da

    def __gt__(self, other):
        if not isinstance(other,Score):
            raise TypeError("operand is not a Score")
        else:
            return self._score > other._score

    def __eq__(self, other):
        if not isinstance(other,Score):
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
        return str(self._player)+" "+str(self._date)+" "+str(self._score)

    def give_score(self):
        return self._score

class ScoreBoard:

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
        elif self._best.last().element().give_score() <= s.give_score():
            cursor = self._best.first()
            while cursor != self._best.last() and cursor.element().give_score() > s.give_score():
                cursor = super(CircularPositionalList,self._best).after(cursor)
            if cursor.element().give_score() > s.give_score():
                self._best.add_after(cursor, s)
            else:
                self._best.add_before(cursor, s)
            if self.size() > len(self):
                self._best.delete(self._best.last())
     # Mantengo tutto ordinato



    """def insert(self, s):
        
        if len(self) < self._max:
            #   QUA AGGIUNGE FINCHè NON RAGGIUNGE IL LIMITE MASSIMO, POI AGGIUNGE SE MIGLIORE DEI PRESENTI, IN TESTA, ELIMINADO IL PRIMO
            self._best.add_last(s)
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
            #       self._size += 1"""

    def merge(self, new):
        """Fonde lo scoreboard corrente con new selezionando i 10 migliori risultati"""
        if not isinstance(new, ScoreBoard):
            raise TypeError("The operand is not a ScoreBoard")

        score_merge = merge(self._best.reverse(), new._best.reverse()).reverse() #Potrei aver invertito tutto....
        counter = 0
        for score in score_merge:
            yield score
            counter +=1
            if counter == 10:
                break
        """if self.size() > 10:            #Rivedere traccia
            #seleziona i primi 10
            tmp_list = CircularPositionalList()
            for element in self._best:
                tmp_list.add_last(element)
                if len(tmp_list) == 10:
                    break
            self._best = tmp_list"""

        '''
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
        return new_board.top(10)'''

    def top(self, i=1):
        """Restituisce i migliori i score nello ScoreBoard"""
        counter = 0
        for element in self._best:
            yield element
            counter += 1
            if counter == i:
                break
        """
        imp = len(self) - i
        cur = self._best.first()
        lis = CircularPositionalList()
        for p in range(len(self._best)):
            lis.add_last(cur.element().give_score())
            cur = super(CircularPositionalList, self._best).after(cur)
        counter = 0
        for el in bubblesorted(lis):
            if counter >= imp:
                yield el
            counter += 1"""

    def last(self, i=1):
        """Restituisce i peggiori i score nello ScoreBoard"""
        cur = self._best.last()
        for k in range(i):
            yield cur.element()
            cur = super(CircularPositionalList, self._best).before(cur)
        """counter = 0
        for el in bubblesorted(lis):
            if counter < i:
                yield el
            else:
                break
            counter += 1"""

    def __iter__(self):
        for score in self._best:
            yield score


if __name__ == "__main__":
    score1 = Score("AAA",10, "15/10/2017")
    score2 = Score("BBB",5,"15/10/2017")
    score3 = Score("CCC",15,"15/10/2017")
    score4 = Score("DDD",7,"15/10/2017")
    score5 = Score("EEE",21,"15/10/2017")
    score6 = Score("EEE",1,"15/10/2017")
    score7 = Score("EEE",56,"15/10/2017")
    score8 = Score("EEE",-4,"15/10/2017")
    score9 = Score("EEE",18,"15/10/2017")
    score10 = Score("EEE",8,"15/10/2017")

    # print(score1._player, " ", score1._score, " ", score1._date)

    SB1 = ScoreBoard(4)
    # print("SCOREBOARD DIMENSION: ", SB._max)
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

    print("TOPs 2")
    for e in SB1.top(2):
        print(e)

    print("LASTs 1")
    for e in SB1.last():
        print(e)

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

    for e in SB1.merge(SB2):
        print(e)

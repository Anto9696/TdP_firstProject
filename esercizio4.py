from CircularPositionalList import CircularPositionalList
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
           correntemente salvati quando lo scoreboard è pieno. Non incrementa la dimensione dello scoreboard."""
        if self.size() == 0:                                   #se lo scoreboard è vuoto, lo inserisco come first
            self._best.add_first(s)
        elif self._best.first().element() <= s or self.size() < len(self):     #lo scoreboard è ordinato crescente andando da first a last, per questo controlliamo il primo
            cursor = self._best.first()
            while cursor != self._best.last() and cursor.element() < s:        #usciamo dal ciclo quando arriviamo all'ultimo elem o quando troviamo un elem maggiore o uguale a s (score)
                cursor = self._best._next_position(cursor)
            if cursor.element() < s:                                           #se siamo usciti dal ciclo e l'elem corrente è ancora minore di s, allora inseriamo dopo
                self._best.add_after(cursor, s)
            elif str(s) != str(cursor.element()):        # Se sono completamente uguali su nome-data-punteggio non lo inserisco, se non lo sono lo inserisco prima
                self._best.add_before(cursor, s)
            if self.size() > len(self):                 #ora controllo se eccedo la lunghezza massima, se è così cancello il primo (più piccolo score)
                self._best.delete(self._best.first())

    def merge(self, new):
        """Fonde lo scoreboard corrente con new selezionando gli x migliori risultati"""
        if not isinstance(new, ScoreBoard):
            raise TypeError("The operand is not a ScoreBoard")
        if not (new.is_empty() and self.is_empty()):      #se entrambe le liste non sono vuote richiamiamo il merge dell'esercizio 3
            self._best = merge(self._best, new._best)
            #ORA ANDIAMO AD ELIMINARE I DUPLICATI (nei 2 scoreboard potrebbero essere presenti score uguali)
            if self.size() > 1:                          #altrimenti sicuro non ci sono duplicati
                cursor = self._best.first()
                while cursor != self._best.last():
                    next_cursor = self._best._next_position(cursor)            #scorriamo una voolta lo scoreboard e confrontiamo ciascun elemento con il successivo,
                    if str(cursor.element()) == str(next_cursor.element()):    #possono esserci al più due score uguali e se è così saranno adiacenti
                        self._best.delete(cursor)
                    cursor = next_cursor
            #E ADESSO AGGIIUSTIAMO LA GRANDEZZA DELLO SCORE
            while self.size() > len(self):  # seleziona i primi X
                self._best.delete(self._best.first())

    def top(self, i=1):
        """Restituisce i migliori i score nello ScoreBoard"""
        self._best.reverse()     # essendo già ordinato basta selezionare gli ultimi i della lista su cui viene applicato reverse
        score_list = self.last(i)
        self._best.reverse()
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


# IL TEST E' STATO EFFETTUATO QUI E NON IN verifica.py
if __name__ == "__main__":
    score1 = ScoreBoard.Score("AAA", 10, "15/10/2017")
    score2 = ScoreBoard.Score("BBB", 5, "15/10/2016")
    score3 = ScoreBoard.Score("CCC", 15, "15/10/2015")
    score4 = ScoreBoard.Score("DDD", 7, "15/10/2014")
    score5 = ScoreBoard.Score("EEE", 21, "15/10/2013")
    score6 = ScoreBoard.Score("FFF", 1, "15/10/2012")
    score7 = ScoreBoard.Score("GGG", 56, "15/10/2011")
    score8 = ScoreBoard.Score("HHH", -4, "15/10/2010")
    score9 = ScoreBoard.Score("III", 18, "15/10/2009")
    score10 = ScoreBoard.Score("LLL", 8, "15/10/2008")

    SB1 = ScoreBoard(4)

    print("\n\nEMPTY SCOREBOARD 1: ", SB1.is_empty())
    print("LENGTH OF SCOREBOARD 1: ", SB1.size(), "/", len(SB1))
    print("----------------------------------------------------")

    print("INSERT SCORE: ", score1)
    SB1.insert(score1)
    print("EMPTY SCOREBOARD 1: ", SB1.is_empty())
    print("LENGTH OF SCOREBOARD 1: ", SB1.size(), "/", len(SB1))
    for e in SB1:
        print(e)
    print("----------------------------------------------------")

    print("INSERT SCORE IN SCOREBOARD 1:")
    SB1.insert(score2)
    SB1.insert(score3)
    SB1.insert(score4)
    print(score2)
    print(score3)
    print(score4)

    print("LENGTH OF SCOREBOARD 1: ", SB1.size(), "/", len(SB1))
    for e in SB1:
        print(e)
    print("----------------------------------------------------")

    print("INSERT SCORE IN SCOREBOARD 2")
    SB2 = ScoreBoard(4)
    SB2.insert(score5)
    SB2.insert(score6)
    SB2.insert(score7)
    print(score5)
    print(score6)
    print(score7)
    # print(SB2._best._header._next._element.give_score())
    print("LENGTH OF SCOREBOARD 2: ", SB2.size(), "/", len(SB2))
    for e in SB2._best:
        print(e)

    print()
    print("TOPs 2 in SCOREBOARD 1:")
    for e in SB1.top(2):
        print(e)

    print("LASTs 1 in SCOREBOARD 1:")
    for e in SB1.last():
        print(e)
    print("----------------------------------------------------")

    print("SCOREBOARD 1:")
    for e in SB1:
        print(e)
    print("ADD ELEMENTS TO SCOREBOARD 1")
    SB1.insert(score7)
    SB1.insert(score9)
    print(score7)
    print(score9)

    print("SCOREBOARD 1:")
    for e in SB1:
        print(e)
    print("NEW LENGTH OF SCOREBOARD 1: ", SB1.size(), "/", len(SB1))
    print("----------------------------------------------------")

    print("ADD ELEMENTS TO SCOREBOARD 1")
    SB1.insert(score10)
    print(score10)
    print("NEW LENGTH OF SCOREBOARD 1: ", SB1.size(), "/", len(SB1))
    for e in SB1:
        print(e)
    print("----------------------------------------------------")

    print("<<<<< MERGE SCOREBOARD 1 & SCOREBOARD 2 >>>>>")
    print("SCOREBOARD 1:")
    for e in SB1:
        print(e)
    print("---------")
    print("SCOREBOARD 2:")
    for e in SB2:
        print(e)
    print("---------")
    print("MERGE RESULT:")
    SB1.merge(SB2)

    for e in SB1:
        print(e)

    print("<<<<< TEST TOP/LAST >>>>>")
    print("TOPs SCOREBOARD 1:")
    for e in SB1.top(10):
        print(e)

    print("--------------------------VOID TEST----------------------------------")
    print("a AND b ARE EMPTY SCOREBOARD")
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
    print("----SCOREBOARD 1 MERGING with a-----")
    for e in SB1:
        print(e)
    a.merge(b)
    print("----a MERGING with b-----")
    for e in a:
        print(e)
    a.merge(SB1)
    print("----a MERGING with SCOREBOARD 1-----")
    for e in a:
        print(e)

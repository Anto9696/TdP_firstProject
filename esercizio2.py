from CircularPositionalList import CircularPositionalList


def bubblesorted(list):
    """ordina gli elementi della CircularPositionalList e li restituisce nell’ordine risultante.
       Non modifica l'ordine di memorizzazione degli elementi nella lista passatagli."""
    list_ordered = list.copy()
    if not list_ordered.is_empty():
        sup = len(list_ordered) - 1
        while sup != 0:                #perchè se list aveva meno di 2 elem
            last_swap = 0
            cursor = list_ordered.first()
            succ_cursor = list_ordered._next_position(cursor)
            for i in range(sup):
                if cursor.element() > succ_cursor.element():
                    list_ordered.replace(succ_cursor, list_ordered.replace(cursor, succ_cursor.element()))
                    last_swap = i
                cursor = succ_cursor
                succ_cursor = list_ordered._next_position(cursor)
            sup = last_swap

    for element in list_ordered:
        yield element


    # IL TEST E' STATO EFFETTUATO QUI E NON IN verifica.py
if __name__ == "__main__":
    list1 = CircularPositionalList()
    list2 = CircularPositionalList()
    for i in range(10):
        list1.add_first(i)
        list2.add_last(i + 11)

    print("LIST 1")
    print(list1)
    print("ORDERED LIST 1")
    out = ""
    for e in bubblesorted(list1):
        out += str(e) + ", "
    print(out[:-2])

    print("LIST 2")
    print(list2)
    print("ORDERED LIST 2")
    out = ""
    for e in bubblesorted(list2):
        out += str(e) + ", "
    print(out[:-2])

    list3 = list1 + list2
    print("LIST 3 (is list1 + list2)")
    print(list3)

    print("ORDERED LIST 3")
    out = ""
    for e in bubblesorted(list3):
        out += str(e) + ", "
    print(out[:-2])

    list4 = CircularPositionalList()
    print("LIST 4 is an empty list")
    print("ORDERED LIST 4")
    out = ""
    for e in bubblesorted(list4):
        out += str(e) + ", "
    if not out:
        print("[empty]")

    list4.add_first(3)
    print("ADDED 3 AT LIST 4")
    print("ORDERED LIST 3")
    out = ""
    for e in bubblesorted(list4):
        out += str(e) + ", "
    print(out[:-2])








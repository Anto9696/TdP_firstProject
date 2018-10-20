from CircularPositionalList import CircularPositionalList


def bubblesorted(list):
    """ordina gli elementi della CircularPositionalList e
    li restituisce nell’ordine risultante."""
    list_ordered = list.copy()
    sup = len(list_ordered) - 1
    while sup != 0:
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
    print("LIST 2")
    print(list2)

    list3 = list1 + list2
    print("LIST 3")
    print(list3)

    print("ORDERED LIST 3")
    out = ""
    for e in bubblesorted(list3):
        out += str(e) + ", "
    print(out[:-2])

    print("LIST 3")
    print(list3)

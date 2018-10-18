from my_list_test import CircularPositionalList
import random

print("\nBenvenuto nella sezione di test, diamoci da fare!\nChe tipo di test desideri effettuare?\n")
print("\t\tI = interattivo\n\t\tS = Standard (Esercizio 5)\n")
scelta = ""
while(scelta.upper() != "I" and scelta.upper() !="S"):
    scelta = input("Digita la tua scelta [I/S]: ")

if scelta.upper() == "I":
    print("\n\t\t<<<<<<<<<< INTERACTIVE TEST >>>>>>>>>>>\n")
    print("[1] PARTI DA UNA LISTA VUOTA\n[2] PARTI DA UNA LISTA CASUALE\n[3] QUIT\n")
    scelta = ""
    while scelta != "1" and scelta != "2" and scelta != "3":
        scelta = input("Digita la tua scelta: ")

    if scelta == "1":
        list1 = CircularPositionalList()
        print("\nEcco la tua lista di partenza: [vuota]")
    elif scelta == "2":
        list1 = CircularPositionalList()
        for i in range(10):
            list1.add_first(random.randint(0,100))
        print("\nEcco la tua lista di partenza: ", str(list1))
    elif scelta == "3":
        exit(0)

    print("-------------------------------------")
    scelta = ""
    while scelta != "Q":
        print("LISTA: ", str(list1))
        print("SCEGLI L'AZIONE DA SVOLGERE:\n")
        print("1. Aggiungi in coda alla lista altri X elementi")
        print("2. Add After")
        print("3. Add Before")
        print("4. Add First")
        print("5. Add Last")
        print("6. length")
        print("7. Clear")
        print("8. Delete")
        print("9. Find")
        print("10. Contain")
        print("11. Replace")
        print("12. Reverse")
        print("13. First")
        print("14. Last")
        print("15. Is sorted")
        print("16. Stampa albero di natale con gli *")
        print("Scrivere Q per terminare il programma")
        scelta = input("Digita la tua scelta: ")

        if scelta == "1":
            list2 = CircularPositionalList()
            length = int(input("Quanti elementi vuoi nella lista? ")) # gli input sono sempre stringhe
            for i in range(length):
                el = int(input("Inserisci elemento: "))
                list2.add_first(el)
            list1 = list1 + list2
            print("LIST 1: ", str(list1))
            print("-----------------------------------------------------------")
        elif scelta == "2":
            element = int(input("Valore da inserire: "))
            pos = int(input("Dopo quale valore già presente lo vuoi inserire? "))
            try:
                list1.add_after(list1.find(pos), element)
                print("LIST 1 aggiornata: ", str(list1))
            except TypeError:
                print("Il valore selezionato non è presente!")
                print("-----------------------------------------------------------")
        elif scelta == "3":
            element = int(input("Valore da inserire: "))
            pos = int(input("Prima di quale valore già presente lo vuoi inserire? "))
            try:
                list1.add_before(list1.find(pos), element)
                print("LIST 1 aggiornata: ", str(list1))
            except TypeError:
                print("Il valore selezionato non è presente!")
            print("-----------------------------------------------------------")
        elif scelta == "4":
            element = int(input("Valore da inserire all'inizio: "))
            list1.add_first(element)
            print("LIST 1 aggiornata: ", str(list1))
            print("-----------------------------------------------------------")
        elif scelta == "5":
            element = int(input("Valore da inserire alla fine: "))
            list1.add_last(element)
            print("LIST 1 aggiornata: ", str(list1))
            print()
        elif scelta == "6":
            print("La lunghezza della lista è: ", len(list1))
            print("-----------------------------------------------------------")
        elif scelta == "7":
            print("La lista1 è stata cancellata")
            list1.clear()
            print("LIST 1 - len: ",len(list1))
            print("LIST 1: ", str(list1))
            print("-----------------------------------------------------------")
        elif scelta == "8":
            element = int(input("Quale elemento vuoi eliminare? "))
            try:
                list1.delete(list1.find(element))
                print("LIST 1: ", str(list1))
            except TypeError:
                print("Il valore selezionato non è presente!")

            print("-----------------------------------------------------------")
        elif scelta == "9":
            element = int(input("Trova elemento: "))
            try:
                print(list1[list1.find(element)], "è stato trovato")
            except TypeError:
                print("Il valore selezionato non è presente!")

            print("-----------------------------------------------------------")
        elif scelta == "10":
            element = int(input("Elemento contenuto: "))
            print(element, " è contenuto nella lista?")
            try:
                print(list1.find(element) in list1)
            except TypeError:
                print("Il valore selezionato non è presente!")

            print("-----------------------------------------------------------")
        elif scelta == "11":
            element = int(input("Inserire nuovo elemento: "))
            pos = int(input("Inserire vecchio elemento: "))
            print("REPLACE ", pos, " CON ", element, " nella LIST 1")
            try:
                old_element = list1.replace(list1.find(pos), element)
                print("LIST 1: ", str(list1))
                print("OLD ELEMENT: ", str(old_element))
            except TypeError:
                print("Il valore selezionato non è presente!")

            print("-----------------------------------------------------------")
        elif scelta == "12":
            list1.reverse()
            print("REVERSE DELLA LIST 1: ", str(list1))
            print("-----------------------------------------------------------")
        elif scelta == "13":
            print("Il primo elemento è ", str(list1[list1.first()]))
            print("-----------------------------------------------------------")
        elif scelta == "14":
            print("L'ultimo elemento è ", str(list1[list1.last()]))
            print("-----------------------------------------------------------")
        elif scelta == "15":
            if list1.is_sorted():
                print("La lista è ordinata")
            else:
                print("La lista non è ordinata")
            print("-----------------------------------------------------------")
        elif scelta == "16":
            n = int(input("Inserire altezza albero: "))
            for i in range(n):
                print(("*" * (i * 2 + 1)).center(n * 2 - 1))
            print("-----------------------------------------------------------")
        elif scelta == "Q" or scelta == "q":
            exit(0)

elif scelta.upper() == "S":
    print("\n\t\t<<<<<<<<<< STANDARD TEST >>>>>>>>>>>\n")

    list1 = CircularPositionalList()
    list1.add_first(2)
    list1.add_last(10)
    list1.add_after(list1.find(2), 6)
    list1.add_before(list1.find(10), 8)
    list2 = list1.copy()

    print("\nEcco le due liste di riferimento:\n")

    print("LIST 1: ", str(list1))
    print("LIST 2: ", str(list2))


    print("-----------------------------------------------------------")

    list1.add_first(-2)
    print("ADDED -2 at the beginning of LIST1 ")
    list2.add_first(-2)
    print("ADDED -2 at the beginning of LIST2 ")
    print("LIST 1: ", str(list1))
    print("LIST 2: ", str(list2))

    print("-----------------------------------------------------------")

    list1.add_last(-32)
    print("ADDED -32 at the end of LIST1 ")
    list2.add_last(-32)
    print("ADDED -32 at the end of LIST2 ")
    print("LIST 1: ", str(list1))
    print("LIST 2: ", str(list2))

    print("-----------------------------------------------------------")

    print("FOUND 6 IN LIST 1: ", list1.find(6).element() == 6)
    print("FOUND 6 IN LIST 2: ", list2.find(6).element() == 6)
    print("FOUND -3 IN LIST 1: ", list1.find(-3) == -3)
    print("FOUND -3 IN LIST 2: ", list2.find(-3) == -3)

    print("-----------------------------------------------------------")

    for i in range(10):
        list1.add_first(i)
        print("ADDED ",i," at the beginning of LIST1 ")
        list2.add_first(i)
        print("ADDED ", i, " at the beginning of LIST2 ")
        list1.add_last(i + 11)
        print("ADDED ",i+11," at the end of LIST1 ")
        list2.add_last(i + 11)
        print("ADDED ", i + 11, " at the end of LIST2 ")

    print("LIST 1 - len: ",len(list1))
    print("LIST 1: ", str(list1))

    print("LIST 2 - len: ",len(list2))
    print("LIST 2: ", str(list2))

    print("-----------------------------------------------------------")

    list3 = list1 + list2
    print("LIST 3 - len: ",len(list3))
    print("LIST 3: ", str(list3))
    list3.reverse()
    print("REVERSE OF LIST 3: ", str(list3))
    print("CLEAR LIST 3")
    list3.clear()
    print("LIST 3 - len: ",len(list3))
    print("LIST 3: ", str(list3))


    print("-----------------------------------------------------------")

    value=list1.add_before(list1.first(),-1)
    print("ADDED  ",value.element()," before first of list1")
    value=list2.add_before(list2.first(),-1)
    print("ADDED  ",value.element()," before first of list1")

    value=list1.add_before(list1.find(5),-100)
    print("ADDED  ",value.element()," before 5 of list1")
    value=list2.add_before(list2.find(5),-100)
    print("ADDED  ",value.element()," before 5 of list2")

    value=list1.add_after(list1.last(),100)
    print("ADDED  ",value.element()," after last of list1")
    value=list2.add_after(list2.last(),100)
    print("ADDED  ",value.element()," after last of list2")

    value=list1.add_after(list1.find(15),-100)
    print("ADDED  ",value.element()," after 15 of list1")
    value=list2.add_after(list2.find(15),-100)
    print("ADDED  ",value.element()," after 15 of list2")

    print("AFTER INSERT LIST 1 - len ",len(list1))
    print("AFTER INSERT LIST 2 - len ",len(list2))

    print("LIST 1: ", str(list1))
    print("LIST 2: ", str(list2))

    print("-----------------------------------------------------------")
    print("FIND -100 AND -101010 in LIST 1:")
    print(list1.find(-100).element())
    print(list1.find(-101010))
    print("FIND -100 AND -101010 in LIST 1:")
    print(list2.find(-100).element())
    print(list2.find(-101010))

    print("-----------------------------------------------------------")

    print("LIST 1: ", str(list1))
    print("LIST 2: ", str(list2))
    print("FIND 1 in LIST 1 AND USE get_item:")
    print(list1[list1.find(1)])
    print("FIND 1 in LIST 2 AND USE get_item:")
    print(list2[list2.find(1)])

    print("IS 1 CONTAINED IN LIST 1?")
    print(list1.find(1) in list1)
    print("Is 1 CONTAINED IN LIST 2?")
    print(list2.find(1) in list2)

    print("IS 27 CONTAINED IN LIST 1?")
    try:
        list3.add_first(27)
        pos = list3.first()
        print(pos in list1)
        print("27 is contained in LIST 1")
    except ValueError or TypeError :
        print("p does not belong to this container, so it isn't contained")

    print("IS 27 CONTAINED IN LIST 2?")
    try:
        list3.add_first(27)
        pos = list3.first()
        print(pos in list2)
        print("27 is contained in LIST 2")
    except ValueError or TypeError :
        print("p does not belong to this container, so it isn't contained")

    print("-----------------------------------------------------------")

    print("LIST 1: ", str(list1))
    print("LIST 2: ", str(list2))
    print("DELETE 1 IN LIST 1")
    del list1[list1.find(1)]
    print("LIST 1: ", str(list1))
    print("DELETE 1 IN LIST 2")
    del list2[list2.find(1)]
    print("LIST 2: ", str(list3))

    print("-----------------------------------------------------------")

    list1.delete(list1.find(9))
    print("DELETE 9 IN LIST 1")
    print("LIST 1: ", str(list1))
    list2.delete(list2.find(9))
    print("DELETE 9 IN LIST 2")
    print("LIST 2: ", str(list2))

    print("-----------------------------------------------------------")


    print("REPLACE -100 WITH -500 in LIST 1")
    old_element = list1.replace(list1.find(-100), -500)
    print("LIST 1: ", str(list1))
    print("OLD ELEMENT: ", str(old_element))

    print("REPLACE -100 WITH -500 in LIST 2")
    old_element = list2.replace(list2.find(-100), -500)
    print("LIST 2: ", str(list2))
    print("OLD ELEMENT: ", str(old_element))

    print("-----------------------------------------------------------")

    print("REPLACE 27 (not exist) WITH -27 in LIST 1")
    try:
        old_element = list1.replace(list1.find(27), -27)
        print("LIST 1: ", str(list1))
        print("OLD ELEMENT: ", str(old_element))
    except TypeError:
        print("ELEMENT DOES NOT EXSIST")

    print("REPLACE 27 (not exist) WITH -27 in LIST 2")
    try:
        old_element = list2.replace(list2.find(27), -27)
        print("LIST 2: ", str(list2))
        print("OLD ELEMENT: ", str(old_element))
    except TypeError:
        print("ELEMENT DOES NOT EXSIST")

    print("-----------------------------------------------------------")

    print("LIST 1: ", str(list1))
    print("REPLACE 12 WITH -1000 in LIST 1")
    list1[list1.find(12)]= -1000
    print("LIST 1: ", str(list1))

    print("LIST 2: ", str(list2))
    print("REPLACE 12 WITH -1000 in LIST 2")
    list2[list2.find(12)]= -1000
    print("LIST 2: ", str(list2))

    print("-----------------------------------------------------------")

    print("LIST 1: ", str(list1))
    print("LIST 2: ", str(list2))
    print("CLEAR LIST 1 AND LIST 2")
    list1.clear()
    list2.clear()
    print("LIST 1: ", str(list1))
    print("LIST 2: ", str(list2))

    list1.reverse()         #reverse of an empty list
    list2.reverse()         #reverse of an empty list
    print("REVERSE OF LIST 1: ", str(list1))
    print("REVERSE OF LIST 2: ", str(list2))


    list1.add_first(-2)
    print("ADDED -2 to LIST1")
    list2.add_first(-2)
    print("ADDED -2 to LIST2")
    print("LIST 1: ", str(list1))
    print("LIST 2: ", str(list2))
    list1.reverse()                         #reverse of a list with one node
    list2.reverse()                         #reverse of a list with one node
    print("REVERSE OF LIST 1: ", str(list1))
    print("REVERSE OF LIST 2: ", str(list2))

    list1.add_first(10)                                             #reverse of a list with 2 elements
    print("ADDED 10 to LIST1")
    list2.add_first(10)                                             #reverse of a list with 2 elements
    print("ADDED 10 to LIST2")
    print("LIST 1: ", str(list1))
    print("LIST 2: ", str(list2))
    list1.reverse()
    list2.reverse()
    print("REVERSE OF LIST 1: ", str(list1))
    print("REVERSE OF LIST 2: ", str(list2))

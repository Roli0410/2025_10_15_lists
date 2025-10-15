""" program generáljon 10 darab véletlenszámot [1;3] intervallumon, ezeket tárolja egy listában, a lista tartalmát írja ki a képernyőre!
A felhasználónak legyen lehetősége megadni egy számot [1;3] intervallumon,
és a program törölje ennek a számnak valamennyi előfordulását a listából, majd írja ki a módosított listát a képernyőre!"""

import random 

szamok = [random.randint (1, 3 ) for i in range(10)]

megadott_szam = int(input("Adj meg egy számot 1-től 3-ig "))

if megadott_szam in szamok:
    for i in range(szamok.count(megadott_szam)):
        szamok.remove(megadott_szam)
    print(szamok)

elif megadott_szam not in szamok:
    print("A megadott szám nincs a számok között")

#while megadott_szam in szamok: szamok.remove(megadott_szam) - ez egyszerűbb 



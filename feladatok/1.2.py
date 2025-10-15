"""Alakítsuk át az előbbi programot úgy, hogy a program arról adjon tájékoztatást,
hogy pontosan hányszor szerepel a felhasználó által megadott szín a listában! 
Ha a megadott szín nincs még tárolva, továbbra is a "A megadott szín nem szerepel a listában." szöveg jelenjen meg!
"""

szinek = ["zöld", "piros","sárga", "kék" ]
valasztott_szin = (str(input("Adj meg egy színt ")))

darabszam = szinek.count(valasztott_szin)

if darabszam > 0:
    print(f"A {valasztott_szin} már {darabszam}-szor/szer benne van az alap színekben " )
    print(szinek)

elif valasztott_szin not in szinek:
    print(f"A {valasztott_szin} nincs az alapszínek között")
    print(szinek)


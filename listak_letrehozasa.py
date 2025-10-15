"""https://sulipy.hu/listak/listak_letrehozasa?tab=peldak"""

honapok = ['január', 'február','március', 'április', 'május', 'június']

print(type(honapok))
print("----------------------------------")
# lista hossza: len( )
print(len(honapok))
print("----------------------------------")
# a 0. indexű az első elem
print(honapok[0])
print(honapok[1])
print(honapok[2])
print(honapok[3])
print(honapok[4])
print(honapok[5])
print("----------------------------------")
print(f"Utolsó elem a listában:{honapok}"[-1])

# az 1-es és 2-es indexű elemek kiíratása
print("----------------------------------")
print(honapok[1:3])

# az elejétől a 2-es indexű elemmel bezárólag
print(honapok[:3])

# 2-es indexű elemtől a végéig
print("----------------------------------")
print(honapok[2:])


print("----------------------------------")
print(",".join(honapok))

#lista bejárása , i = növekvő szám
print("----------------------------------")
for i in range(len(honapok)):
    print(honapok[i])

print("----------------------------------")
for honap in honapok:
    print(honap)





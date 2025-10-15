honapok = ['január', 'február','március', 'április', 'május', 'június']

honapok.append('július')
print(honapok)

# eltávolítja a legutolsó elemet, és azzal tér vissza
# itt például a törölt értéket a 'torolt_honap' fogja tartalmazni
honapok.pop()
print(f"Utolsó hónap törlése után a lista: {honapok}")
torolt_honap = honapok.pop()
print(f"Utolsó hónap: {torolt_honap}")
print(honapok)

#törlés adott index alapján
torolt_honap = honapok.pop(0)
print(torolt_honap)

print(honapok.remove("február"))
print(honapok)

#adott indexű helyre beszúrja az adott elemet
honapok.insert(0, "február")
print(honapok)

#lista kiürítése
honapok.clear()
print(honapok)


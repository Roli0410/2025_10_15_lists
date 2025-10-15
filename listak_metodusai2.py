honapok = ['január', 'február','március', 'április', 'május', 'június']

#sorbarendezi a listát

sorted_honapok = sorted(honapok)
print(honapok)
print(sorted_honapok)
#print(honapok.sort())
#print(honapok)

reversed_honapok = sorted(honapok, reverse=True)
print(reversed_honapok)

#az adott elem előfordulásának indexe
print(honapok.index("március"))

print("április" in honapok)
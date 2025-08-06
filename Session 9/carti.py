numere = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
culori = ['Inima Rosie', 'Inima Neagra', 'Trefla', 'Romb']

# carti = set()
#
# for numar in numere:
#     for culoare in culori:
#         carti.add((numar, culoare))

carti = {(numar, culoare) for numar in numere for culoare in culori}

print(carti)

# carti.add('Joker Rosu')
# carti.add('Joker Negru')
#
# while len(carti) > 5:
#     print(carti.pop())
#
# print(carti)

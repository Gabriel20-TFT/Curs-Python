lista1 = [1, 2, 3, 10]
lista2 = [1, 7, 8, 9, 10]

set1 = set(lista1)
set2 = set(lista2)

elemente_comune = list(set1 & set2)
doar_lista1 = list(set1 - set2)
doar_lista2 = list(set2 - set1)
doar_in_una_din_liste = list(set1 ^ set2)

print("Elemente comune:", elemente_comune)
print("Doar in lista 1:", doar_lista1)
print("Doar in lista 2:", doar_lista2)
print("In fix una dintre liste (dar nu in ambele):", doar_in_una_din_liste)

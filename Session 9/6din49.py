set_numere = {str(i) for i in range(1, 50)}

numere_trase = set()

for i in range(6):
    numere_trase.add(int(set_numere.pop()))

set_numere_alese = {int(input(f"Alege numarul {i + 1}: ")) for i in range(6)}

print(numere_trase)
print(set_numere_alese)

print(f"Ai nimerit {len(numere_trase.intersection(set_numere_alese))} numere.")
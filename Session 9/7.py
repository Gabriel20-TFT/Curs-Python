cuvant = input("Spune un cuvant: ")

aparitii_caractere = {char: cuvant.count(char) for char in cuvant}
caractere_distincte = set(cuvant)

while True:
    aparitii_valori = {aparitii: list(aparitii_caractere.values()).count(aparitii) for aparitii in aparitii_caractere.values()}
    if len(aparitii_valori) == 1 and list(aparitii_valori.values())[0] == 1:
        print("Se poate!")
        break

    if len(aparitii_valori) != 2:
        print("Nu se poate!")
        break

    if -1 in aparitii_valori:
        print("Nu se poate!")
        break

    if 0 in aparitii_valori and 1 in aparitii_valori and aparitii_valori[1] == 1:
        print("Se poate!")
        break

    for char in caractere_distincte:
        aparitii_caractere[char] -= 1

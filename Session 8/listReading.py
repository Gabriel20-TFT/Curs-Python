# lungime = int(input("Cate elemente vrei sa fie in lista? "))
#
# lista = []
# for i in range(lungime):
#     lista.append(int(input(f"Care vrei sa fie elementul de pe pozitia {i + 1}? ")))

# lista = [int(input(f"Care vrei sa fie elementul de pe pozitia {i + 1}? ")) for i in range(int(input("Cate elemente vrei sa fie in lista? ")))]
#
# print(lista)

# lista1 = list(map(int, input("Introdu elementele listei 1 separate prin spațiu: ").split()))


rez = list(map(int, input("Introdu elementele listei 1 separate prin spațiu: ").split()))
print(rez, type(rez))

# print(lista1)
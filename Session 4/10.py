numarul = int(input("Scrie un numar:"))

suma = 0

while True:
    suma += numarul % 10
    numarul //= 10
    print(suma, numarul)

    if numarul == 0:
        break

if suma % 8 == 0:
    print("Suma cifrelor e divizibila cu 8")
else:
    print("Suma cifrelor nu e divizibila cu 8")
def suma_din_string(s):
    lista_char = [char for char in s]
    for i in range(len(lista_char)):
        if not lista_char[i].isdigit():
            lista_char[i] = " "
    numere = "".join(lista_char).split()

    suma = 0

    for numar in numere:
        suma += int(numar)
    return suma

if __name__ == '__main__':
    s = 'eu am 33 de ani. in 2 luni va fi ziua mea de nume'
    print(suma_din_string(s))
if __name__ == "__main__":
    myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    myStrList = list(map(lambda x: x * x, myList))
    print(myStrList)

    suma = lambda x, y: x + y
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    lista2 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    lista3 = list(map(suma, lista1, lista2))
    print(lista3)

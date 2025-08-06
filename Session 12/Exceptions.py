if __name__ == '__main__':
    # dictionar = {"nume": "Catalin", "varsta": 26}
    # try:
    #     print(dictionar["prenume"])
    # except KeyError as e:
    #     print("KeyError")

    # while True:
    #     try:
    #         number = int(input("Numar: "))
    #         rezultat = 100 / number
    #         print(rezultat)
    #     except ValueError:
    #         print("Ai introdus o valoare care nu e numar intreg! Incearca iar.")
    #     except ZeroDivisionError:
    #         print("Ai introdus 0 la care nu se poate imparti! Incearca iar.")
    #     else:
    #         break

    numar = int(input("Numar: "))
    if numar < 10:
        print(numar)
    else:
        # raise Exception("Numar prea mare!")
        raise ValueError("Numarul e prea mare (maxim 9)")

    print("Ruleaza in continuare...")
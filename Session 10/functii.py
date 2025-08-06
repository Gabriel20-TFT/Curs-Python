# def functie(a, b, *args, x=1, **kwargs):
#     sum = 0
#     print(x)
#     print(args)
#     print(kwargs)

def ridicare_putere(x, exponent=2):
    return x**exponent

def radical(x, ordin=2):
    return x ** (1 / ordin)

if __name__ == '__main__':
    print(radical(8, 3))

    # functie(1, 2, 3, 4, 5, x=10, y=20, z=30)


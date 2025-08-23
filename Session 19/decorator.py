from datetime import datetime


def timer_decorator(f):
    def wrapper_with_timer(*args, **kwargs):
        now = datetime.now()
        rezultat = f(*args, **kwargs)
        print(f'Rularea a durat {datetime.now() - now}.')
        return rezultat

    return wrapper_with_timer


def list_decorator(f):
    def wrapper(*args, **kwargs):
        rezultat = f(*args, **kwargs)
        return rezultat, len(rezultat)

    return wrapper


@timer_decorator
def suma_n(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma


@timer_decorator
def factorial(n):
    produs = 1
    for i in range(1, n + 1):
        produs *= i
    return produs


@timer_decorator
def suma_numere(*args):
    return sum(args)

@list_decorator
def get_n_list(n):
    return list(range(1, n + 1))


if __name__ == '__main__':
    print(factorial(50))
    print(suma_n(50000000))

    print(suma_numere(1, 3, 6, 8, 2))

    print(get_n_list(50))

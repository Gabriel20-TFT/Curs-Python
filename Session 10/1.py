import time

def list_speed_test(x):
    start_time = time.time()

    lista = []
    for i in range(x):
        lista.append(i)

    end_time = time.time()
    time_elapsed = end_time - start_time
    return time_elapsed

def list_compr_speed_test(x):
    start_time = time.time()

    lista = [i for i in range(x)]

    end_time = time.time()
    time_elapsed = end_time - start_time
    return time_elapsed

if __name__ == '__main__':
    x = 400000
    suma_durata_clasic = 0
    for i in range(10):
        suma_durata_clasic += list_speed_test(x)
    suma_durata_compr = 0
    for i in range(10):
        suma_durata_compr += list_compr_speed_test(x)
    print(suma_durata_clasic)
    print(suma_durata_compr)

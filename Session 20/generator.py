def range_generator(start, stop, step=1):
    i = start
    while i < stop:
        yield i
        i += step

if __name__ == '__main__':
    gen1 = (x for x in range(10000))
    gen2 = range_generator(100, 200, 3)
    for x in gen2:
        print(x)
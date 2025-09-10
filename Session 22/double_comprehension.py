def func1():
    def func2():
        print("Function 2")

    print("Function 1")


if __name__ == "__main__":
    triplets = [(x, y, z) for x in range(10) for y in range(10) for z in range(10) if x < y < z]
    divizori = [[j for j in range(1, i + 1) if i % j == 0] for i in range(10, 30)]
    # print(divizori)

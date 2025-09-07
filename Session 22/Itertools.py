import itertools

if __name__ == '__main__':
    # for number in itertools.count(start=1, step=2):
    #     if number > 10:
    #         break
    #     print(number)

    # for i in itertools.cycle([1, 2, 3, 4, 5]):
    #     print(i)

    # print("Printing the numbers repeatedly : ")
    # print(list(itertools.repeat(25, 1000)))
    # for i in itertools.repeat(100, 1000):
    #     print(i)

    # print("The cartesian product using repeat:")
    # print(list(itertools.product([1, 2], repeat=4)))
    # print()
    #
    # print("The cartesian product of the containers:")
    # print(list(itertools.product(['geeks', 'for', 'geeks'], '2')))
    # print()
    #
    # print("The cartesian product of the containers:")
    # print(list(itertools.product('AB', [3, 4])))

    print("All the permutations of the given list is:")
    print(list(itertools.permutations([1, 'geeks'], 2)))
    print()

    print("All the permutations of the given string is:")
    print(list(itertools.permutations('AB')))
    print()

    print("All the permutations of the given container is:")
    print(list(itertools.permutations(range(10), 5)))
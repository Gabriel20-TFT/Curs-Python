import os

if __name__ == '__main__':
    # print(os.listdir())
    # os.chdir('../')
    # print(os.listdir())
    # os.makedirs("TestFolder/TestFolder2")
    # print(os.stat("log.txt"))
    for x in os.walk(os.getcwd()):
        print(x)

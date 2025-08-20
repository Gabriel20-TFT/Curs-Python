class ClasaA:
    def __init__(self):
        print("Init A")

    def vorbeste(self):
        print("Vorbeste A")

class ClasaB(ClasaA):
    def __init__(self):
        super().__init__()
        print("Init B")

    def vorbeste(self):
        print("Vorbeste B")

class ClasaC(ClasaA):
    def __init__(self):
        super().__init__()
        print("Init C")

    def vorbeste(self):
        print("Vorbeste C")

class ClasaD(ClasaB, ClasaC):
    def __init__(self):
        super().__init__()
        print("Init D")
        super().vorbeste()

    def vorbeste(self):
        print("Vorbeste D")

if __name__ == "__main__":
    # a = ClasaA()
    # b = ClasaB()
    # c = ClasaC()
    d = ClasaD()

    # a.vorbeste()
    # b.vorbeste()
    # c.vorbeste()
    # d.vorbeste()

    print(ClasaD.mro())

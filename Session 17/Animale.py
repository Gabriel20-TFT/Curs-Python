class Animal:
    def __init__(self, nume_specie, varsta):
        self.nume_specie = nume_specie
        self.varsta = varsta

    def __str__(self):
        return f"Animal - ({self.nume_specie} - {self.varsta})"

class Mamifer(Animal):
    def __init__(self, nume_specie, varsta, picioare):
        super().__init__(nume_specie, varsta)

        self.picioare = picioare

    def __str__(self):
        return f"Mamifer - ({self.nume_specie} - {self.varsta} - {self.picioare})"

if __name__ == "__main__":
    # anumal1 = Animal("Homo Sapiens", 26)
    # print(anumal1)
    mamifer1 = Mamifer("Homo Sapiens", 26, 2)
    print(mamifer1)
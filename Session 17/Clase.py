class Angajat:
    def __init__(self, prenume, nume, pozitie, salariu, inceput_program, sfarsit_program):
        self.prenume = prenume
        self.nume = nume
        self.pozitie = pozitie
        self.salariu = salariu
        self.inceput_program = inceput_program
        self.sfarsit_program = sfarsit_program

        self.bani_acumulati = 0

    def __str__(self):
        return f'Angajat - {self.prenume} {self.nume} ({self.pozitie} - {self.salariu}$)'

    def program(self):
        return f"{self.inceput_program} - {self.sfarsit_program}"

    def schimba_pozitia(self, pozitie, salariu=None, inceput_program=None, sfarsit_program=None):
        self.pozitie = pozitie
        if salariu is not None:
            self.salariu = salariu
        if inceput_program is not None:
            self.inceput_program = inceput_program
        if sfarsit_program is not None:
            self.sfarsit_program = sfarsit_program

    def primire_salariu(self):
        self.bani_acumulati += self.salariu


if __name__ == '__main__':
    angajatCatalin = Angajat("Catalin", "Breaz", "Python Developer", 1000, "9:00", "18:00")

    # print(angajatCatalin)
    # print(angajatCatalin.program())
    #
    # angajatCatalin.schimba_pozitia("Java Developer", 750)
    #
    # print(angajatCatalin)
    # print(angajatCatalin.program())

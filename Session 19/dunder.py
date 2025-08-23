class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f'{self.name} {self.surname}'

    # def __repr__(self):
    #     return f'Person(name={self.name}, surname={self.surname}, age={self.age})'

    def __add__(self, other):
        if isinstance(other, Person):
            return Person(self.name, self.surname, self.age + other.age)
        elif isinstance(other, int):
            return Person(self.name, self.surname, self.age + other)
        else:
            raise TypeError

    def __neg__(self):
        return Person(self.name, self.surname, -self.age)

    def __sub__(self, other):
        return self + (-other)
        # return Person(self.name, self.surname, self.age - other.age)

    def __eq__(self, other):
        return self.name == other.name and self.surname == other.surname and self.age == other.age

    def __ne__(self, other):
        return not(self == other)

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return not(self < other) and (self != other)

    def __le__(self, other):
        return not(self > other)

    def __ge__(self, other):
        return not(self < other)

    def string_value(self):
        return f"{self.name} {self.surname} {self.age}"

if __name__ == '__main__':
    person1 = Person('Catalin', 'Breaz', 26)
    person2 = Person('Alexandru', 'Cataramba', 23)
    # listaPersoane = [person1, person2]
    # print(listaPersoane)
    print(f'Person 1 = {person1}')

    # print(repr(person1 - person2))

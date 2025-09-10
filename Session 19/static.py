class Person:
    contor_persoane = 0

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Person.contor_persoane += 1

    @staticmethod
    def countPersons():
        print(Person.contor_persoane)


class Student(Person):
    def __init__(self, name, age, gender, grades):
        super().__init__(name, age, gender)
        Student.contor_persoane += 1
        self.grades = grades


if __name__ == '__main__':
    Person.countPersons()
    person1 = Person('Catalin', 'Breaz', 26)
    student1 = Student('Mihai', 'Mihalcea', 40, [10, 9, 9.5])
    Person.countPersons()


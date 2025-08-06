# student = {"nume": "Breaz", "prenume": "Catalin", "varsta": 26, "note": [8, 9.6, 7.23]}
# # numere = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight"}
#
# # for key in student:
# #     print(f"{key} - {student[key]}")
#
# # for value in numere.values():
# #     print(value)
#
# for key, value in student.items():
#     print(key, value)

# numar = int(input("Zi cate elemente vrei sa fie in lista: "))
#
# lista = []
# for i in range(numar):
#     lista.append(input("Zi-mi un nou string: "))

# student = {}
#
# student['nume'] = input("Zi-mi numele studentului: ")
# student['prenume'] = input("Zi-mi prenumele studentului: ")
# student['varsta'] = int(input("Zi-mi varsta studentului: "))
#
# print(student)

dictionar = {}

while True:
    key = input("Zi o noua cheie (leave blank to quit): ")

    if key == "":
        break

    dictionar[key] = input("Zi o valoare: ")

print(dictionar)
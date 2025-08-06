mesaj = input("Scrie un mesaj: ")

# pozitie_punct = mesaj.find(".")
# if pozitie_punct == -1:
#     if mesaj.isdigit():
#         print(int(mesaj))
#     else:
#         print("Nu e numar")
# else:
#     if mesaj[:pozitie_punct].isdigit() and mesaj[pozitie_punct + 1:].isdigit():
#         print(float(mesaj))
#     else:
#         print("Nu e numar")

try:
    print(float(mesaj))
except ValueError:
    print("Nu e numar")

# varsta = 26 # numere (intregi sau float)
# inaltimea = 1.81
#
# nume_prenume = "Breaz Catalin" # string-uri (siruri de caractere)
#
# traieste = True # valori boolene (bool - adevarat/fals si 0/1)
#
# o_noua_variabila = 26
#
# # print(id(varsta), varsta)
# # print(id(o_noua_variabila), o_noua_variabila)
# #
# # o_noua_variabila = o_noua_variabila + 5
# #
# # print(id(o_noua_variabila), o_noua_variabila)
# # print(varsta, type(varsta))
#
# # func(x1, x2, x3, y1=x4, y2=x5)
#
# varsta = int(input("Care este varsta ta?"))
# print(varsta * 2)

import math

cateta_1 = float(input("Introduceti cateta 1:"))
cateta_2 = float(input("Introduceti cateta 2:"))

a = cateta_1
b = cateta_2
c = math.sqrt((a * a) + (b * b))

ipotenuza = c

print(f"Ipotenuza este: {ipotenuza:.2f}")


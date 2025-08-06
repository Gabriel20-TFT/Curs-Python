inceput = int(input("De unde sa inceapa intervalul? "))
sfarsit = int(input("Unde sa se termine intervalul? "))

patrate = [i for i in range(inceput, sfarsit + 1) if (i ** 0.5) == int((i ** 0.5))]
# patrate = [i * i for i in range(int(inceput ** 0.5), int((sfarsit + 2) ** 0.5))]

print(patrate)

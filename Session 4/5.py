weight = float(input("Care e greutatea mea (in kg)?"))
height = float(input("Care e inaltimea mea (in metrii)?"))

bmi = weight / (height * height)

print("BMI este: ", bmi)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Healthy Weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obesity")

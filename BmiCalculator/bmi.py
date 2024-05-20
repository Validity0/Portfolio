weight = float(input("What is your Weight in LB?"))
height = float(input("What is your Hight in feet?"))

bmi = round(float((weight / (height * 12) ** 2) * 703), 1)
print("Your bmi is", bmi)
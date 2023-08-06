print("Welcome to BMI calculator.")

weight = float(input("Input your weight in kgs:" ))
height = float(input("Input your height in m:" ))

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"Your BMI {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI {bmi}, you are normal.")
elif bmi < 30:
    print(f"Your BMI {bmi}, you are overweight.")
elif bmi < 35:
    print(f"Your BMI {bmi}, you are obese.")
else:
    print(f"Your BMI {bmi}, you are clinically obese.")
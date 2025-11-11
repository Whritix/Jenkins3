import sys

if len(sys.argv) == 3:
    script_name = sys.argv[0]
    weight = float(sys.argv[1])
    height = float(sys.argv[2])
else:
    script_name = sys.argv[0]
    weight = 70.0
    height = 1.75

bmi = weight / (height ** 2)
print("Your BMI is:", bmi)

if bmi < 18.5:
    print("Underweight")
elif bmi <= 24.9:
    print("Normal weight")
else:
    print("Overweight")

print("Find your BMI using pounds and inches.")
weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))
bmi = 703 * weight/(height ** 2)
roundedbmi = round(bmi, 1)
print(f"You have a rounded BMI of: {roundedbmi}")
if roundedbmi < 18.5:
    print("You are underweight.")
elif 18.5 <= roundedbmi < 25:
    print("You have a normal weight.")
elif 25 < roundedbmi < 30:
    print("You are overweight.")
elif roundedbmi >= 30:
    print("You are obese.")

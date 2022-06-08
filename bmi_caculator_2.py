# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

result = weight/ height**2
result1 = round(result / 1)
print(result1)

if result1 <18.5:
  print(f"Your BMI is {result1}, you are underweight.")
elif result1 < 25:
  print(f"Your BMI is {result1}, you have a normal weight.")
elif result1 < 30:
  print(f"Your BMI is {result1}, you are slightly overweight.")
elif result1 < 35:
  print(f"Your BMI is {result1}, you are obese.")
else:
  print(f"Your BMI is {result1}, you are clinically obese.")
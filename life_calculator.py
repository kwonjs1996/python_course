# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆 365 52 12

#Write your code below this line 👇

live = 90 - int(age)
left_day = live * 365
left_week = live * 52
left_month = live * 12

print(f"You have {left_day} days, {left_week} weeks and {left_month} months left.")

#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
total_bill = input("What was the tatal bill? $")
give_per = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

tip_give_per = float(give_per)/100+1

tip = float(total_bill)/int(people)*tip_give_per
#tip_float2 = round(tip, 2)
tip_float2 = "{:.2f}".format(tip)
print(f"Each person should pay: ${tip_float2}")

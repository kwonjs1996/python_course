import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
pay = random.randint(0, len(names)-1)

pay_man = names[pay]

print(f"{pay_man} is going to buy the meal today!")

#pay_man = random.choice(names)
#print(f"{pay_man} is going to buy the meal today!")
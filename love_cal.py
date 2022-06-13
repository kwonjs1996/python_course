# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower_name1 = name1.lower()
lower_name2 = name2.lower()

print(lower_name1 + lower_name2)
print(type(lower_name1))

total_name = lower_name1 + lower_name2
print(total_name)
first_score = total_name.count("t") + total_name.count("r")+total_name.count("u")+total_name.count("e")
str(first_score)
print(first_score)
print(type(first_score))
second_score = total_name.count("l") + total_name.count("o") + total_name.count("v") + total_name.count("e")
print(second_score)
love_score = int(str(first_score) + str(second_score))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
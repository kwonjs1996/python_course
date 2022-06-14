import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
a = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
b = random.randint(0, 2)
list = [rock, paper, scissors]
if a >= 0 and a < 3:
    print(list[a])
else:
    print("Please check your choice")
print(list[b])

if a == b:
  print("Draw")
elif a == b-1:
  print('You lose')
elif a==0 and b==2:
  print("You Win")
elif a==1 and b==0:
  print("You win")
elif a==2 and b==0:
  print("You lose")
elif a== 2 and b==1:
  print("You win!")


# answer
#가위바위보_answer.py

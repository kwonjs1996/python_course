import random

answer = random.randrange(1,101)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

#난이도 정하고 난이도에 따른 값으로 실행하기
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
chance = 10
if difficulty == 'hard':
  chance = 5

while not chance == 0:
  print(f"You have {chance} attempts remaining to guess the number.{answer}")
  guess = int(input("Make a guess: "))
  if guess == answer:
    print(f"You got it! The answer was {answer}.")
    chance = 0
  elif guess > answer:
    print("Too high.")
    chance -= 1
  elif guess < answer:
    print("Too low. ")
    chance -= 1
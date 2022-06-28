import random
import art
from higher_lower import game_data


def pick():
  return random.choice(game_data.data)

print(art.logo)
#랜덤 데이터 가져오기
a = pick()
print(a)
name = a["name"]
description = a["description"]
country = a["country"]

print(f"Compare A: {name}, {description}, from {country}")

print(art.vs)
b = pick()

print(b)
name = b["name"]
description = b["description"]
country = b["country"]

print(f" B: {name}, {description}, from {country}")


user_pick = input("Who has more followers? Type 'A' or 'B': ").lower()

if user_pick == 'a':
  if a["follower_count"] > b["follower_count"]:
    print("correct a => a b => 다시뽑아 점수 1점 올려줘")
  else:
    print("end game")
elif user_pick == 'b':
  if a["follower_count"] < b["follower_count"]:
    print("correct b => a  c를 뽑아서 다시 점수 1점 올려줘")
    a = b
    print(f"a = {a}")
  else:
    print("end game")
else:
  print("you type wrong")
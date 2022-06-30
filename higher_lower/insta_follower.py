import random
import art
from higher_lower_answer import game_data


# 랜덤 데이터 가져오기
def pick():
    return random.choice(game_data.data)

a = pick()
b = pick()



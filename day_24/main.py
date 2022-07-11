# open(mode = "a": 파일 가장 밑에 추가, "r": 읽기전용, "w": 읽기쓰기)


with open("text.txt", mode="w") as file:
    file.write("hi")
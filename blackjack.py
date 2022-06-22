# import random
# # 처음 카드 배열 만들고 유저와 컴퓨터 랜덤한 숫자 2개 뽑기
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# user_cards = random.sample(cards, 2)
# computer_cards = random.sample(cards, 2)
# print(user_cards)
# print(computer_cards)
#
#
# def blackjack():
#     # from art import logo
#     # print(logo)
#     print(user_cards)
#     print(computer_cards)
#     user_current_score = 0
#     computer_current_score_now = False
#     # 컴퓨터 카드 합계가 17보다 낮을 때마다 더 뽑아서 변수 저장하기
#     while not computer_current_score_now:
#         computer_current_score = 0
#         for i in range(len(computer_cards)):
#             computer_current_score += computer_cards[i]
#         if computer_current_score < 17:
#             computer_cards.append(random.choice(cards))
#         else:
#             computer_current_score_now = True
#
#     print(computer_cards)
# # 유저에게 현 상황 보여주기
#     for i in range(len(user_cards)):
#         user_current_score += user_cards[i]
#     print(f"   Your cards: {user_cards}, current score: {user_current_score}")
#     print(f"   Computer's first card: {computer_cards[0]}")
#     # 유저에게 카드를 더 뽑을지 말지 물어보기
#     should_go = input("Type 'y' to get another card, type 'n' to pass: ")
#     # 유저가 더 뽑는다고 했을 때
#     if should_go == "y":
#         user_cards.append(random.choice(cards))
#         print(f"   Your cards: {user_cards}, current score: {user_current_score}")
#         print(f"   Computer's first card: {computer_cards[0]}")
#         for i in range(len(user_cards)):
#             user_current_score += user_cards[i]
#         if user_current_score > 21:
#             print(f"   Your final hand: {user_cards}, final score: {user_current_score}")
#             print(f"   Computer's final hand: {computer_cards}, final score: {computer_current_score}")
#             print("You went over. You lose ㅜㅜ")
#         else:
#             should_go = input("Type 'y' to get another card, type 'n' to pass: ")
#
#     def who_win():
#         if user_current_score <= 21:
#             if computer_current_score > 21:
#                 print(f"   Your final hand: {user_cards} final score: {user_current_score}")
#                 print(f"   Computer's final hand: {computer_cards}, final score: {computer_current_score}")
#                 print("Opponent went over. You win")
#             else:
#                 if user_current_score < computer_current_score:
#                     print(f"   Your final hand: {user_cards} final score: {user_current_score}")
#                     print(f"   Computer's final hand: {computer_cards}, final score: {computer_current_score}")
#                     print("You lose")
#                 elif user_current_score > computer_current_score:
#                     print(f"   Your final hand: {user_cards} final score: {user_current_score}")
#                     print(f"   Computer's final hand: {computer_cards}, final score: {computer_current_score}")
#                     print("You Win")
#                 elif user_current_score == computer_current_score:
#                     print(f"   Your final hand: {user_cards} final score: {user_current_score}")
#                     print(f"   Computer's final hand: {computer_cards}, final score: {computer_current_score}")
#
#
# start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
#
# if start == "y":
#     blackjack()
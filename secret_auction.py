import os

# HINT: You can call clear() to clear the output in the console.

print("Welcome to the secret auction program.")
user_list = []


clear = "\n" * 100


def blined_auction(name, bid):
    user_info = {}
    user_info["name"] = name
    user_info["bid"] = bid
    user_list.append(user_info)


new = False
highest_bid = 0
while not new:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    blined_auction(name, bid)
    other = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if other == "yes":
        new = False
        print(clear)
    if other == "no":
        new = True
        print(clear)
        for price in range(len(user_list)):
            if user_list[price]["bid"] > highest_bid:
                highest_bid = user_list[price]["bid"]
            # 굳이 쓸 필요가 없음 아무것도 안하면 되기때문에
            # else:
            #     highest_bid = highest_bid
            if highest_bid == user_list[price]["bid"]:
                winner_name = user_list[price]["name"]
        print(f"The winner is {winner_name} with a bid of $ {highest_bid}.")

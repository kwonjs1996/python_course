# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
price_s = 15
price_m = 20
price_l = 25

if size == "S":
    price_s
    if add_pepperoni == "Y":
        price_s += 2
        if extra_cheese == "Y":
            price_s += 1
            print(f"Your final bill is: ${price_s}.")
        elif extra_cheese == "N":
            price_s
            print(f"Your final bill is: ${price_s}.")
    elif add_pepperoni == "N":
        price_s
        if extra_cheese == "Y":
            price_s += 1
            print(f"Your final bill is: ${price_s}.")
        elif extra_cheese == "N":
            price_s
            print(f"Your final bill is: ${price_s}.")
    else:
        print("You choose wrong, Please check your choice")

elif size == "M":
    price_m
    if add_pepperoni == "Y":
        price_m += 3
        if extra_cheese == "Y":
            price_m += 1
            print(f"Your final bill is: ${price_m}.")
        elif extra_cheese == "N":
            price_m
            print(f"Your final bill is: ${price_m}.")
    elif add_pepperoni == "N":
        price_m
        if extra_cheese == "Y":
            price_m += 1
            print(f"Your final bill is: ${price_m}.")
        elif extra_cheese == "N":
            price_m
            print(f"Your final bill is: ${price_m}.")
    else:
        print("You choose wrong, Please check your choice")
elif size == "L":
    price_l
    if add_pepperoni == "Y":
        price_l += 3
        if extra_cheese == "Y":
            price_l += 1
            print(f"Your final bill is: ${price_l}.")
        elif extra_cheese == "N":
            price_l
            print(f"Your final bill is: ${price_l}.")
    elif add_pepperoni == "N":
        price_l
        if extra_cheese == "Y":
            price_l += 1
            print(f"Your final bill is: ${price_l}.")
        elif extra_cheese == "N":
            price_l
            print(f"Your final bill is: ${price_l}.")
    else:
        print("You choose wrong, Please check your choice")
else:
    print("You choose wrong size, Please check your choice")
    # if add_pepperoni == "Y":
    #   price_s+=2
    # elif add_pepperoni == "N":
    #   price_s
    #   if extra_cheese == "Y":
    #     price_s += 1
    #     print(f"Your final bill is: ${price_s}.")
    #   if extra_cheese == "N":
    #     price_s
    #     print(f"Your final bill is: ${price_s}.")

# else:
#   print("Small Pizza: $15")
# if size == "M":
#   print(f"Medium Pizza: ${price_m}")
# if size == "L":
#   print(f"Large Pizza: ${price_l}")

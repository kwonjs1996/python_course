# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
price_s = 15
price_m = 20
price_l = 25

if size == "S":
  price_s
  if add_pepperoni == "Y":
    price_s+=2
    print(f"Your final bill is: ${price_s}.")
    if extra_cheese == "Y":
      price_s += 1
      print(f"Your final bill is: ${price_s}.")
    else:
      price_s
      print(f"Your final bill is: ${price_s}.")
  else:
    price_s
    print(f"Your final bill is: ${price_s}.")





# else:
#   print("Small Pizza: $15")
# if size == "M":
#   print(f"Medium Pizza: ${price_m}")
# if size == "L":
#   print(f"Large Pizza: ${price_l}")
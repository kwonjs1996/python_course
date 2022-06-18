# Write your code below this line 👇
def prime_checker(number):
    a = []
    for i in range(2, number):
        b = str(number % i)
        a += b
    if "0" in a:
        print("not prime")
    else:
        print("Prime")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

##내코드
if year%4 == 0 and year%100 ==0 and year%400==0:
  print("윤달")
elif year%4 == 0 and year%100==0 and year%400!=0:
  print("Not Leap")
elif year%4 == 0 and year%100!=0:
  print("Leap")
else:
  print("Not Leap")

##강의코드
if year %4==0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
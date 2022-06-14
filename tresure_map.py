# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
x = [int(a) for a in str(position)]
a = x[0]-1
b = x[1]-1
print(x[0]-1)
print(x[1]-1)

map[b][a] = 'X   '
# 11 = [0][0]
# 21 = [0][1]
# 31 = [0][2]
# 12 = [1][0]
# 13 = [2][0]
#answer
# horizontal = int(position[0])
# vertical = int(position[1])

# selected_row = map[vertical - 1]
# selected_row[horizontal - 1]= 'X'
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
# import turtle
# # 개체의 속성 = attribute
# # 개체에 속한 함수 = Method
# # Object   Class(BluePrint)
# timmy = turtle.Turtle()
# print(timmy)
# # Objict  Method
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(200)
# timmy.left(200)
# # Object     Class(BluePrint)
# my_screen = turtle.Screen()
# # Object      attribute
# print(my_screen.canvheight)
# # Object    Method
# my_screen.exitonclick()

from prettytable import PrettyTable

tabel = PrettyTable()

tabel.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
tabel.add_column("Type",["Electric", "Water", "Fire"])
tabel.align = "r"
print(tabel)


# with open("weather_data.csv") as weather_data:
#     data1 = weather_data.readlines()
#     data = []
#     print(data1)
#     for i in range(len(data1)):
#         new_data = data1[i].replace("\n", "")
#         print(new_data)
#         data.append(new_data)
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# temp_list = data["temp"].to_list()
# print(temp_list)
# total_temp = 0
# for aver in temp_list:
#     total_temp += aver
# aver_temp = total_temp / len(temp_list)
# print(aver_temp)
# print(data["temp"].nlargest(1))
# print(data["temp"].max())
# highest_temp = data["temp"].max()
# print(highest_temp)
#
#
# print(data[data.temp == data["temp"].max()])

# Get data in row
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp
# print(monday_temp)
# print((monday.temp * 9/5)+32)

# Create a dataframe from scratch
# data_dict = {
#     "student": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.scv")

# for row in data:
    #     print(row[1])
    #     temperatures.append(row[1])
    # del temperatures[0]
    # print(temperatures)
    # for temp in temperatures:
    #     int(temp)
    #     print(type(int(temp)))
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"].tolist()
gray = []
cinnamon = []
black = []
for color in fur_color:
    if color == "Gray":
        gray.append(color)
    elif color == "Cinnamon":
        cinnamon.append(color)
    elif color == "Black":
        black.append(color)
print(len(fur_color))
print(len(gray))
print(len(cinnamon))
print(len(black))

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
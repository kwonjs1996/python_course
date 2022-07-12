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

data = pandas.read_csv("weather_data.csv")
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
data_dict = {
    "student": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.scv")

# for row in data:
    #     print(row[1])
    #     temperatures.append(row[1])
    # del temperatures[0]
    # print(temperatures)
    # for temp in temperatures:
    #     int(temp)
    #     print(type(int(temp)))

import requests
from datetime import datetime

USER_NAME = "ggam"
TOKEN = "kwonjs1996"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_confit = {
    "id": "graph1",
    "name": "coding",
    "unit": "commit",
    "type": "int",
    "color": "kuro",
}
## header 이용한 인증.
HEADER = {
    "X-USER-TOKEN": TOKEN,
}

today = datetime(year=2022, month=7, day=21)


# response = requests.post(url=graph_endpoint, json=graph_confit, headers=header)
# print(response.text)

post_pixel_endpoint = f"{graph_endpoint}/graph1"

update_pixel_endpoint = f"{post_pixel_endpoint}/20220721"

post_pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many commit today??")
}

# response = requests.post(url=post_pixel_endpoint, json=post_pixel_config, headers=HEADER)
# print(response.text)
response = requests.delete(update_pixel_endpoint, headers=HEADER)
print(response.text)

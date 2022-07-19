import requests
from datetime import datetime

MY_LAT = 37.525378  # 32 ~ 42
MY_LNG = 126.805377  # 121~131

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])

iss_position = (longitude, latitude)

print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(sunrise, sunset)
time_now = datetime.now()
print(time_now.hour)

while sunset < time_now.hour < sunrise:
    if 32 < latitude < 42 and 121 < longitude < 131:
        print("Look at the sky")
    else:
        pass

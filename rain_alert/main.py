import requests
import os

API_KEY = os.getenv('OWM_API_KEY')
LATITUDE = 37.566536
LONGITUDE = 126.977966
WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
weather_params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}
id_list = []
print(os.environ)

response = requests.get(WEATHER_ENDPOINT, params=weather_params)
weather_data = response.json()
print(weather_data)
print(weather_data["hourly"][0]["weather"][0]["id"])
for i in range(12):
    weather_id = weather_data["hourly"][i]["weather"][0]["id"]
    id_list.append(weather_id)
    if weather_id < 700:
        print("umbrella")
print(id_list)

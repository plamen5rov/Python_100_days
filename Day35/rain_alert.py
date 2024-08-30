import requests

#Params

API_KEY = "aa7f86b0e29a5e3a06a003fab53a4bcd"
LATITUDE = 42.697708
LONGITUDE = 23.321867
URL = f"https://api.openweathermap.org/data/2.5/forecast?lat={LATITUDE}&lon={LONGITUDE}&appid={API_KEY}"

response = requests.get(url=URL)
response.raise_for_status()
data = response.json()

#print(data)

#Alternative method

weather_params = {
    "lat":42.697708,
    "lon":23.321867,
    "appid":API_KEY,
    "cnt":4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", 
                        params=weather_params,
                        timeout=10)
response.raise_for_status()
weather_data = response.json()

# print(response.status_code)
# print(weather_data["list"][0]["weather"][0]["id"])
for n in range(0,4):
    weather_code = int(weather_data["list"][n]["weather"][0]["id"])
    if weather_code < 700:
        print("Bring an umbrella!")
    else:
        print("You don't need an umbrella!")
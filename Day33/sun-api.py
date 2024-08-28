import requests
import datetime

parameters = {
    "lat":42.666660, 
    "lng":23.324030,
    "formatted":0
    }

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()

print(data)

sunrise = data["results"]["sunrise"].split("T")[1].split("+")[0]
sunset = data["results"]["sunset"].split("T")[1].split("+")[0]
today=data["results"]["sunrise"].split("T")[0]

print(f"Today is {today} and sunrise starts at {sunrise} and sunsets is at {sunset}.")

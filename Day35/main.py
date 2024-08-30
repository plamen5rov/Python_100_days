from twilio.rest import Client
import requests
import os

#Params

API_KEY = os.environ.get("API_KEY")
LATITUDE = 42.697708
LONGITUDE = 23.321867
weather_params = {
    "lat":42.697708,
    "lon":23.321867,
    "appid":API_KEY,
    "cnt":4,
}

account_sid = os.environ.get("SID")
auth_token = os.environ.get("TWILIO_TOKEN")

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", 
                        params=weather_params,
                        timeout=10)
response.raise_for_status()
weather_data = response.json()
for n in range(0,4):
    weather_code = int(weather_data["list"][n]["weather"][0]["id"])
    if weather_code < 700:
        
        client = Client(account_sid, auth_token)
        message = client.messages.create(
        from_='+12625585117',
        body='Bring an umbrella!',
        to='+359888849888')
        print(message.status
              )
    else:
        print("You don't need an umbrella!")




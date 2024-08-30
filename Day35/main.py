from twilio.rest import Client
import requests

#Params

API_KEY = "aa7f86b0e29a5e3a06a003fab53a4bcd"
LATITUDE = 42.697708
LONGITUDE = 23.321867
weather_params = {
    "lat":42.697708,
    "lon":23.321867,
    "appid":API_KEY,
    "cnt":4,
}

account_sid = 'ACa2fcd2a09692aff1ccb9f86214c83171'
auth_token = 'fcd4e7085259d82abb95322f06f07c7d'

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
        print(message.status)
    else:
        print("You don't need an umbrella!")



